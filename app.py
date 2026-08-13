from flask import Flask, render_template, redirect, url_for
from flask_login import login_required, current_user
from config import Config
from models import db, login_manager, bcrypt, init_models
import os


def create_app(config_class=Config):
    """Application factory"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'

    # Initialize models
    with app.app_context():
        init_models()
        db.create_all()

        # Create default admin if not exists
        from models.user import User

        admin = User.query.filter_by(username='admin').first()

        if not admin:
            hashed_password = bcrypt.generate_password_hash(
                'admin123'
            ).decode('utf-8')

            admin = User(
                username='admin',
                password=hashed_password,
                role='admin',
                full_name='System Administrator',
                email='admin@attendance.com'
            )

            db.session.add(admin)
            db.session.commit()

            print(
                "Default admin created - "
                "Username: admin, Password: admin123"
            )

    # Register blueprints
    from routes.auth import auth
    from routes.admin import admin
    from routes.lecturer import lecturer
    from routes.student import student

    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(lecturer)
    app.register_blueprint(student)

    # Main routes
    @app.route('/')
    def index():
        """Landing page"""
        if current_user.is_authenticated:
            return redirect(url_for('main.dashboard'))

        return render_template('index.html')

    @app.route('/dashboard')
    @login_required
    def dashboard():
        """Main dashboard - redirects based on role"""

        if current_user.is_admin():
            return redirect(url_for('admin.dashboard'))

        elif current_user.is_lecturer():
            return redirect(url_for('lecturer.dashboard'))

        elif current_user.is_student():
            return redirect(url_for('student.my_attendance'))

        else:
            return redirect(url_for('index'))

    # Register main blueprint for dashboard route
    from flask import Blueprint

    main = Blueprint('main', __name__)

    main.add_url_rule(
        '/dashboard',
        'dashboard',
        dashboard
    )

    main.add_url_rule(
        '/',
        'index',
        index
    )

    app.register_blueprint(main)

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template(
            'errors/404.html'
        ), 404

    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template(
            'errors/403.html'
        ), 403

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()

        return render_template(
            'errors/500.html'
        ), 500

    return app


if __name__ == '__main__':
    app = create_app()

    # Allow other devices on the same Wi-Fi network
    # to access the Flask application.
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
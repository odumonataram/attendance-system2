from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, bcrypt
from models.user import User
from utils.validators import sanitize_input

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Login page for admin and lecturer"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        username = sanitize_input(request.form.get('username'))
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            if user.role in ['admin', 'lecturer']:
                login_user(user)
                next_page = request.args.get('next')
                flash(f'Welcome back, {user.full_name}!', 'success')
                return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
            else:
                flash('Students cannot login from this page. Please scan QR code to mark attendance.', 'warning')
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('login.html')

@auth.route('/student-login/<token>', methods=['GET', 'POST'])
def student_login(token):
    """Student login via QR code scan"""
    from models.qr_session import QRSession
    
    # Verify QR session exists and is valid
    qr_session = QRSession.query.filter_by(qr_code_data=token).first()
    
    if not qr_session:
        flash('Invalid QR code.', 'danger')
        return render_template('student/invalid_qr.html')
    
    if qr_session.is_expired():
        flash('This QR code has expired. Please ask your lecturer to generate a new one.', 'warning')
        return render_template('student/expired_qr.html')
    
    if request.method == 'POST':
        matric_number = sanitize_input(request.form.get('matric_number'))
        name = sanitize_input(request.form.get('name'))
        password = request.form.get('password')
        
        # Find student by matric number
        student = User.query.filter_by(matric_number=matric_number, role='student').first()
        
        if not student:
            flash('Student not found. Please check your matric number.', 'danger')
            return render_template('student/login.html', token=token, qr_session=qr_session)
        
        # Verify password
        if not bcrypt.check_password_hash(student.password, password):
            flash('Invalid password.', 'danger')
            return render_template('student/login.html', token=token, qr_session=qr_session)
        
        # Verify name matches
        if student.full_name.lower() != name.lower():
            flash('Name does not match our records.', 'danger')
            return render_template('student/login.html', token=token, qr_session=qr_session)
        
        # Check if student is registered for this course
        from models.course import CourseRegistration
        registration = CourseRegistration.query.filter_by(
            student_id=student.id,
            course_id=qr_session.course_id
        ).first()
        
        if not registration:
            flash('You are not registered for this course.', 'danger')
            return render_template('student/not_registered.html', course=qr_session.course)
        
        # Login student temporarily for marking attendance
        login_user(student)
        return redirect(url_for('student.mark_attendance', session_id=qr_session.id))
    
    return render_template('student/login.html', token=token, qr_session=qr_session)

@auth.route('/logout')
@login_required
def logout():
    """Logout current user"""
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('main.index'))

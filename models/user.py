from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # admin, lecturer, student
    full_name = db.Column(db.String(150), nullable=False)
    matric_number = db.Column(db.String(50), unique=True, nullable=True)  # For students only
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    courses_taught = db.relationship('Course', backref='lecturer', lazy=True, foreign_keys='Course.lecturer_id')
    course_registrations = db.relationship('CourseRegistration', backref='student', lazy=True)
    attendance_records = db.relationship('Attendance', backref='student', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username} - {self.role}>'
    
    def is_admin(self):
        return self.role == 'admin'
    
    def is_lecturer(self):
        return self.role == 'lecturer'
    
    def is_student(self):
        return self.role == 'student'

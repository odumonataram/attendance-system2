from . import db
from datetime import datetime

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), nullable=False)
    course_name = db.Column(db.String(150), nullable=False)
    lecturer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    section = db.Column(db.String(10), nullable=False)  # A, B, C, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    registrations = db.relationship('CourseRegistration', backref='course', lazy=True, cascade='all, delete-orphan')
    qr_sessions = db.relationship('QRSession', backref='course', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Course {self.course_code} - {self.course_name} (Section {self.section})>'
    
    def get_registered_students_count(self):
        return len(self.registrations)

class CourseRegistration(db.Model):
    __tablename__ = 'course_registrations'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Unique constraint to prevent duplicate registrations
    __table_args__ = (db.UniqueConstraint('student_id', 'course_id', name='unique_student_course'),)
    
    def __repr__(self):
        return f'<CourseRegistration Student:{self.student_id} Course:{self.course_id}>'

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db
from models.qr_session import QRSession
from models.attendance import Attendance
from models.course import CourseRegistration
from utils.decorators import student_required

student = Blueprint('student', __name__, url_prefix='/student')

@student.route('/scan/<token>')
def scan(token):
    """Redirect to student login with token"""
    return redirect(url_for('auth.student_login', token=token))

@student.route('/mark-attendance/<int:session_id>', methods=['GET', 'POST'])
@login_required
@student_required
def mark_attendance(session_id):
    """Mark attendance for student"""
    qr_session = QRSession.query.get_or_404(session_id)
    
    # Check if session is expired
    if qr_session.is_expired():
        flash('This attendance session has expired.', 'warning')
        return render_template('student/expired_qr.html')
    
    # Check if student is registered for this course
    registration = CourseRegistration.query.filter_by(
        student_id=current_user.id,
        course_id=qr_session.course_id
    ).first()
    
    if not registration:
        flash('You are not registered for this course.', 'danger')
        return render_template('student/not_registered.html', course=qr_session.course)
    
    if request.method == 'POST':
        # Mark attendance
        ip_address = request.remote_addr
        attendance, message = Attendance.mark_attendance(
            student_id=current_user.id,
            qr_session_id=session_id,
            ip_address=ip_address
        )
        
        if attendance:
            flash(message, 'success')
            return render_template('student/attendance_success.html',
                                 course=qr_session.course,
                                 attendance=attendance)
        else:
            flash(message, 'warning')
            return render_template('student/attendance_marked.html', course=qr_session.course)
    
    return render_template('student/mark_attendance.html',
                         qr_session=qr_session,
                         course=qr_session.course)

@student.route('/my-attendance')
@login_required
@student_required
def my_attendance():
    """View student's attendance history"""
    # Get all courses student is registered for
    registrations = CourseRegistration.query.filter_by(student_id=current_user.id).all()
    
    courses_data = []
    for reg in registrations:
        course = reg.course
        
        # Get all sessions for this course
        all_sessions = QRSession.query.filter_by(course_id=course.id).count()
        
        # Get attendance records for this student in this course
        attended_sessions = db.session.query(Attendance).join(QRSession).filter(
            Attendance.student_id == current_user.id,
            QRSession.course_id == course.id
        ).count()
        
        # Calculate attendance percentage
        attendance_percentage = (attended_sessions / all_sessions * 100) if all_sessions > 0 else 0
        
        courses_data.append({
            'course': course,
            'total_sessions': all_sessions,
            'attended_sessions': attended_sessions,
            'attendance_percentage': round(attendance_percentage, 2)
        })
    
    return render_template('student/my_attendance.html', courses_data=courses_data)

@student.route('/course-attendance/<int:course_id>')
@login_required
@student_required
def course_attendance(course_id):
    """View detailed attendance for a specific course"""
    # Verify student is registered for this course
    registration = CourseRegistration.query.filter_by(
        student_id=current_user.id,
        course_id=course_id
    ).first()
    
    if not registration:
        flash('You are not registered for this course.', 'danger')
        return redirect(url_for('student.my_attendance'))
    
    course = registration.course
    
    # Get all attendance records for this student in this course
    attendance_records = db.session.query(Attendance, QRSession).join(QRSession).filter(
        Attendance.student_id == current_user.id,
        QRSession.course_id == course_id
    ).order_by(Attendance.marked_at.desc()).all()
    
    return render_template('student/course_attendance.html',
                         course=course,
                         attendance_records=attendance_records)

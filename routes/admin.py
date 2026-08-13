from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models import db, bcrypt
from models.user import User
from models.course import Course
from utils.decorators import admin_required
from utils.validators import validate_email, validate_username, validate_password, validate_matric_number, validate_course_code, sanitize_input

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/dashboard')
@login_required
@admin_required
def dashboard():
    """Admin dashboard"""
    total_lecturers = User.query.filter_by(role='lecturer').count()
    total_students = User.query.filter_by(role='student').count()
    total_courses = Course.query.count()
    
    recent_lecturers = User.query.filter_by(role='lecturer').order_by(User.created_at.desc()).limit(5).all()
    recent_students = User.query.filter_by(role='student').order_by(User.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         total_lecturers=total_lecturers,
                         total_students=total_students,
                         total_courses=total_courses,
                         recent_lecturers=recent_lecturers,
                         recent_students=recent_students)

@admin.route('/lecturers')
@login_required
@admin_required
def lecturers():
    """View all lecturers"""
    all_lecturers = User.query.filter_by(role='lecturer').order_by(User.full_name).all()
    return render_template('admin/lecturers.html', lecturers=all_lecturers)

@admin.route('/add-lecturer', methods=['GET', 'POST'])
@login_required
@admin_required
def add_lecturer():
    """Add new lecturer"""
    if request.method == 'POST':
        username = sanitize_input(request.form.get('username'))
        password = request.form.get('password')
        full_name = sanitize_input(request.form.get('full_name'))
        email = sanitize_input(request.form.get('email'))
        
        # Validation
        if not validate_username(username):
            flash('Invalid username format. Use 3-20 alphanumeric characters.', 'danger')
            return render_template('admin/add_lecturer.html')
        
        if not validate_password(password):
            flash('Password must be at least 6 characters long.', 'danger')
            return render_template('admin/add_lecturer.html')
        
        if not validate_email(email):
            flash('Invalid email format.', 'danger')
            return render_template('admin/add_lecturer.html')
        
        # Check if username or email already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return render_template('admin/add_lecturer.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'danger')
            return render_template('admin/add_lecturer.html')
        
        # Create lecturer
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        lecturer = User(
            username=username,
            password=hashed_password,
            role='lecturer',
            full_name=full_name,
            email=email
        )
        
        db.session.add(lecturer)
        db.session.commit()
        
        flash(f'Lecturer {full_name} added successfully!', 'success')
        return redirect(url_for('admin.assign_courses', lecturer_id=lecturer.id))
    
    return render_template('admin/add_lecturer.html')

@admin.route('/assign-courses/<int:lecturer_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def assign_courses(lecturer_id):
    """Assign courses to lecturer"""
    lecturer = User.query.get_or_404(lecturer_id)
    
    if lecturer.role != 'lecturer':
        flash('Invalid lecturer.', 'danger')
        return redirect(url_for('admin.lecturers'))
    
    if request.method == 'POST':
        # Get course data from form
        course_codes = request.form.getlist('course_code[]')
        course_names = request.form.getlist('course_name[]')
        sections = request.form.getlist('section[]')
        
        # Create courses
        for i in range(len(course_codes)):
            if course_codes[i] and course_names[i]:
                course_code = sanitize_input(course_codes[i]).upper()
                course_name = sanitize_input(course_names[i])
                section = sanitize_input(sections[i]).upper()
                
                if not validate_course_code(course_code):
                    flash(f'Invalid course code format: {course_code}. Use format like CSC301.', 'warning')
                    continue
                
                # Check if course already exists for this lecturer
                existing = Course.query.filter_by(
                    course_code=course_code,
                    lecturer_id=lecturer_id,
                    section=section
                ).first()
                
                if not existing:
                    course = Course(
                        course_code=course_code,
                        course_name=course_name,
                        lecturer_id=lecturer_id,
                        section=section
                    )
                    db.session.add(course)
        
        db.session.commit()
        flash(f'Courses assigned to {lecturer.full_name} successfully!', 'success')
        return redirect(url_for('admin.lecturers'))
    
    existing_courses = Course.query.filter_by(lecturer_id=lecturer_id).all()
    return render_template('admin/assign_courses.html', lecturer=lecturer, existing_courses=existing_courses)

@admin.route('/students')
@login_required
@admin_required
def students():
    """View all students"""
    all_students = User.query.filter_by(role='student').order_by(User.full_name).all()
    return render_template('admin/students.html', students=all_students)

@admin.route('/add-student', methods=['GET', 'POST'])
@login_required
@admin_required
def add_student():
    """Add new student"""
    if request.method == 'POST':
        username = sanitize_input(request.form.get('username'))
        password = request.form.get('password')
        full_name = sanitize_input(request.form.get('full_name'))
        matric_number = sanitize_input(request.form.get('matric_number')).upper()
        email = sanitize_input(request.form.get('email'))
        
        # Validation
        if not validate_username(username):
            flash('Invalid username format. Use 3-20 alphanumeric characters.', 'danger')
            return render_template('admin/add_student.html')
        
        if not validate_password(password):
            flash('Password must be at least 6 characters long.', 'danger')
            return render_template('admin/add_student.html')
        
        if not validate_matric_number(matric_number):
            flash('Invalid matric number format. Use 6-15 alphanumeric characters.', 'danger')
            return render_template('admin/add_student.html')
        
        if not validate_email(email):
            flash('Invalid email format.', 'danger')
            return render_template('admin/add_student.html')
        
        # Check if username, email, or matric number already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return render_template('admin/add_student.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'danger')
            return render_template('admin/add_student.html')
        
        if User.query.filter_by(matric_number=matric_number).first():
            flash('Matric number already exists.', 'danger')
            return render_template('admin/add_student.html')
        
        # Create student
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        student = User(
            username=username,
            password=hashed_password,
            role='student',
            full_name=full_name,
            matric_number=matric_number,
            email=email
        )
        
        db.session.add(student)
        db.session.commit()
        
        flash(f'Student {full_name} added successfully!', 'success')
        return redirect(url_for('admin.students'))
    
    return render_template('admin/add_student.html')

@admin.route('/courses')
@login_required
@admin_required
def courses():
    """View all courses"""
    all_courses = Course.query.order_by(Course.course_code).all()
    return render_template('admin/courses.html', courses=all_courses)

@admin.route('/delete-user/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
    """Delete a user"""
    user = User.query.get_or_404(user_id)
    
    if user.role == 'admin':
        flash('Cannot delete admin users.', 'danger')
        return redirect(url_for('admin.dashboard'))
    
    db.session.delete(user)
    db.session.commit()
    
    flash(f'{user.full_name} deleted successfully.', 'success')
    
    if user.role == 'lecturer':
        return redirect(url_for('admin.lecturers'))
    else:
        return redirect(url_for('admin.students'))

@admin.route('/delete-course/<int:course_id>', methods=['POST'])
@login_required
@admin_required
def delete_course(course_id):
    """Delete a course"""
    course = Course.query.get_or_404(course_id)
    
    db.session.delete(course)
    db.session.commit()
    
    flash(f'Course {course.course_code} deleted successfully.', 'success')
    return redirect(url_for('admin.courses'))

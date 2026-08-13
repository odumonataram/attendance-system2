"""
Setup script to initialize database with sample data
Run this after first installation to populate the system with test data
"""

from app import create_app
from models import db, bcrypt
from models.user import User
from models.course import Course, CourseRegistration
from datetime import datetime

def create_sample_data():
    """Create sample data for testing"""
    
    app = create_app()
    
    with app.app_context():
        # Clear existing data (optional - comment out if you want to keep existing data)
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()
        
        # Create Admin (always create)
        print("Creating admin user...")
        admin = User(
            username='admin',
            password=bcrypt.generate_password_hash('admin123').decode('utf-8'),
            role='admin',
            full_name='System Administrator',
            email='admin@attendance.com'
        )
        db.session.add(admin)
        
        # Create Lecturers
        print("Creating lecturers...")
        lecturers_data = [
            {
                'username': 'lecturer1',
                'password': 'pass123',
                'full_name': 'Dr. John Smith',
                'email': 'john.smith@university.edu',
                'courses': [
                    ('CSC301', 'Data Structures', 'A'),
                    ('CSC302', 'Algorithms', 'B'),
                    ('CSC303', 'Database Systems', 'A')
                ]
            },
            {
                'username': 'lecturer2',
                'password': 'pass123',
                'full_name': 'Prof. Sarah Johnson',
                'email': 'sarah.johnson@university.edu',
                'courses': [
                    ('MTH201', 'Linear Algebra', 'A'),
                    ('MTH202', 'Calculus II', 'B'),
                    ('MTH203', 'Discrete Mathematics', 'A')
                ]
            },
            {
                'username': 'lecturer3',
                'password': 'pass123',
                'full_name': 'Dr. Michael Brown',
                'email': 'michael.brown@university.edu',
                'courses': [
                    ('EEE401', 'Digital Electronics', 'A'),
                    ('EEE402', 'Circuit Analysis', 'B'),
                    ('EEE403', 'Control Systems', 'A')
                ]
            },
            {
                'username': 'lecturer4',
                'password': 'pass123',
                'full_name': 'Dr. Emily Davis',
                'email': 'emily.davis@university.edu',
                'courses': [
                    ('PHY301', 'Quantum Physics', 'A')
                ]
            }
        ]
        
        lecturers = []
        for lec_data in lecturers_data:
            lecturer = User(
                username=lec_data['username'],
                password=bcrypt.generate_password_hash(lec_data['password']).decode('utf-8'),
                role='lecturer',
                full_name=lec_data['full_name'],
                email=lec_data['email']
            )
            db.session.add(lecturer)
            db.session.flush()  # Get the lecturer ID
            
            # Add courses for this lecturer
            for course_code, course_name, section in lec_data['courses']:
                course = Course(
                    course_code=course_code,
                    course_name=course_name,
                    lecturer_id=lecturer.id,
                    section=section
                )
                db.session.add(course)
            
            lecturers.append(lecturer)
        
        # Create Students
        print("Creating students...")
        students_data = [
            ('student1', 'pass123', 'Alice Williams', 'STU001', 'alice.williams@student.edu'),
            ('student2', 'pass123', 'Bob Anderson', 'STU002', 'bob.anderson@student.edu'),
            ('student3', 'pass123', 'Charlie Martinez', 'STU003', 'charlie.martinez@student.edu'),
            ('student4', 'pass123', 'Diana Garcia', 'STU004', 'diana.garcia@student.edu'),
            ('student5', 'pass123', 'Edward Lee', 'STU005', 'edward.lee@student.edu'),
            ('student6', 'pass123', 'Fiona Wang', 'STU006', 'fiona.wang@student.edu'),
            ('student7', 'pass123', 'George Chen', 'STU007', 'george.chen@student.edu'),
            ('student8', 'pass123', 'Hannah Kim', 'STU008', 'hannah.kim@student.edu'),
            ('student9', 'pass123', 'Ian Patel', 'STU009', 'ian.patel@student.edu'),
            ('student10', 'pass123', 'Julia Rodriguez', 'STU010', 'julia.rodriguez@student.edu'),
        ]
        
        students = []
        for username, password, full_name, matric, email in students_data:
            student = User(
                username=username,
                password=bcrypt.generate_password_hash(password).decode('utf-8'),
                role='student',
                full_name=full_name,
                matric_number=matric,
                email=email
            )
            db.session.add(student)
            students.append(student)
        
        db.session.commit()
        
        # Register students for courses
        print("Registering students for courses...")
        courses = Course.query.all()
        
        # Register first 5 students for all Computer Science courses
        cs_courses = Course.query.filter(Course.course_code.like('CSC%')).all()
        for course in cs_courses:
            for student in students[:5]:
                registration = CourseRegistration(
                    student_id=student.id,
                    course_id=course.id
                )
                db.session.add(registration)
        
        # Register students 3-8 for Mathematics courses
        math_courses = Course.query.filter(Course.course_code.like('MTH%')).all()
        for course in math_courses:
            for student in students[2:8]:
                registration = CourseRegistration(
                    student_id=student.id,
                    course_id=course.id
                )
                db.session.add(registration)
        
        # Register students 5-10 for Engineering courses
        eee_courses = Course.query.filter(Course.course_code.like('EEE%')).all()
        for course in eee_courses:
            for student in students[4:10]:
                registration = CourseRegistration(
                    student_id=student.id,
                    course_id=course.id
                )
                db.session.add(registration)
        
        # Register first 4 students for Physics
        phy_courses = Course.query.filter(Course.course_code.like('PHY%')).all()
        for course in phy_courses:
            for student in students[:4]:
                registration = CourseRegistration(
                    student_id=student.id,
                    course_id=course.id
                )
                db.session.add(registration)
        
        db.session.commit()
        
        print("\n" + "="*60)
        print("✅ Database initialized successfully with sample data!")
        print("="*60)
        print("\n📊 SUMMARY:")
        print(f"   - 1 Admin created")
        print(f"   - {len(lecturers)} Lecturers created")
        print(f"   - {len(students)} Students created")
        print(f"   - {Course.query.count()} Courses created")
        print(f"   - {CourseRegistration.query.count()} Course registrations")
        
        print("\n🔐 LOGIN CREDENTIALS:")
        print("\n   ADMIN:")
        print("   Username: admin")
        print("   Password: admin123")
        
        print("\n   LECTURERS (all have password: pass123):")
        for lec in lecturers_data:
            print(f"   - {lec['username']} ({lec['full_name']})")
        
        print("\n   STUDENTS (all have password: pass123):")
        for username, _, full_name, matric, _ in students_data:
            print(f"   - {username} / {matric} ({full_name})")
        
        print("\n" + "="*60)
        print("🚀 You can now run: python app.py")
        print("="*60 + "\n")

if __name__ == '__main__':
    create_sample_data()

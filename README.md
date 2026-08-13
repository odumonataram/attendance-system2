# 📚 QR Code Attendance System

A modern, web-based attendance tracking system using QR codes. Built with Python Flask, this system allows lecturers to generate time-limited QR codes for attendance, and students to mark their attendance by scanning these codes with their smartphones.

## 🌟 Features

### Admin Panel
- Add and manage lecturers
- Add and manage students
- Assign courses to lecturers (3 courses per lecturer)
- View system statistics
- Manage all courses and users

### Lecturer Panel
- View assigned courses
- Register students for courses
- Generate time-limited QR codes (15-minute expiration)
- View real-time attendance as students mark it
- View attendance history for each course
- Export attendance records to Excel
- Manage registered students per course

### Student Panel
- Scan QR code with smartphone
- Secure login with matric number and password
- Mark attendance (one-time per session)
- View personal attendance history
- See attendance statistics per course

## 🔒 Security Features

- Password hashing with bcrypt
- Time-limited QR codes (15 minutes)
- Session management with Flask-Login
- Role-based access control
- Duplicate attendance prevention
- Course registration verification

## 🛠️ Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML, CSS, JavaScript
- **QR Code**: Python qrcode library
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Export**: Pandas, OpenPyXL

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

### 1. Clone or Download the Project

```bash
cd attendance-system
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## 👤 Default Admin Login

After first run, use these credentials:

- **Username**: `admin`
- **Password**: `admin123`

**⚠️ IMPORTANT**: Change the default admin password immediately after first login!

## 📱 How to Use

### For Administrators

1. Login with admin credentials
2. Go to Admin Dashboard
3. Add lecturers and assign courses (3 per lecturer)
4. Add students to the system
5. Monitor system usage

### For Lecturers

1. Login with provided credentials
2. View your assigned courses
3. Register students for your courses
4. Generate QR code for attendance
5. Display QR code to students
6. View real-time attendance
7. Export attendance records

### For Students

1. Scan QR code displayed by lecturer (using phone camera)
2. Enter matric number, name, and password
3. Click "Mark Attendance"
4. Receive confirmation
5. View attendance history anytime

## 📊 Database Schema

### Users Table
- Stores admins, lecturers, and students
- Unique usernames and email addresses
- Hashed passwords for security

### Courses Table
- Course code, name, section
- Linked to lecturer

### Course Registrations
- Links students to courses
- Prevents duplicate registrations

### QR Sessions
- Time-limited QR codes
- Linked to specific courses
- Auto-expire after 15 minutes

### Attendance Table
- Records attendance marks
- Prevents duplicate entries
- Tracks timestamp and IP

## 🔧 Configuration

Edit `config.py` to customize:

```python
# Secret key for sessions
SECRET_KEY = 'your-secret-key-here'

# Database URL
SQLALCHEMY_DATABASE_URI = 'sqlite:///attendance.db'

# QR code expiration (minutes)
QR_CODE_EXPIRATION = 15
```

## 📦 Project Structure

```
attendance-system/
├── app.py                  # Main application
├── config.py               # Configuration
├── requirements.txt        # Dependencies
├── models/                 # Database models
│   ├── user.py
│   ├── course.py
│   ├── qr_session.py
│   └── attendance.py
├── routes/                 # Application routes
│   ├── auth.py
│   ├── admin.py
│   ├── lecturer.py
│   └── student.py
├── templates/              # HTML templates
│   ├── admin/
│   ├── lecturer/
│   └── student/
├── static/                 # Static files
│   ├── css/
│   └── js/
└── utils/                  # Utility functions
    ├── qr_generator.py
    ├── validators.py
    └── decorators.py
```

## 🌐 Deployment

### For Production

1. Change `SECRET_KEY` in config.py
2. Use PostgreSQL instead of SQLite
3. Set `DEBUG = False`
4. Use a production WSGI server (Gunicorn)
5. Set up HTTPS
6. Configure firewall rules

### Example with Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: Database doesn't exist
**Solution**: Delete `attendance.db` and restart the app

**Issue**: QR code doesn't scan
**Solution**: Ensure phone camera has proper lighting and focus

**Issue**: Student can't mark attendance
**Solution**: Verify student is registered for the course

**Issue**: QR code expired
**Solution**: Generate a new QR code (they expire after 15 minutes)

## 📝 Sample Courses

The system supports any courses. Here are examples:

**Computer Science:**
- CSC301 - Data Structures
- CSC302 - Algorithms
- CSC303 - Database Systems

**Mathematics:**
- MTH201 - Linear Algebra
- MTH202 - Calculus II
- MTH203 - Discrete Mathematics

**Engineering:**
- EEE401 - Digital Electronics
- EEE402 - Circuit Analysis
- EEE403 - Control Systems

## 🔐 Security Best Practices

1. Change default admin password
2. Use strong passwords for all users
3. Keep dependencies updated
4. Use HTTPS in production
5. Regular database backups
6. Limit QR code validity period
7. Monitor for suspicious activity

## 📈 Future Enhancements

- Mobile app for students
- Biometric verification
- Geolocation verification
- Email notifications
- SMS alerts
- Detailed analytics dashboard
- Bulk student import (CSV)
- Multi-language support

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Check Flask documentation

## 📄 License

This project is for educational purposes.

## 👨‍💻 Author

Created for modern attendance tracking in educational institutions.

---

**Note**: This system is designed for educational institutions. Customize as needed for your specific requirements.

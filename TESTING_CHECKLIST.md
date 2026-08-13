# ✅ Testing Checklist

Use this checklist to ensure all features are working correctly.

## 🔧 Installation & Setup

- [ ] Python 3.8+ installed
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] No installation errors
- [ ] Database created successfully
- [ ] Sample data loaded (if running setup.py)

## 👤 Authentication & Access Control

### Admin Login
- [ ] Can login with admin credentials
- [ ] Can logout successfully
- [ ] Cannot access without login
- [ ] Admin dashboard displays correctly

### Lecturer Login
- [ ] Can login with lecturer credentials
- [ ] Can logout successfully
- [ ] Cannot access admin routes
- [ ] Cannot access student routes
- [ ] Lecturer dashboard displays correctly

### Student Login
- [ ] Can login via QR code scan
- [ ] Login requires correct matric number, name, and password
- [ ] Wrong credentials show error message
- [ ] Cannot login from regular login page
- [ ] Student panel displays correctly

## 🎛️ Admin Panel Features

### Lecturer Management
- [ ] Can view all lecturers
- [ ] Can add new lecturer with validation
- [ ] Username must be unique
- [ ] Email must be unique and valid format
- [ ] Password minimum 6 characters
- [ ] Can assign courses to lecturer
- [ ] Course code validation (3 letters + 3 digits)
- [ ] Can delete lecturer
- [ ] Deletion confirmation works

### Student Management
- [ ] Can view all students
- [ ] Can add new student with validation
- [ ] Username must be unique
- [ ] Matric number must be unique
- [ ] Email must be unique and valid
- [ ] Can delete student
- [ ] Deletion confirmation works

### Course Management
- [ ] Can view all courses
- [ ] Can see lecturer assigned to each course
- [ ] Can see number of registered students
- [ ] Can delete course
- [ ] Deletion removes related data

## 👨‍🏫 Lecturer Panel Features

### Course Management
- [ ] Can view only assigned courses
- [ ] Course details display correctly
- [ ] Student count is accurate

### Student Registration
- [ ] Can view all students for registration
- [ ] Can select multiple students
- [ ] Already registered students are marked
- [ ] Cannot register same student twice
- [ ] Success message after registration
- [ ] Can unregister students
- [ ] Unregister confirmation works

### QR Code Generation
- [ ] Can generate QR code for each course
- [ ] QR code displays clearly
- [ ] Timer shows correct expiration time
- [ ] QR code expires after 15 minutes
- [ ] Old QR codes are deactivated when new one is generated
- [ ] QR code contains correct URL

### Attendance Tracking
- [ ] Can view real-time attendance
- [ ] New attendance appears automatically
- [ ] Total present count is accurate
- [ ] Total absent count is accurate
- [ ] Attendance percentage calculated correctly
- [ ] Student details display correctly
- [ ] Timestamp is accurate

### Attendance History
- [ ] Can view all past sessions
- [ ] Sessions display in correct order (newest first)
- [ ] Can view attendance for each session
- [ ] Session status (active/expired) is correct

### Export Functionality
- [ ] Can export attendance to Excel
- [ ] Excel file downloads successfully
- [ ] Excel contains all required columns
- [ ] Data in Excel is accurate
- [ ] Filename includes course code and timestamp

## 👨‍🎓 Student Panel Features

### QR Code Scanning
- [ ] QR code URL works when scanned
- [ ] QR code URL works when manually opened
- [ ] Expired QR shows error message
- [ ] Invalid QR shows error message

### Attendance Marking
- [ ] Login form displays correctly
- [ ] Requires all three fields (matric, name, password)
- [ ] Wrong credentials show error
- [ ] Name mismatch shows error
- [ ] Verification checks course registration
- [ ] Non-registered student cannot mark attendance
- [ ] Registered student can mark attendance
- [ ] Success message displays after marking
- [ ] Cannot mark attendance twice for same session
- [ ] Duplicate attempt shows appropriate message

### Attendance History
- [ ] Can view all registered courses
- [ ] Attendance statistics are accurate
- [ ] Can view detailed attendance per course
- [ ] Dates and times are correct
- [ ] Attendance percentage calculated correctly

## 🔒 Security Tests

### Authentication
- [ ] Cannot access protected routes without login
- [ ] Session persists correctly
- [ ] Session expires after timeout
- [ ] Logout clears session

### Authorization
- [ ] Admin cannot be deleted
- [ ] Students cannot access lecturer routes
- [ ] Lecturers cannot access admin routes
- [ ] Lecturers can only view their own courses
- [ ] Students can only view their own attendance

### Data Validation
- [ ] SQL injection attempts fail
- [ ] XSS attempts are sanitized
- [ ] Invalid email formats rejected
- [ ] Invalid course codes rejected
- [ ] Password requirements enforced

### QR Code Security
- [ ] QR codes have unique tokens
- [ ] Tokens are cryptographically secure
- [ ] Expired codes cannot be used
- [ ] Used tokens cannot be reused

## 🎨 UI/UX Tests

### Responsive Design
- [ ] Works on desktop (1920x1080)
- [ ] Works on laptop (1366x768)
- [ ] Works on tablet (768x1024)
- [ ] Works on mobile (375x667)
- [ ] Navigation works on all screen sizes

### Visual Elements
- [ ] Logo displays correctly
- [ ] Colors are consistent
- [ ] Buttons have hover effects
- [ ] Forms are properly aligned
- [ ] Tables are readable
- [ ] Flash messages are visible
- [ ] Flash messages auto-hide after 5 seconds

### User Experience
- [ ] Navigation is intuitive
- [ ] Buttons are clearly labeled
- [ ] Error messages are helpful
- [ ] Success messages are encouraging
- [ ] Loading states are clear
- [ ] No broken links
- [ ] All images load correctly

## 🐛 Error Handling

### 404 - Not Found
- [ ] Custom 404 page displays
- [ ] Can navigate back from 404

### 403 - Forbidden
- [ ] Custom 403 page displays
- [ ] Shows when accessing unauthorized route

### 500 - Server Error
- [ ] Custom 500 page displays
- [ ] Database errors handled gracefully

### Form Errors
- [ ] Validation errors display clearly
- [ ] Empty fields show error
- [ ] Invalid formats show specific error
- [ ] Duplicate entries show error

## 📊 Data Integrity

### Database
- [ ] No orphaned records
- [ ] Foreign keys work correctly
- [ ] Cascade deletes work properly
- [ ] Unique constraints enforced
- [ ] Data types are correct

### Relationships
- [ ] One lecturer has many courses
- [ ] One course has many students
- [ ] One student has many courses
- [ ] Attendance links correctly to student and session

## ⚡ Performance

### Page Load Times
- [ ] Homepage loads in < 2 seconds
- [ ] Dashboard loads in < 2 seconds
- [ ] QR generation is instant
- [ ] Attendance marking is instant
- [ ] Export downloads quickly

### Database Queries
- [ ] No N+1 query problems
- [ ] Queries are optimized
- [ ] Large tables load efficiently

## 🔄 Edge Cases

### Attendance
- [ ] Marking attendance on last minute before expiry works
- [ ] Marking attendance after expiry fails
- [ ] Student not registered for course cannot mark
- [ ] Multiple students can mark simultaneously

### Course Registration
- [ ] Cannot register student twice
- [ ] Cannot register for non-existent course
- [ ] Unregistering removes only that registration

### QR Codes
- [ ] Generating new QR deactivates old one
- [ ] Cannot use QR from different course
- [ ] Cannot use QR from different section

## 📱 Mobile Testing

### QR Scanning
- [ ] Phone camera recognizes QR code
- [ ] QR URL opens in mobile browser
- [ ] Mobile login form works
- [ ] Mobile keyboard appears correctly
- [ ] Mobile attendance marking works

### Mobile UI
- [ ] Layout adapts to mobile screen
- [ ] Buttons are touchable
- [ ] Text is readable
- [ ] No horizontal scrolling
- [ ] Forms work on mobile

## 🚀 Production Readiness

### Configuration
- [ ] SECRET_KEY is changed from default
- [ ] DEBUG is set to False for production
- [ ] Database is PostgreSQL (not SQLite)
- [ ] All environment variables are set

### Security
- [ ] Default admin password changed
- [ ] HTTPS is configured
- [ ] CSRF protection enabled
- [ ] Rate limiting implemented (if applicable)

### Backup
- [ ] Database backup strategy in place
- [ ] Backup restore tested
- [ ] Data export works

---

## 📝 Test Results Template

```
Date: __________
Tester: __________
Environment: Development / Production

Total Tests: ___
Passed: ___
Failed: ___
Skipped: ___

Critical Issues Found:
1. 
2. 

Minor Issues Found:
1. 
2. 

Recommendations:
1. 
2. 

Overall Status: ☐ Ready ☐ Not Ready

Tester Signature: __________
```

---

## 🎯 Quick Smoke Test (5 minutes)

For quick verification after changes:

1. [ ] Admin can login
2. [ ] Lecturer can login
3. [ ] QR code generates successfully
4. [ ] Student can scan and mark attendance
5. [ ] Attendance appears in lecturer view
6. [ ] Export to Excel works

If all 6 pass, system is likely working correctly!

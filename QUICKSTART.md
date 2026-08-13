# 🚀 Quick Start Guide

Get the Attendance System up and running in 5 minutes!

## Step 1: Install Dependencies

```bash
cd attendance-system
pip install -r requirements.txt
```

## Step 2: Initialize Database with Sample Data (Optional but Recommended)

```bash
python setup.py
```

This will create:
- 1 Admin account
- 4 Lecturers with courses
- 10 Students
- Course registrations

## Step 3: Run the Application

```bash
python app.py
```

Open your browser and go to: `http://localhost:5000`

---

## 🔐 Default Login Credentials

### Admin
- **Username**: `admin`
- **Password**: `admin123`

### Lecturers (Password: `pass123` for all)
- **lecturer1** - Dr. John Smith (CSC courses)
- **lecturer2** - Prof. Sarah Johnson (MTH courses)
- **lecturer3** - Dr. Michael Brown (EEE courses)
- **lecturer4** - Dr. Emily Davis (PHY courses)

### Students (Password: `pass123` for all)
- **student1** / **STU001** - Alice Williams
- **student2** / **STU002** - Bob Anderson
- **student3** / **STU003** - Charlie Martinez
- **student4** / **STU004** - Diana Garcia
- **student5** / **STU005** - Edward Lee
- ... (10 students total)

---

## 📱 Quick Test Flow

### Test as Lecturer:
1. Login as `lecturer1` / `pass123`
2. Click "My Courses"
3. Select a course (e.g., CSC301)
4. Click "Generate QR Code"
5. Display the QR code

### Test as Student:
1. **Option A**: Use your phone to scan the QR code
2. **Option B**: Copy the URL from the QR page and open in another browser
3. Login with student credentials (e.g., `STU001` / `Alice Williams` / `pass123`)
4. Click "Mark Attendance"
5. See success message!

### View Attendance:
1. Go back to lecturer view
2. Click "View Live Attendance"
3. See the student who just marked attendance
4. Click "Export to Excel" to download the attendance report

---

## 🎯 Main Features to Try

### As Admin:
- Add new lecturers
- Add new students
- Assign courses to lecturers
- View all system data

### As Lecturer:
- Register students for your courses
- Generate QR codes for attendance
- View real-time attendance updates
- Export attendance to Excel
- View attendance history

### As Student:
- Scan QR code to mark attendance
- View your attendance records
- Check attendance percentage per course

---

## ⚠️ Important Notes

1. **QR Codes Expire**: QR codes are valid for 15 minutes only
2. **One Attendance Per Session**: Students can't mark attendance twice for the same session
3. **Must Be Registered**: Students must be registered for a course to mark attendance
4. **Change Admin Password**: Change the default admin password immediately!

---

## 🐛 Troubleshooting

**Can't install dependencies?**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Database error?**
```bash
# Delete the database and recreate
rm attendance.db
python setup.py
```

**Port already in use?**
Edit `app.py` and change port 5000 to another port like 5001:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

---

## 📖 Next Steps

1. Read the full `README.md` for detailed documentation
2. Explore all features as different user roles
3. Add your own lecturers and students
4. Customize the system for your institution

---

## 💡 Tips

- Use the **setup.py** script to reset the database with fresh sample data anytime
- Test the QR code scanning with your phone's camera app
- Export attendance regularly for backup
- Monitor the real-time attendance view when students are marking attendance

---

**Need help?** Check the README.md file for detailed documentation!

**Ready to start?** Run `python app.py` and visit `http://localhost:5000`

Happy tracking! 📚✨

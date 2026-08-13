from . import db
from datetime import datetime

class Attendance(db.Model):
    __tablename__ = 'attendance'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    qr_session_id = db.Column(db.Integer, db.ForeignKey('qr_sessions.id'), nullable=False)
    marked_at = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(50), nullable=True)
    
    # Unique constraint to prevent duplicate attendance marking
    __table_args__ = (db.UniqueConstraint('student_id', 'qr_session_id', name='unique_attendance'),)
    
    def __repr__(self):
        return f'<Attendance Student:{self.student_id} Session:{self.qr_session_id}>'
    
    @classmethod
    def mark_attendance(cls, student_id, qr_session_id, ip_address=None):
        """Mark attendance for a student in a QR session"""
        # Check if already marked
        existing = cls.query.filter_by(
            student_id=student_id,
            qr_session_id=qr_session_id
        ).first()
        
        if existing:
            return None, "Attendance already marked for this session"
        
        # Create new attendance record
        attendance = cls(
            student_id=student_id,
            qr_session_id=qr_session_id,
            ip_address=ip_address
        )
        
        db.session.add(attendance)
        db.session.commit()
        
        return attendance, "Attendance marked successfully"

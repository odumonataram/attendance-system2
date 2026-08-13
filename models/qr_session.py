from . import db
from datetime import datetime, timedelta
import secrets

class QRSession(db.Model):
    __tablename__ = 'qr_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    qr_code_data = db.Column(db.String(200), unique=True, nullable=False)
    generated_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relationships
    attendance_records = db.relationship('Attendance', backref='qr_session', lazy=True)
    
    def __repr__(self):
        return f'<QRSession {self.qr_code_data} - Active:{self.is_active}>'
    
    @staticmethod
    def generate_token():
        """Generate a unique token for QR code"""
        return secrets.token_urlsafe(32)
    
    def is_expired(self):
        """Check if QR session has expired"""
        return datetime.utcnow() > self.expires_at or not self.is_active
    
    def deactivate(self):
        """Deactivate the QR session"""
        self.is_active = False
        db.session.commit()
    
    @classmethod
    def create_session(cls, course_id, expiration_minutes=15):
        """Create a new QR session with expiration"""
        token = cls.generate_token()
        expires_at = datetime.utcnow() + timedelta(minutes=expiration_minutes)
        
        session = cls(
            course_id=course_id,
            qr_code_data=token,
            expires_at=expires_at,
            is_active=True
        )
        
        db.session.add(session)
        db.session.commit()
        
        return session

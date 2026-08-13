import os
from datetime import timedelta

class Config:
    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-this-in-production'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///attendance.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
    
    # QR Code expiration time (in minutes)
    QR_CODE_EXPIRATION = 15
    
    # Upload folder
    UPLOAD_FOLDER = 'static/uploads'
    
    # Maximum file size (16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

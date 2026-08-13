import re

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_matric_number(matric):
    """Validate matric number format (alphanumeric, 6-15 characters)"""
    if not matric:
        return False
    pattern = r'^[A-Za-z0-9]{6,15}$'
    return re.match(pattern, matric) is not None

def validate_username(username):
    """Validate username (alphanumeric and underscore, 3-20 characters)"""
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    return re.match(pattern, username) is not None

def validate_password(password):
    """Validate password (minimum 6 characters)"""
    return len(password) >= 6

def validate_course_code(course_code):
    """Validate course code format"""
    pattern = r'^[A-Z]{3}\d{3}$'
    return re.match(pattern, course_code.upper()) is not None

def sanitize_input(text):
    """Remove potentially harmful characters"""
    if not text:
        return ""
    return text.strip()

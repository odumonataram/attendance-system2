import qrcode
from io import BytesIO
import base64

def generate_qr_code(data):
    """
    Generate QR code from data and return as base64 string
    
    Args:
        data: String data to encode in QR code
        
    Returns:
        base64 encoded PNG image string
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    return f"data:image/png;base64,{img_base64}"

def generate_attendance_url(base_url, token):
    """
    Generate full attendance URL from token
    
    Args:
        base_url: Base URL of the application
        token: QR session token
        
    Returns:
        Full URL string
    """
    return f"{base_url}/student/scan/{token}"

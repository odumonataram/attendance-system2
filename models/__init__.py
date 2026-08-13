from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

# Import models after db initialization to avoid circular imports
def init_models():
    from . import user, course, attendance, qr_session

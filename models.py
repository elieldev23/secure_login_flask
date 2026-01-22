from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    # Unique user ID
    id = db.Column(db.Integer, primary_key=True)

    # Email address (must be unique)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)

    # Hashed password (never store plain text passwords)
    password_hash = db.Column(db.String(255), nullable=False)

    # Account creation date
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

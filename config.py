import os

class Config:
    # Secret key used to sign sessions and cookies
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")

    # Database location (SQLite by default)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secure session cookie settings
    SESSION_COOKIE_HTTPONLY = True      # Prevent JavaScript access to cookies
    SESSION_COOKIE_SAMESITE = "Lax"     # Protect against CSRF
    SESSION_COOKIE_SECURE = False       # Set True when using HTTPS

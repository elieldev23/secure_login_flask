from flask import Flask, render_template, request, redirect, session, url_for
from passlib.hash import bcrypt
from dotenv import load_dotenv
from functools import wraps

from config import Config
from models import db, User

# Load environment variables from .env
load_dotenv()

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Create DB tables if needed
with app.app_context():
    db.create_all()

def login_required(view_func):
    # Decorator to protect routes that require authentication
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return view_func(*args, **kwargs)
    return wrapper

@app.route("/")
def home():
    # Redirect depending on authentication state
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    # If user is already logged in, redirect
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        if len(password) < 10:
            return "Password must be at least 10 characters"

        if User.query.filter_by(email=email).first():
            return "User already exists"

        password_hash = bcrypt.hash(password)

        user = User(email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # If user is already logged in, redirect
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        # Verify password using bcrypt
        if not user or not bcrypt.verify(password, user.password_hash):
            return "Invalid credentials"

        # Clear any previous session and set the logged-in user
        session.clear()
        session["user_id"] = user.id

        return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    # Read user info from DB using session user_id
    user = User.query.get(session["user_id"])
    return render_template("dashboard.html", email=user.email)

@app.route("/logout")
def logout():
    # Clear the session to log out user
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

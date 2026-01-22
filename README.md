# Secure_Login_System_flask

A secure user authentication system built with Flask and SQLite.

## Features

- User registration  
- User login  
- Password hashing with bcrypt  
- Secure session management  
- Protected routes (dashboard)  
- Logout system  
- Environment-based secret configuration  
- SQLite database storage  

## Security Practices

- Passwords are never stored in plain text  
- bcrypt is used with automatic salting  
- Sessions use HTTPOnly cookies  
- Sensitive data is stored in a .env file  
- Protected routes require authentication  

## Technologies

- Python  
- Flask  
- SQLite  
- bcrypt (via passlib)  
- HTML  

## How to Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

## Project Goal

This project demonstrates secure authentication, password protection, and session management following modern web security best practices.

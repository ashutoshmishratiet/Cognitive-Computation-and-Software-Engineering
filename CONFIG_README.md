# Authentication System - Configuration Guide

## Email Configuration Setup

The system includes email verification functionality. To enable it:

### Option 1: Gmail (Recommended for testing)

1. Go to your Google Account settings
2. Enable 2-Factor Authentication
3. Generate an App Password:
   - Go to Security > 2-Step Verification > App passwords
   - Select "Mail" and "Windows Computer"
   - Copy the 16-character password
4. Update in `auth_app.py`:
   ```python
   app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your-16-char-app-password'
   ```

### Option 2: Disable Email Verification (for testing)

To run the system without email verification:
1. In `auth_app.py`, find the register route
2. After creating the user, set `user.is_verified = True`
3. Remove or comment out the `send_verification_email()` call

Example modification in auth_app.py (line ~180):
```python
user.is_verified = True  # Add this line to skip email verification
# send_verification_email(user.email, user.verification_token)  # Comment this out
```

## Database

The system uses SQLite by default. The database file `auth_system.db` will be created automatically.

### Manual Admin Creation

To add admins manually via Python shell:

```python
from auth_app import app, db, Admin

with app.app_context():
    admin = Admin(
        username='youradmin',
        email='admin@example.com',
        full_name='Your Name',
        role='super_admin'
    )
    admin.set_password('your_secure_password')
    db.session.add(admin)
    db.session.commit()
    print("Admin created successfully!")
```

## Default Credentials

A default admin is created automatically:
- Username: `admin`
- Password: `admin123`

**⚠️ IMPORTANT: Change this password immediately after first login!**

## Security Notes

1. Change the SECRET_KEY in production
2. Use environment variables for sensitive data
3. Enable HTTPS in production
4. Regularly update passwords
5. Monitor admin access logs

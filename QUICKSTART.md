# Quick Start Guide - Authentication System

## Installation & Setup

1. Install required packages:
```bash
pip install -r requirements_auth.txt
```

2. Run the application:
```bash
python auth_app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Default Admin Access

- Username: `admin`
- Password: `admin123`
- Login as: **Administrator**

## User Registration Flow

1. Click "Register" on the home page
2. Fill in the registration form
3. Submit the form
4. Check email for verification link (if email is configured)
5. Click verification link
6. Login with your credentials

## Quick Test (Without Email Verification)

For immediate testing without email setup:

1. Edit `auth_app.py` at line ~180 in the register route
2. Add `user.is_verified = True` after creating the user
3. Comment out the email sending line
4. Register a new user and login immediately

## Features

✅ User registration with email verification
✅ Secure password hashing
✅ Separate user and admin dashboards
✅ Session management
✅ SQLite database storage
✅ Responsive UI design

## Troubleshooting

**Issue: Can't login after registration**
- Verify email verification is working or disabled
- Check if user.is_verified is set to True

**Issue: Email not sending**
- Configure email settings in auth_app.py
- Or disable email verification for testing

**Issue: Database errors**
- Delete `auth_system.db` file
- Restart the application (it will recreate the database)

## File Structure

```
cogn/
├── auth_app.py              # Main Flask application
├── requirements_auth.txt    # Python dependencies
├── CONFIG_README.md         # Configuration guide
├── QUICKSTART.md           # This file
├── templates/
│   ├── base.html           # Base template
│   ├── index.html          # Home page
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   ├── user_dashboard.html # User dashboard
│   └── admin_dashboard.html # Admin dashboard
└── auth_system.db          # SQLite database (auto-created)
```

## Next Steps

1. Configure email settings (see CONFIG_README.md)
2. Change default admin password
3. Test user registration and login
4. Customize dashboards as needed
5. Add additional features

## Support

For issues or questions, check CONFIG_README.md for detailed configuration options.

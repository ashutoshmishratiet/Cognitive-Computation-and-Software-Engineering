# Integration Guide - Flask Auth + Streamlit Dashboard

## System Architecture

```
Login System (Flask) ──┬──> Admin Dashboard
http://localhost:5000  │    (File Management)
                       │
                       ├──> Streamlit Dashboard
                       │    http://localhost:8501
                       │    (Data Visualization)
                       │
                       └──> User Dashboard
                            (Profile View)
```

## Project Structure

```
cogn/
├── auth_app.py                    # Main Flask app with authentication
├── admin_dashboard_routes.py      # Admin file upload routes
├── streamlit_app.py               # Streamlit cognitive dashboard
├── add_admin.py                   # Admin management script
├── requirements_auth.txt          # Python dependencies
├── templates/
│   ├── base.html                 # Base template
│   ├── index.html                # Home page
│   ├── login.html                # Login page
│   ├── register.html             # User registration
│   ├── user_dashboard.html       # User dashboard
│   ├── admin_dashboard.html      # Admin overview
│   ├── admin_upload.html         # File upload page
│   └── admin_files.html          # File management
├── uploads/                       # Uploaded data files
├── auth_system.db                # SQLite database
├── QUICKSTART.md                 # Quick start guide
└── CONFIG_README.md              # Configuration guide
```

## Running the Complete System

### Step 1: Install Dependencies

```bash
cd c:\Users\Anshika Rana\OneDrive\Desktop\cogn
pip install -r requirements_auth.txt
```

### Step 2: Start Flask Authentication Server

**Terminal 1:**
```bash
python auth_app.py
```

Access at: http://localhost:5000

### Step 3: Start Streamlit Dashboard (Admin Only)

**Terminal 2:**
```bash
streamlit run streamlit_app.py
```

Access at: http://localhost:8501

## How to Use the System

### User Workflow

1. **Register**
   - Go to http://localhost:5000
   - Click "Register"
   - Fill in details and submit
   - User is auto-verified (email disabled)

2. **Login**
   - Select "Regular User"
   - Enter username and password
   - Access user dashboard

3. **View Dashboard**
   - See profile information
   - View analytics (coming soon)

### Admin Workflow

1. **Login**
   - Go to http://localhost:5000
   - Click "Login"
   - Select "Administrator"
   - Use: username=`admin`, password=`admin123`
   - Access admin dashboard

2. **Upload Data**
   - Click "📤 Upload Data" button
   - Upload Excel file (.xlsx, .xls, or .csv)
   - File is stored in `uploads/` folder

3. **View Uploaded Files**
   - Click "📁 Manage Files"
   - See all uploaded files
   - Download or delete files

4. **View Cognitive Dashboard**
   - Click "📊 View Dashboard"
   - Opens Streamlit app at http://localhost:8501
   - Displays data from latest uploaded file

## File Upload Details

### Supported Formats
- Excel: .xlsx, .xls
- CSV: .csv
- Maximum size: 50 MB

### Expected Sheet Name
- "Excel 3BM" (or first sheet if not found)

### Expected Columns
**Technical Scores:**
- U_raw, U_S, U_S1, D_raw, etc.
- T1, T2, T3, CL1

**Emotion Scores:**
- P1_B_Decimal through P7_A_Decimal
- Total_B_Decimal, B1, B1_Scaled, Emotion_Value

### File Storage
```
uploads/
├── 20260131_120000_Technical_data.xlsx
├── 20260131_130000_Updated_data.xlsx
└── uploads.json  # Upload metadata
```

## Database Schema

### Users Table
```
id              | Integer    | Primary Key
username        | String(80) | Unique
email           | String(120)| Unique
password_hash   | String(200)|
full_name       | String(100)|
phone           | String(20) |
date_of_birth   | Date       |
is_verified     | Boolean    | Default: True
verification_token| String(100)|
created_at      | DateTime   |
```

### Admins Table
```
id              | Integer    | Primary Key
username        | String(80) | Unique
email           | String(120)| Unique
password_hash   | String(200)|
full_name       | String(100)|
role            | String(50) | Default: 'admin'
created_at      | DateTime   |
last_login      | DateTime   |
```

## API Routes

### Authentication Routes
- `GET  /` - Home page
- `GET  /register` - Registration form
- `POST /register` - Submit registration
- `GET  /login` - Login form
- `POST /login` - Submit login
- `GET  /logout` - Logout user
- `GET  /verify/<token>` - Email verification (disabled)

### User Routes
- `GET  /user/dashboard` - User dashboard

### Admin Routes
- `GET  /admin/dashboard` - Admin overview
- `GET  /admin/upload` - Upload form
- `POST /admin/upload` - Submit file upload
- `GET  /admin/files` - List all files
- `GET  /admin/download/<filename>` - Download file
- `POST /admin/delete/<filename>` - Delete file

## Troubleshooting

### Flask App Won't Start
```
Error: Address already in use
Solution: Port 5000 is taken. Kill the process or use different port.
```

### Streamlit Won't Connect
```
Error: Cannot connect to localhost:8501
Solution: Make sure Streamlit is running in a separate terminal.
```

### File Upload Failed
```
Error: File size exceeds limit
Solution: Maximum file size is 50 MB. Compress your file.
```

### Database Errors
```
Error: Database locked
Solution: Delete auth_system.db and restart (it will recreate).
```

## Admin Management

### Add New Admin via Script

```bash
python add_admin.py
```

Follow the interactive prompts to add a new administrator.

### Add Admin via Python

```python
from auth_app import app, db, Admin

with app.app_context():
    admin = Admin(
        username='newadmin',
        email='admin@company.com',
        full_name='Admin Name',
        role='admin'
    )
    admin.set_password('secure_password')
    db.session.add(admin)
    db.session.commit()
```

## Security Notes

⚠️ **Important for Production:**

1. Change the default admin password immediately
2. Use environment variables for secret keys
3. Enable HTTPS
4. Implement rate limiting
5. Add CSRF protection
6. Validate all file uploads
7. Use a production WSGI server (not Flask debug)

## Default Credentials

- **Username:** admin
- **Password:** admin123

⚠️ **Change immediately after first login!**

## Next Steps

1. ✅ Test user registration and login
2. ✅ Test admin file upload
3. ✅ View data in Streamlit dashboard
4. ✅ Download exported files
5. 🔲 Customize UI colors and branding
6. 🔲 Add email verification (if needed)
7. 🔲 Implement user-specific reports
8. 🔲 Add data processing pipeline

## Support & Documentation

- **Quick Start:** See QUICKSTART.md
- **Configuration:** See CONFIG_README.md
- **Flask Docs:** https://flask.palletsprojects.com/
- **Streamlit Docs:** https://docs.streamlit.io/
- **SQLAlchemy Docs:** https://docs.sqlalchemy.org/

---

**System Status:** ✅ Ready for Use
**Last Updated:** January 31, 2026

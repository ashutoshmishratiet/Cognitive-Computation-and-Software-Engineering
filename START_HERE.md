# 🚀 START HERE - Simple Setup Guide

## What You're Getting

A complete authentication system for your Cognitive Load Assessment project with:
- Login/Registration system
- User and Admin separate accounts
- Admin can upload Excel files
- Professional Dashboard with data visualization

---

## ⚡ Quick Start (5 Minutes)

### Step 1: Flask Server is Already Running ✅
Your Flask server is currently running at: **http://localhost:5000**

### Step 2: Start Streamlit (NEW Terminal)

**Open PowerShell and go to your project:**
```bash
cd c:\Users\Anshika Rana\OneDrive\Desktop\cogn
streamlit run streamlit_app.py
```

Streamlit will start at: **http://localhost:8501**

### Step 3: Done! 🎉

Visit: **http://localhost:5000**

---

## 🧪 Try It Out (Right Now)

### Test 1: Login as Admin
1. Go to http://localhost:5000
2. Click "Login"
3. Enter:
   - Username: `admin`
   - Password: `admin123`
   - Select: "Administrator"
4. Click Login

### Test 2: Create a User
1. Click "Logout"
2. Click "Register"
3. Fill in:
   - Username: `john`
   - Email: `john@example.com`
   - Password: `john123456`
   - Full Name: `John Doe`
4. Click "Create Account"
5. Go to Login, select "Regular User", enter same details

### Test 3: Upload Data
1. Login as admin (username: admin, password: admin123)
2. Click "📤 Upload Data"
3. Click to upload a file (Excel: .xlsx, .xls or CSV)
4. Upload your Cognitive data file
5. Click "📊 View Dashboard" to see visualization

---

## 📱 System Overview

```
┌─────────────────────────────────┐
│   YOUR APPLICATION (Port 5000)  │
├─────────────────────────────────┤
│  Login  │  Register  │  Logout  │
└─────────────────────────────────┘
         │
    User / Admin Login
         │
    ┌────┴─────┐
    │           │
Regular User  Administrator
    │           │
User Page   Admin Page
(Profile)   ├─ Upload File
            ├─ Manage Files
            └─ View Dashboard
                (Port 8501)
```

---

## 📁 Where Are My Files?

- **Uploaded Excel files:** `c:\...\Desktop\cogn\uploads\`
- **Database:** `c:\...\Desktop\cogn\auth_system.db`
- **Code:** All in `c:\...\Desktop\cogn\`

---

## 🔑 Accounts You Can Use

### Admin Account (Pre-created)
- **Username:** admin
- **Password:** admin123
- **Role:** Can upload files, view dashboard

### Create User Accounts
- Use "Register" button
- You create your own username & password
- Auto-verified (no email needed)

---

## 📊 Admin Actions

### Upload File
1. Login as admin
2. Click "📤 Upload Data" button
3. Select your Excel file (.xlsx, .xls)
4. Click Upload

### Manage Files
1. Login as admin
2. Click "📁 Manage Files"
3. See all uploaded files
4. Download or Delete

### View Dashboard
1. Login as admin
2. Click "📊 View Dashboard"
3. Opens Cognitive Analytics at Port 8501
4. See data visualizations

---

## 💾 Database (Auto-Created)

Two tables:
1. **Users Table** - For regular users
   - Username, Email, Password, Phone, DOB
   
2. **Admins Table** - For administrators
   - Username, Email, Password, Role

All passwords are securely encrypted!

---

## 🐛 Having Issues?

### Issue: Can't reach http://localhost:5000
**Fix:** Make sure Flask server is running in the terminal. You should see:
```
Running on http://127.0.0.1:5000
```

### Issue: Login not working
**Try:** Username: `admin`, Password: `admin123`, Select: "Administrator"

### Issue: Upload button not visible
**Fix:** Make sure you're logged in as admin

### Issue: Streamlit page blank
**Fix:** Open a NEW terminal and run: `streamlit run streamlit_app.py`

### Issue: Uploaded file not showing
**Fix:**
1. Check file uploaded successfully (see success message)
2. Restart Streamlit: Stop (Ctrl+C) and restart

---

## 📚 Detailed Guides Available

- **QUICKSTART.md** - Detailed quick start
- **README.md** - Full system overview
- **TESTING_GUIDE.md** - How to test everything
- **CONFIG_README.md** - Configuration options
- **INTEGRATION_GUIDE.md** - Technical details

---

## ✅ Checklist

- [ ] Flask server running at localhost:5000
- [ ] Can access login page
- [ ] Can login as admin (admin/admin123)
- [ ] Can see admin dashboard
- [ ] Can create a new user
- [ ] Can upload a file
- [ ] Started Streamlit server
- [ ] Can access Streamlit at localhost:8501
- [ ] Streamlit shows uploaded data

---

## 🎯 What's Next?

1. **Test with your real data** - Upload your cognitive assessment Excel file
2. **Create multiple users** - Practice the registration system
3. **Explore visualizations** - Check Streamlit dashboard features
4. **Customize** - Change colors/themes in template files
5. **Deploy** - When ready, deploy to production server

---

## 💡 Pro Tips

- First admin is auto-created: `admin` / `admin123`
- Always change default admin password
- Users are auto-verified (email skipped for ease)
- Files are stored with timestamp: `20260131_120000_filename.xlsx`
- Each upload tracked in `uploads/uploads.json`
- Use `add_admin.py` to create more admins

---

## 🆘 Still Stuck?

**Check error in Flask terminal:**
1. Look at the terminal window where Flask is running
2. Copy any error message
3. Google the error or ask for help

**Quick Restart:**
1. Close Flask terminal (Ctrl+C)
2. Close Streamlit (Ctrl+C)
3. Restart Flask: `python auth_app.py`
4. In new terminal, restart Streamlit: `streamlit run streamlit_app.py`

---

## 🎓 Learning Resources

- **Flask Official:** https://flask.palletsprojects.com/
- **Streamlit Official:** https://docs.streamlit.io/
- **SQLite Tutorial:** https://www.sqlitetutorial.net/
- **Python Virtual Env:** https://docs.python.org/3/tutorial/venv.html

---

**Version:** 2.0 - Complete Integration  
**Date:** January 31, 2026  
**Status:** ✅ Ready to Use

---

## 🚀 Start Now!

1. Flask is already running → Visit http://localhost:5000
2. Open new terminal → Run `streamlit run streamlit_app.py`
3. Login with admin credentials
4. Upload a file
5. View your cognitive dashboard!

**Happy analyzing! 📊**

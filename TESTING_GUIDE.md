# System Testing & Demo Guide

## Quick Test Checklist

### ✅ Phase 1: User Registration & Login

- [ ] Open http://localhost:5000
- [ ] Click "Register"
- [ ] Fill in test user info:
  - Username: `testuser`
  - Email: `test@example.com`
  - Password: `test123456`
  - Full Name: `Test User`
- [ ] Verify success message appears
- [ ] Login with: Username `testuser`, Password `test123456`, Type: User
- [ ] Verify redirected to user dashboard
- [ ] Check profile information displays correctly
- [ ] Click Logout

### ✅ Phase 2: Admin Login

- [ ] Click Login
- [ ] Select "Administrator"
- [ ] Use:
  - Username: `admin`
  - Password: `admin123`
- [ ] Verify redirected to admin dashboard
- [ ] Check stats display (Users, Admins, Verified Users, Data Files)
- [ ] Click Logout

### ✅ Phase 3: File Upload

- [ ] Login as admin
- [ ] Click "📤 Upload Data" button
- [ ] Upload your Excel file:
  - Use `Technical_data_with_all_scores.xlsx` if available
  - Or create a test file with required columns
- [ ] Verify success message
- [ ] Verify file appears in recent uploads list
- [ ] Click "📁 Manage Files"
- [ ] Verify file listed with correct details
- [ ] Test Download button

### ✅ Phase 4: Streamlit Dashboard Integration

- [ ] Admin logged in
- [ ] In quick actions, click "📊 View Dashboard"
- [ ] Should open http://localhost:8501 (Streamlit app)
- [ ] Verify data loads from uploaded file
- [ ] Navigate through pages:
  - [ ] Overview
  - [ ] Technical Performance
  - [ ] Affective Dynamics
  - [ ] Individual Profiles
  - [ ] Data Export
  - [ ] About
- [ ] Test export functionality

### ✅ Phase 5: Admin Features

- [ ] Login as admin
- [ ] Test File Management:
  - [ ] Upload multiple files
  - [ ] Delete a file
  - [ ] Download a file
  - [ ] View file details
- [ ] Check Users table displays all registered users
- [ ] Check Admins table displays all admins

### ✅ Phase 6: User Features

- [ ] Login as regular user
- [ ] Verify cannot access admin routes
- [ ] Verify only see user dashboard
- [ ] Verify profile information correct
- [ ] Verify logout works

## Test Data Sample

If you need to create a test Excel file quickly:

**Create file with these columns:**
```
ID, U_raw, U_S, U_S1, D_raw, T1, T2, T3, CL1, 
P1_B_Decimal, P2_B_Decimal, P3_B_Decimal, Total_B_Decimal, 
B1, B1_Scaled, Emotion_Value
```

**Sample values:**
```
1, 2.5, 0.85, 0.90, 1.2, 0.75, 0.80, 0.85, 0.70, 
0.6, 0.7, 0.65, 0.65, 2, 1.5, 0.68
```

## Expected Behaviors

### ✅ Registration Success
- Email verification skipped
- User auto-verified
- Flash message: "Registration successful! You can now login..."

### ✅ Login Success
- Redirects to dashboard
- Flash message: "Welcome, [Name]!"
- Session created

### ✅ File Upload Success
- File saved to `uploads/` folder with timestamp
- Upload record created in `uploads/uploads.json`
- Flash message: "File uploaded successfully!"

### ✅ Admin Only Routes
- Try to access `/admin/upload` as user → redirect to login
- Try to access `/admin/dashboard` as user → redirect to login
- Only admin can see upload/file management pages

### ✅ Streamlit Integration
- Latest uploaded file automatically loaded
- Data displays in Streamlit dashboard
- All visualization pages work

## Common Issues & Solutions

### Issue: "Address already in use" port 5000
```bash
# Find and kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID [PID] /F
```

### Issue: "No module named 'admin_dashboard_routes'"
```bash
# Make sure admin_dashboard_routes.py exists in same directory as auth_app.py
# Reinstall packages
pip install -r requirements_auth.txt
```

### Issue: Streamlit shows "No data files uploaded yet"
```bash
# Verify file was uploaded to uploads/ folder
# Check uploads/uploads.json exists
# Try uploading file again from admin panel
```

### Issue: Database shows old data after delete
```bash
# Delete auth_system.db
rm auth_system.db
# Restart Flask app (it will recreate database)
python auth_app.py
```

## Performance Testing

### Load Testing
1. Register 10+ users
2. Upload multiple large files (10-50 MB)
3. Check app responsiveness

### Security Testing
1. Try SQL injection in login: `admin' OR '1'='1`
   - Expected: Error message, login fails
2. Try accessing admin routes without login
   - Expected: Redirect to login
3. Try uploading non-Excel file
   - Expected: Error message, file rejected

## Browser Compatibility

Tested and compatible with:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Edge 90+
- ✅ Safari 14+

## Performance Metrics

Expected performance:
- Page load: < 1 second
- File upload: < 30 seconds (for 50 MB file)
- Dashboard render: < 2 seconds
- Streamlit load: < 5 seconds

## Next Steps After Testing

1. ✅ Backup the auth_system.db file
2. ✅ Change default admin password
3. ✅ Customize dashboard colors/branding
4. ✅ Deploy to production
5. ✅ Set up email notifications (optional)
6. ✅ Enable HTTPS

## Testing Logs

Record your test results:

```
Date: ____________
Tester: ____________

Test Phase 1: ______ (Pass/Fail)
Test Phase 2: ______ (Pass/Fail)
Test Phase 3: ______ (Pass/Fail)
Test Phase 4: ______ (Pass/Fail)
Test Phase 5: ______ (Pass/Fail)
Test Phase 6: ______ (Pass/Fail)

Issues Found:
1. _________________________________
2. _________________________________
3. _________________________________

Notes:
_____________________________________
_____________________________________
```

---

Good luck with testing! 🚀

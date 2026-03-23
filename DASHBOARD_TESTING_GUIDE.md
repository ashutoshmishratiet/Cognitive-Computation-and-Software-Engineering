# Full-Stack Dashboard Testing Guide

## 🎯 Overview
This guide provides step-by-step instructions to test the complete Cognitive Performance Analytics Dashboard with all 3 sections, visualizations, and interactive features.

---

## ✅ System Architecture

### Backend (Flask/Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Data Processing**: Pandas & NumPy for normalization and calculations
- **API Routes**: RESTful endpoints for dashboard data
- **Authentication**: Admin & User roles with session management

### Frontend (HTML/CSS/JavaScript)
- **Framework**: Bootstrap 5.3.0
- **Charts**: Chart.js 4.4.0
- **Tables**: DataTables.js 1.13.7 with export functionality
- **Styling**: Professional light theme with #2563eb primary color

### Data Features
- **50+ Student Sample Data** pre-generated in Excel format
- **Normalized Metrics**: Understanding, Debugging, Completion, Cognitive Load
- **Cognitive Load Categories**: Low (<20%), Medium (20-50%), High (>50%)
- **Color-Coded Display**: Green (High), Orange (Medium), Red (Low)

---

## 🚀 Quick Start

### 1. **Verify Flask App is Running**
```
Terminal Output Shows:
✓ Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

### 2. **Test Accounts**
| Role | Username | Password |
|------|----------|----------|
| Admin | `admin` | `admin@2024` |
| User | `user` | `user@2024` |

---

## 📋 Testing Workflows

### **WORKFLOW 1: Admin Data Upload**

#### Step 1: Login as Admin
1. Go to `http://localhost:5000`
2. Click **"Admin Login"** (if on login page)
3. Enter: `admin` / `admin@2024`
4. Verify: Redirected to **Admin Dashboard**

#### Step 2: Upload Sample Data
1. Click **"Upload"** tab in admin dashboard
2. Click **"Choose File"** button
3. Navigate to: `uploads/Sample_Cognitive_Data.xlsx`
4. Select file and click **"Upload"**
5. Verify: 
   - File appears in **Data Manager**
   - Shows: 50 rows, 28 columns
   - Status: "Active"

#### Step 3: Verify File Metadata
- **File Size**: ~50-100 KB
- **Upload Date**: Current date/time
- **Status**: Active (✓)

Expected Result: ✅ File successfully uploaded and indexed

---

### **WORKFLOW 2: User Dashboard - Overall Analytics**

#### Step 1: Login as User
1. Open new browser tab/window
2. Go to `http://localhost:5000`
3. Click **"User Login"**
4. Enter: `user` / `user@2024`
5. Click **"Analytics Dashboard"** or visit `/user/dashboard-v2`

#### Step 2: Verify Section 1 - Overall Performance
Expected to see **6 metric cards in top row:**

| Metric | Expected Range | Sample Value |
|--------|-----------------|--------------|
| Total Students | 50 | 50 |
| Avg Understanding | 5-8/10 | 6.7/10 |
| Avg Debugging | 5-8/10 | 6.8/10 |
| Avg Completion | 5-8/10 | 6.6/10 |
| Avg Cognitive Load | 30-60% | 46.2% |
| Overall Performance | 6-7/10 | 6.7/10 |

#### Step 3: Verify Chart 1 - Bar Chart (Cognitive Indices)
- **Title**: "Cognitive Indices Comparison"
- **X-axis**: 0-10 (Score scale)
- **Y-axis**: 
  - Code Understanding
  - Debugging
  - Completion
- **Bars**: Should display in blue, teal, green colors
- **Interactivity**: Hover over bars to see exact values

#### Step 4: Verify Chart 2 - Pie Chart (Cognitive Load Distribution)
- **Title**: "Cognitive Load Distribution"
- **Segments**:
  - Low (<20%): Green segment
  - Medium (20-50%): Orange segment
  - High (>50%): Red segment
- **Numbers**: Sum should equal 50 students
- **Legend**: Shows all 3 categories

#### Step 5: Verify Chart 3 - Line Chart (Performance Trends)
- **Title**: "Performance Trends (Top 20 Students by Cognitive Load)"
- **3 Lines**:
  - Understanding (Blue)
  - Debugging (Teal)
  - Completion (Green)
- **X-axis**: Student 1 through Student 20
- **Y-axis**: 0-10 scale
- **Shows**: Top 20 students sorted by cognitive load

Expected Result: ✅ All 3 sections visible with interactive charts

---

### **WORKFLOW 3: Student-Specific Analysis**

#### Step 1: Select Individual Student
1. Scroll to **Section 2** on dashboard
2. Open dropdown: **"Select Student:"**
3. Choose any student (e.g., "STU001")
4. Click **"Load Analysis"** button

#### Step 2: Verify Loading Spinner
- **Expected**: Overlay appears with loading animation
- **Duration**: 1-2 seconds
- **Auto-hides**: Once data loads

#### Step 3: Verify Student Metrics Display
After loading, see **4 metric cards**:

```
┌─────────────────────────────────────┐
│ Understanding Score  │ Debugging Score    │
│      7.3/10          │      6.8/10        │
├─────────────────────────────────────┤
│ Completion Score     │ Overall Performance│
│      7.1/10          │      7.1/10        │
└─────────────────────────────────────┘
```

#### Step 4: Verify Student Bar Chart
- **Title**: "Individual Scores Comparison"
- **Bars**: 3 bars for Understanding, Debugging, Completion
- **Colors**: Blue, Teal, Green
- **Values**: Individual student's scores (0-10)
- **Comparison**: Should show relative performance across 3 indices

#### Step 5: Verify Gauge Chart (Cognitive Load)
- **Title**: "Cognitive Load & Category"
- **Circular Gauge**: Shows colored segment
  - Red: High (>50%)
  - Orange: Medium (20-50%)
  - Green: Low (<20%)
- **Center Text**: Displays percentage and category (e.g., "42.5% Medium Load")
- **Color-Coded**: Segment color matches category

#### Step 6: Test Multiple Students
1. Change dropdown selection to different student
2. Click **"Load Analysis"** again
3. Verify: Charts update with new student's data
4. Verify: No errors in console

Expected Result: ✅ Individual student analysis works with dynamic chart updates

---

### **WORKFLOW 4: Data Table & Filtering**

#### Step 1: Scroll to Section 3
Scroll down to **"Complete Data Table"** section

#### Step 2: Verify Table Display
**Table should show:**
- **Columns**: Student ID, Understanding, Debugging, Completion, Cognitive Load, Category, Overall Performance
- **Rows**: First 10 students (default pagination)
- **Total**: Show "Showing 1 to 10 of 50 entries"

#### Step 3: Verify Color-Coding
Cognitive Load column should show:
```
< 20%: RED background text
20-50%: ORANGE background text
> 50%: GREEN background text
```

Example:
```
STU001: 15.2% (RED)
STU002: 35.4% (ORANGE)
STU003: 72.1% (GREEN)
```

#### Step 4: Test Sorting
1. **Click** "Cognitive Load" column header
2. **Verify**: Table sorts by lowest to highest
3. **Click** again: Reverse sort (highest to lowest)
4. **Verify**: Rows reorder correctly

#### Step 5: Test Pagination
1. Click **"Next"** button at bottom of table
2. **Verify**: Shows students 11-20
3. Click **"Last"** button
4. **Verify**: Shows students 41-50 (or last page)
5. Click page number (e.g., "3")
6. **Verify**: Jumps to that page

#### Step 6: Test Search
1. Find **search box** (usually top-right of table)
2. Type **"STU010"**
3. **Verify**: Table filters to show only STU010
4. Clear search box
5. **Verify**: All 50 students appear again

#### Step 7: Test Export Button
1. Click **"Export to CSV"** button
2. **Verify**: 
   - Browser downloads `cognitive_data_[timestamp].csv`
   - File contains appropriate data
   - File is CSV format (can open in Excel)

Expected Result: ✅ Table fully functional with sorting, pagination, search, and export

---

### **WORKFLOW 5: Filter Dropdown (Optional Feature)**

#### Step 1: Locate Filter
Find **"Filter:"** dropdown in Section 3

#### Step 2: Test Filter Options
1. **Default**: "All Cognitive Loads" - shows 50 entries
2. **Select**: "Low (<20%)" - shows only low load students
3. **Verify**: Count decreases (e.g., 8 students)
4. **Select**: "Medium (20-50%)" - shows medium load
5. **Select**: "High (>50%)" - shows high load
6. **Select**: "All Cognitive Loads" - back to 50

Expected Result: ✅ Filter correctly reduces table rows

---

### **WORKFLOW 6: Responsive Design Testing**

#### Test on Different Screen Sizes
1. **Desktop** (1920x1080):
   - All sections visible side-by-side
   - 3 charts display properly
   - Table has full columns

2. **Tablet** (768x1024):
   - Sections stack vertically
   - Charts adjust height
   - Table horizontal scroll works

3. **Mobile** (375x667):
   - Metrics stack in single column
   - Charts stack vertically
   - Table is horizontal-scrollable

#### Verification Points:
- No content cut off
- Buttons clickable
- Dropdowns functional
- Charts responsive

Expected Result: ✅ Responsive on all devices

---

## 🧪 Data Validation Tests

### **Test 1: Data Normalization**
1. Open browser DevTools (F12)
2. Go to **Console** tab
3. Verify no JavaScript errors
4. Check:
   - Understanding Score = (U_C*2 + U_W) / (U_C + U_W + U_NA) * 10
   - Debugging Score = (D_C*2 + D_W) / (D_C + D_W + D_NA) * 10
   - Completion Score = (C_C*2 + C_W) / (C_C + C_W + C_NA) * 10
   - Cognitive Load = (CL1 + CL2) / 2, normalized to 0-100

### **Test 2: Calculation Verification**
1. Pick a student (e.g., STU001)
2. Manually calculate expected values
3. Compare with dashboard display
4. Verify within 0.1 variance (rounding)

### **Test 3: API Response Validation**
1. Open DevTools Network tab
2. Refresh dashboard
3. Verify API calls:
   - ✅ `/api/dashboard/overall-stats` → 200 OK
   - ✅ `/api/dashboard/chart-data` → 200 OK
   - ✅ `/api/dashboard/table-data` → 200 OK
4. Check response times < 500ms

---

## ⚠️ Error Handling Tests

### **Test 1: Missing Data File**
1. Delete uploaded file from `uploads/` directory
2. Refresh dashboard
3. **Expected**: Error message displayed gracefully
4. **Verify**: No application crash

### **Test 2: Invalid File Format**
1. Upload `.txt` or `.pdf` file
2. **Expected**: Error message: "Unsupported file format"
3. **Verify**: Admin dashboard doesn't crash

### **Test 3: Corrupted Data**
1. Upload file with missing columns
2. **Expected**: Graceful error handling
3. **Verify**: Clear error message to user

### **Test 4: Network Error**
1. Open DevTools
2. Toggle offline mode
3. Try to load student data
4. **Expected**: Error notification shown
5. **Verify**: Not a JavaScript error, proper error message

---

## 📊 Performance Benchmarks

| Operation | Expected Time |
|-----------|-----|
| Dashboard load (first time) | < 2 seconds |
| Student data load | < 500ms |
| Chart render | < 1 second |
| Table sort | < 300ms |
| Export to CSV | < 1 second |

---

## 🎉 Final Verification Checklist

- [ ] **Admin** can login and upload data file
- [ ] **User** can access analytics dashboard
- [ ] **Section 1** shows all 6 metrics and 3 charts
- [ ] **Section 2** allows student selection with up-to-date charts
- [ ] **Section 3** displays 50-student table with all features
- [ ] **Color-coding** works: Red/Orange/Green for cognitive load
- [ ] **Charts** are interactive and update dynamically
- [ ] **Export** button downloads CSV file
- [ ] **Pagination** works correctly
- [ ] **Search** filters table accurately
- [ ] **Sorting** works on all columns
- [ ] **Loading spinner** appears and disappears
- [ ] **Responsive design** works on mobile/tablet/desktop
- [ ] **No console errors** when performing any action
- [ ] **API responses** are under 500ms

---

## 🔧 Troubleshooting

### Issue: Charts not displaying
**Solution**: 
1. Verify Chart.js loaded: Open DevTools → Sources → search "chart.js"
2. Check console for errors: F12 → Console tab
3. Reload page: Ctrl+Shift+R (hard refresh)

### Issue: Table showing no data
**Solution**:
1. Verify file was uploaded: Check Admin Data Manager
2. Check API response: DevTools → Network → `/api/dashboard/table-data`
3. Look for 404 errors

### Issue: Student selector dropdown empty
**Solution**:
1. Verify data file has "Student ID" column
2. Check uploaded file in Data Manager
3. Ensure normalization ran successfully

### Issue: CSV export not working
**Solution**:
1. Check browser console for errors
2. Verify write permissions on server
3. Try different browser

---

## 🎓 Sample Data Details

**File**: `uploads/Sample_Cognitive_Data.xlsx`
- **Students**: 50 (STU001 to STU050)
- **Records**: One row per student
- **Columns**: 28 total

**Column Groups**:
1. Student Info: ID, Name
2. Understanding Index: U_C, U_W, U_NA
3. Debugging Index: D_C, D_W, D_NA
4. Completion Index: C_C, C_W, C_NA
5. Cognitive Load: CL1, CL2
6. Emotion: Emotion_Value_Scaled
7. Problem Performance: P1-P7 Before/After (14 columns)

---

## 📞 Support

For issues or questions:
1. Check browser console (F12)
2. Review Flask app terminal output
3. Verify all dependencies installed
4. Check database: `instance/cogn_system.db`

---

## ✨ Features Implemented

✅ **Admin Upload Section**
- File upload (CSV/Excel)
- Data validation
- Metadata tracking

✅ **User Dashboard - Section 1: Overall Graphs**
- 6 metric cards (statistics)
- Bar chart (cognitive indices comparison)
- Pie chart (cognitive load distribution)
- Line chart (performance trends)

✅ **User Dashboard - Section 2: Student-Specific View**
- Dropdown student selector
- 4 individual metric cards
- Bar chart (individual scores)
- Gauge chart (cognitive load with color coding)

✅ **User Dashboard - Section 3: Data Table**
- Full student data table
- Column sorting (ascending/descending)
- Pagination (10 rows per page)
- Search functionality
- Color-coded cognitive load cells
- CSV export button
- Responsive design

✅ **Technical Features**
- Loading spinners with animations
- Mobile-responsive layout
- Real-time chart updates
- Data normalization (scores 0-10)
- Cognitive load categorization
- Professional light-theme UI
- Error handling and validation

---

**Last Updated**: February 10, 2026
**Version**: 1.0 Complete
**Status**: ✅ Ready for Production Testing

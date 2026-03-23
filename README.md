# Cognitive Computation and Software Engineering

A comprehensive web application for cognitive data analysis and management with EEG data processing capabilities. This system provides tools for administrators to manage users, upload and analyze cognitive data, and for regular users to view their analysis results.

## Features

- **User Management**: Admin interface for creating and managing user accounts
- **EEG Data Analysis**: Upload and analyze EEG data with multiple analysis methodologies
- **Multi-Analysis Support**: 
  - Technical analysis
  - Paper-compliant analysis
  - Normalized analysis
  - Comprehensive metrics
- **Dashboard**: Real-time analytics and visualization for both admins and users
- **Data Management**: Bulk upload and processing capabilities
- **Calculation Tools**: Advanced calculators for cognitive metrics
- **User Authentication**: Secure login and registration system

## Technology Stack

- **Backend**: Python with Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite
- **Data Processing**: Pandas, NumPy
- **File Handling**: Excel file support (.xlsx)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # On Windows PowerShell
   source .venv/bin/activate   # On macOS/Linux
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database:**
   The database will be created automatically on first run. Administrator account can be set up through the web interface.

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

                # Testing and verification scripts
```

## Usage

### Admin Features

1. **User Management**: Create and manage user accounts
2. **Data Upload**: Upload EEG data files in Excel format
3. **Analysis Tools**: Run various analyses on uploaded data
4. **Dashboard**: Monitor system activity and analytics
5. **Configuration**: Manage system settings and parameters

### User Features

1. **Profile**: View and manage personal information
2. **View Analysis**: Review analysis results and reports
3. **Dashboard**: Personal analytics overview
4. **Data Viewing**: Access EEG data information

## Configuration

Key configuration parameters can be adjusted in `app.py`:
- Database location
- Upload folder path
- Session timeout
- Analysis parameters

## Testing

Run the test files to verify system functionality:

```bash
python test_routes.py              # Test API routes
python test_technical_metrics.py   # Test technical analysis
python test_paper_analyzer.py      # Test paper-compliant analysis
python test_comprehensive_metrics.py # Test comprehensive metrics
```

## File Formats

### Supported Data Format
- Excel files (.xlsx) with the following structure:
  - Headers in first row
  - Numeric data for analysis
  - Subject/participant ID column
  - Timestamp or session information

## Security Considerations

- User passwords are securely hashed
- Session management with timeouts
- Admin-restricted areas require authentication
- File uploads are validated and stored securely

## Database

The application uses SQLite for data persistence. The database includes tables for:
- Users and authentication
- Analysis results
- Upload history
- System logs

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py` or stop the service using port 5000
2. **Database errors**: Delete `instance/cogn_system.db` to reset (creates new on next run)
3. **Import errors**: Ensure all requirements are installed with `pip install -r requirements.txt`

## Contributing

This project was created as an academic exercise in cognitive computation and software engineering.

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions, refer to the technical documentation in the project or contact your instructor.

---

**Version**: 1.0  
**Last Updated**: March 2026

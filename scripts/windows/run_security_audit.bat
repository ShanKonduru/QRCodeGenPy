@echo off
REM Security Audit Script for QR Code Generator Project
REM This script runs comprehensive security audits using safety, bandit, and pip-audit

echo ================================================================
echo 🔐 QR Code Generator - Security Audit Runner (Windows)
echo ================================================================
echo.

REM Check if virtual environment exists
if not exist ".venv\" (
    echo ❌ Virtual environment not found. Please run setup_env.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Failed to activate virtual environment
    pause
    exit /b 1
)

REM Install security audit tools if not already installed
echo 🔄 Ensuring security audit tools are installed...
pip install safety bandit pip-audit --quiet

REM Create security reports directory
if not exist "security_reports\" mkdir security_reports

echo.
echo 🚀 Starting Security Audit...
echo.

REM Run the security audit script
python run_security_audit.py --tool all

REM Check if audit found issues
if errorlevel 1 (
    echo.
    echo ⚠️ Security audit completed with issues found.
    echo 📁 Check security_reports\ folder for detailed reports.
    echo.
) else (
    echo.
    echo ✅ Security audit completed successfully - no issues found!
    echo 📁 Reports saved in security_reports\ folder.
    echo.
)

echo 📋 Security audit complete!
echo.
echo Available reports:
if exist "security_reports\bandit_report.txt" echo   - security_reports\bandit_report.txt
if exist "security_reports\bandit_report.json" echo   - security_reports\bandit_report.json  
if exist "security_reports\pip_audit_report.json" echo   - security_reports\pip_audit_report.json
if exist "security_reports\security_summary.md" echo   - security_reports\security_summary.md

echo.
echo Press any key to exit...
pause > nul
@echo off
echo ========================================
echo     QR Code Generator - Coverage Report
echo ========================================
echo.

if not exist ".venv" (
    echo Error: Virtual environment not found!
    echo Please run 'setup_env.bat' first.
    pause
    exit /b 1
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Running tests with coverage report...
python run_tests.py --html-cov --verbose

echo.
echo Coverage report generated!
echo Check 'htmlcov/index.html' for detailed coverage report.
echo.
pause
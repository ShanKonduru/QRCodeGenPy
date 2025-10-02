@echo off
echo ========================================
echo     QR Code Generator - Unit Tests
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
echo Running unit tests...
python run_tests.py --coverage --verbose

echo.
pause
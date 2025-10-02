@echo off
echo ========================================
echo     QR Code Generator - Main Application
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
echo Running QR Code Generator...
python QRCodeGenerator.py

echo.
pause
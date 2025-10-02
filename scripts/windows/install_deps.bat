@echo off
echo ========================================
echo   QR Code Generator - Install Dependencies
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
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Dependencies installed successfully!
echo.
pause
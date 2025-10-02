@echo off
echo ========================================
echo     QR Code Generator - Streamlit UI
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
echo Starting Streamlit web application...
echo.
echo The application will open in your default browser.
echo Press Ctrl+C to stop the server.
echo.
streamlit run streamlit_app.py

pause
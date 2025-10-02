@echo off
echo ========================================
echo   QR Code Generator - Activate Environment
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
echo Virtual environment activated!
echo You can now run:
echo - install_deps.bat (to install dependencies)
echo - run_main.bat (to run the main application)
echo - run_tests.bat (to run unit tests)
echo - run_streamlit.bat (to run the web UI)
echo.

cmd /k
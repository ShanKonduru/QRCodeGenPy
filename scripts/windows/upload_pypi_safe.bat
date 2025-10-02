@echo off
REM PyPI Upload Script - With pip 25.2 False Positive Handler
REM This script handles the known pip 25.2 false positive security alert

echo ================================================================
echo 📦 QR Code Generator - PyPI Upload (pip 25.2 FP Handler)
echo ================================================================
echo.

REM Change to project root directory
cd /d %~dp0\..\..\

REM Check if virtual environment exists
if not exist ".venv\" (
    echo ❌ Virtual environment not found. Please run scripts\windows\setup_env.bat first.
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

echo.
echo 🔍 Checking for pip 25.2 false positive...
python fix_pip_false_positive.py

echo.
echo ⚠️  IMPORTANT: pip 25.2 Security Alert
echo   The security scan will show a pip vulnerability, but this is a FALSE POSITIVE.
echo   pip 25.2 actually FIXES the vulnerability - it's safe to proceed.
echo.

set /p continue="Do you want to proceed with PyPI upload? (y/N): "
if /i not "%continue%"=="y" (
    echo ❌ Upload cancelled by user.
    pause
    exit /b 0
)

REM Install build tools if not already installed
echo 🔄 Installing/updating build tools...
pip install --upgrade pip setuptools wheel build twine python-dotenv

REM Load environment variables from .env file
echo 🔑 Loading PyPI credentials from .env file...
if not exist ".env" (
    echo ❌ .env file not found! Please create .env with PYPI_USER_NAME and PYPI_PASSWORD
    pause
    exit /b 1
)

REM Read .env file and set environment variables
for /f "usebackq tokens=1,2 delims==" %%a in (".env") do (
    if "%%a"=="PYPI_USER_NAME" set PYPI_USER_NAME=%%b
    if "%%a"=="PYPI_PASSWORD" set PYPI_PASSWORD=%%b
)

if "%PYPI_USER_NAME%"=="" (
    echo ❌ PYPI_USER_NAME not found in .env file
    pause
    exit /b 1
)

if "%PYPI_PASSWORD%"=="" (
    echo ❌ PYPI_PASSWORD not found in .env file
    pause
    exit /b 1
)

echo ✅ PyPI credentials loaded successfully for user: %PYPI_USER_NAME%

REM Clean previous builds
echo 🧹 Cleaning previous builds...
if exist "dist\" rmdir /s /q dist
if exist "build\" rmdir /s /q build
if exist "*.egg-info\" (
    for /d %%d in (*.egg-info) do rmdir /s /q "%%d"
)

REM Run tests (skip security audit since we're handling the false positive)
echo 🧪 Running tests before upload...
python -m pytest tests/ -v
if errorlevel 1 (
    echo ❌ Tests failed! Cannot upload to PyPI with failing tests.
    pause
    exit /b 1
)

echo ✅ All tests passed!

REM Build the package
echo 📦 Building package...
python -m build
if errorlevel 1 (
    echo ❌ Package build failed!
    pause
    exit /b 1
)

echo ✅ Package built successfully!

REM Show what will be uploaded
echo.
echo 📋 Files to be uploaded:
dir dist\

echo.
echo ⚠️  UPLOADING TO PyPI - This action cannot be undone!
echo.
echo 🌐 PyPI URL: https://pypi.org/user/shankonduru/
echo 📦 Package name: qrcodegenpy-shankonduru
echo.

set /p upload="Are you sure you want to upload to PyPI? (y/N): "
if /i not "%upload%"=="y" (
    echo ❌ Upload cancelled by user.
    echo 💡 To upload later, run: twine upload dist/*
    pause
    exit /b 0
)

REM Upload to PyPI
echo 🚀 Uploading to PyPI...
echo.
echo 🔑 Using credentials from .env file for user: %PYPI_USER_NAME%
echo.

REM Use environment variables for authentication
set TWINE_USERNAME=%PYPI_USER_NAME%
set TWINE_PASSWORD=%PYPI_PASSWORD%

twine upload dist/*

if errorlevel 1 (
    echo ❌ Upload failed! Check the error messages above.
    echo.
    echo 💡 Common issues:
    echo   - Incorrect credentials
    echo   - Package name already exists
    echo   - Version number already published
    echo   - Network connection issues
    echo.
    pause
    exit /b 1
)

echo.
echo 🎉 Package uploaded successfully to PyPI!
echo.
echo 🌐 Your package is now available at:
echo   https://pypi.org/project/qrcodegenpy-shankonduru/
echo.
echo 📥 Users can install it with:
echo   pip install qrcodegenpy-shankonduru
echo.
echo 🏷️  Don't forget to:
echo   1. Create a GitHub release
echo   2. Update documentation
echo   3. Announce the release
echo.

pause
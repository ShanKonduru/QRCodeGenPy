@echo off
REM PyPI Upload Script for QR Code Generator Project
REM This script builds and uploads the package to PyPI

echo ================================================================
echo 📦 QR Code Generator - PyPI Upload Script (Windows)
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
    if "%%a"=="PYPI_API_TOKEN" set PYPI_API_TOKEN=%%b
)

if "%PYPI_API_TOKEN%"=="" (
    echo ❌ PYPI_API_TOKEN not found in .env file
    echo 💡 Please create an API token at https://pypi.org/manage/account/token/
    echo    and add it to .env as: PYPI_API_TOKEN=your_token_here
    pause
    exit /b 1
)

echo ✅ PyPI API token loaded successfully

echo.
echo ⚠️  IMPORTANT: Make sure you have:
echo   1. Updated version number in pyproject.toml and setup.py
echo   2. Updated CHANGELOG or release notes
echo   3. Committed all changes to git
echo   4. Tagged the release (git tag v1.0.0)
echo.

set /p continue="Do you want to continue? (y/N): "
if /i not "%continue%"=="y" (
    echo ❌ Upload cancelled by user.
    pause
    exit /b 0
)

REM Clean previous builds
echo 🧹 Cleaning previous builds...
if exist "dist\" rmdir /s /q dist
if exist "build\" rmdir /s /q build
if exist "*.egg-info\" (
    for /d %%d in (*.egg-info) do rmdir /s /q "%%d"
)

REM Run security audit first
echo 🔐 Running security audit before upload...
python run_security_audit.py --tool all
if errorlevel 1 (
    echo.
    echo ⚠️ Security issues found! Please review before uploading to PyPI.
    echo 📁 Check security_reports\ folder for details.
    echo.
    set /p ignore="Do you want to continue despite security issues? (y/N): "
    if /i not "%ignore%"=="y" (
        echo ❌ Upload cancelled due to security concerns.
        pause
        exit /b 1
    )
)

REM Run tests
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
echo 🔑 Using API token authentication
echo.

REM Use API token for authentication (PyPI recommended method)
set TWINE_USERNAME=__token__
set TWINE_PASSWORD=%PYPI_API_TOKEN%

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
#!/bin/bash

# PyPI Upload Script for QR Code Generator Project
# This script builds and uploads the package to PyPI

set -e  # Exit on any error

echo "================================================================"
echo "📦 QR Code Generator - PyPI Upload Script (Unix/Linux/Mac)"
echo "================================================================"
echo

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found. Please run setup_env.sh first."
    exit 1
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

# Install build tools if not already installed
echo "🔄 Installing/updating build tools..."
pip install --upgrade pip setuptools wheel build twine python-dotenv

# Load environment variables from .env file
echo "🔑 Loading PyPI credentials from .env file..."
if [ ! -f ".env" ]; then
    echo "❌ .env file not found! Please create .env with PYPI_USER_NAME and PYPI_PASSWORD"
    exit 1
fi

# Source the .env file
export $(grep -v '^#' .env | xargs)

if [ -z "$PYPI_USER_NAME" ]; then
    echo "❌ PYPI_USER_NAME not found in .env file"
    exit 1
fi

if [ -z "$PYPI_PASSWORD" ]; then
    echo "❌ PYPI_PASSWORD not found in .env file"
    exit 1
fi

echo "✅ PyPI credentials loaded successfully for user: $PYPI_USER_NAME"

echo
echo "⚠️  IMPORTANT: Make sure you have:"
echo "  1. Updated version number in pyproject.toml and setup.py"
echo "  2. Updated CHANGELOG or release notes"
echo "  3. Committed all changes to git"
echo "  4. Tagged the release (git tag v1.0.0)"
echo

read -p "Do you want to continue? (y/N): " continue
if [[ ! "$continue" =~ ^[Yy]$ ]]; then
    echo "❌ Upload cancelled by user."
    exit 0
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info/

# Run security audit first
echo "🔐 Running security audit before upload..."
if ! python run_security_audit.py --tool all; then
    echo
    echo "⚠️ Security issues found! Please review before uploading to PyPI."
    echo "📁 Check security_reports/ folder for details."
    echo
    read -p "Do you want to continue despite security issues? (y/N): " ignore
    if [[ ! "$ignore" =~ ^[Yy]$ ]]; then
        echo "❌ Upload cancelled due to security concerns."
        exit 1
    fi
fi

# Run tests
echo "🧪 Running tests before upload..."
if ! python -m pytest tests/ -v; then
    echo "❌ Tests failed! Cannot upload to PyPI with failing tests."
    exit 1
fi

echo "✅ All tests passed!"

# Build the package
echo "📦 Building package..."
if ! python -m build; then
    echo "❌ Package build failed!"
    exit 1
fi

echo "✅ Package built successfully!"

# Show what will be uploaded
echo
echo "📋 Files to be uploaded:"
ls -la dist/

echo
echo "⚠️  UPLOADING TO PyPI - This action cannot be undone!"
echo
echo "🌐 PyPI URL: https://pypi.org/user/shankonduru/"
echo "📦 Package name: qrcodegenpy-shankonduru"
echo

read -p "Are you sure you want to upload to PyPI? (y/N): " upload
if [[ ! "$upload" =~ ^[Yy]$ ]]; then
    echo "❌ Upload cancelled by user."
    echo "💡 To upload later, run: twine upload dist/*"
    exit 0
fi

# Upload to PyPI
echo "🚀 Uploading to PyPI..."
echo
echo "🔑 Using credentials from .env file for user: $PYPI_USER_NAME"
echo

# Use environment variables for authentication
export TWINE_USERNAME="$PYPI_USER_NAME"
export TWINE_PASSWORD="$PYPI_PASSWORD"

if twine upload dist/*; then
    echo
    echo "🎉 Package uploaded successfully to PyPI!"
    echo
    echo "🌐 Your package is now available at:"
    echo "  https://pypi.org/project/qrcodegenpy-shankonduru/"
    echo
    echo "📥 Users can install it with:"
    echo "  pip install qrcodegenpy-shankonduru"
    echo
    echo "🏷️  Don't forget to:"
    echo "  1. Create a GitHub release"
    echo "  2. Update documentation"
    echo "  3. Announce the release"
    echo
else
    echo "❌ Upload failed! Check the error messages above."
    echo
    echo "💡 Common issues:"
    echo "  - Incorrect credentials"
    echo "  - Package name already exists"
    echo "  - Version number already published"
    echo "  - Network connection issues"
    echo
    exit 1
fi

echo "🔒 PyPI upload process finished."
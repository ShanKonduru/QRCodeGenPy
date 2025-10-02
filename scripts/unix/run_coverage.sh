#!/bin/bash

echo "========================================"
echo "     QR Code Generator - Coverage Report"
echo "========================================"
echo

if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not found!"
    echo "Please run './setup_env.sh' first."
    read -p "Press Enter to continue..."
    exit 1
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo
echo "Running tests with coverage report..."
python run_tests.py --html-cov --verbose

echo
echo "Coverage report generated!"
echo "Check 'htmlcov/index.html' for detailed coverage report."
echo
read -p "Press Enter to continue..."
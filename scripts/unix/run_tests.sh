#!/bin/bash

echo "========================================"
echo "     QR Code Generator - Unit Tests"
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
echo "Running unit tests..."
python run_tests.py --coverage --verbose

echo
read -p "Press Enter to continue..."
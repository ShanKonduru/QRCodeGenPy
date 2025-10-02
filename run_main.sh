#!/bin/bash

echo "========================================"
echo "     QR Code Generator - Main Application"
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
echo "Running QR Code Generator..."
python QRCodeGenerator.py

echo
read -p "Press Enter to continue..."
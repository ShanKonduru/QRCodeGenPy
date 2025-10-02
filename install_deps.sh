#!/bin/bash

echo "========================================"
echo "   QR Code Generator - Install Dependencies"
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
echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo
echo "Dependencies installed successfully!"
echo
read -p "Press Enter to continue..."
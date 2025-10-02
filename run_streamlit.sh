#!/bin/bash

echo "========================================"
echo "     QR Code Generator - Streamlit UI"
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
echo "Starting Streamlit web application..."
echo
echo "The application will open in your default browser."
echo "Press Ctrl+C to stop the server."
echo
streamlit run streamlit_app.py
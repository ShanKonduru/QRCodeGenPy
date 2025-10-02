#!/bin/bash

echo "========================================"
echo "   QR Code Generator - Activate Environment"
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
echo "Virtual environment activated!"
echo "You can now run:"
echo "- ./install_deps.sh (to install dependencies)"
echo "- ./run_main.sh (to run the main application)"
echo "- ./run_tests.sh (to run unit tests)"
echo "- ./run_streamlit.sh (to run the web UI)"
echo

exec bash
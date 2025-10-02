#!/bin/bash

echo "========================================"
echo "     QR Code Generator - Setup"
echo "========================================"
echo

echo "Creating virtual environment..."
python3 -m venv .venv

echo
echo "Virtual environment created successfully!"
echo
echo "Next steps:"
echo "1. Run './activate.sh' to activate the environment"
echo "2. Run './install_deps.sh' to install dependencies"
echo
read -p "Press Enter to continue..."
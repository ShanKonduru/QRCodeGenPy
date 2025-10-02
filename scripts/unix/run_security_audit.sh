#!/bin/bash

# Security Audit Script for QR Code Generator Project
# This script runs comprehensive security audits using safety, bandit, and pip-audit

set -e  # Exit on any error

echo "================================================================"
echo "🔐 QR Code Generator - Security Audit Runner (Unix/Linux/Mac)"
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

# Install security audit tools if not already installed
echo "🔄 Ensuring security audit tools are installed..."
pip install safety bandit pip-audit --quiet

# Create security reports directory
mkdir -p security_reports

echo
echo "🚀 Starting Security Audit..."
echo

# Run the security audit script
if python run_security_audit.py --tool all; then
    echo
    echo "✅ Security audit completed successfully - no critical issues found!"
    echo "📁 Reports saved in security_reports/ folder."
    echo
else
    echo
    echo "⚠️ Security audit completed with issues found."
    echo "📁 Check security_reports/ folder for detailed reports."
    echo
fi

echo "📋 Security audit complete!"
echo
echo "Available reports:"
[ -f "security_reports/bandit_report.txt" ] && echo "  - security_reports/bandit_report.txt"
[ -f "security_reports/bandit_report.json" ] && echo "  - security_reports/bandit_report.json"
[ -f "security_reports/pip_audit_report.json" ] && echo "  - security_reports/pip_audit_report.json"
[ -f "security_reports/security_summary.md" ] && echo "  - security_reports/security_summary.md"

echo
echo "📚 To view reports:"
echo "  - Text report: cat security_reports/bandit_report.txt"
echo "  - Summary: cat security_reports/security_summary.md"
echo "  - JSON reports: Use any JSON viewer or text editor"

echo
echo "🔒 Security audit runner finished."
#!/usr/bin/env python3
"""
Test runner script for QRCodeGenerator project.

This script provides various options for running tests:
- Run all tests
- Run specific test modules
- Generate coverage reports
- Run tests with different verbosity levels
"""

import sys
import subprocess
import argparse
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}")
    print("=" * 50)
    
    try:
        result = subprocess.run(command, shell=True, check=True)
        print(f"✅ {description} completed successfully!")
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed with exit code {e.returncode}")
        return False


def main():
    """Main function to handle command line arguments and run tests."""
    parser = argparse.ArgumentParser(description="Test runner for QRCodeGenerator")
    parser.add_argument(
        "--coverage", 
        action="store_true", 
        help="Run tests with coverage report"
    )
    parser.add_argument(
        "--html-cov", 
        action="store_true", 
        help="Generate HTML coverage report"
    )
    parser.add_argument(
        "--html-report", 
        action="store_true", 
        help="Generate HTML test report"
    )
    parser.add_argument(
        "--verbose", "-v", 
        action="store_true", 
        help="Run tests in verbose mode"
    )
    parser.add_argument(
        "--unit-only", 
        action="store_true", 
        help="Run only unit tests (not integration tests)"
    )
    parser.add_argument(
        "--integration-only", 
        action="store_true", 
        help="Run only integration tests"
    )
    parser.add_argument(
        "--fast", 
        action="store_true", 
        help="Run tests quickly (skip slow tests)"
    )
    
    args = parser.parse_args()
    
    # Get the Python executable path
    python_path = Path(sys.executable)
    
    # Base pytest command
    base_cmd = f'"{python_path}" -m pytest'
    
    # Add verbosity
    if args.verbose:
        base_cmd += " -v"
    
    # Add coverage options
    if args.coverage or args.html_cov:
        base_cmd += " --cov=QRCodeGenerator --cov-report=term-missing"
        if args.html_cov:
            base_cmd += " --cov-report=html:htmlcov"
    
    # Add HTML report option
    if args.html_report:
        base_cmd += " --html=reports/report.html --self-contained-html"
    
    # Add test selection
    if args.unit_only:
        test_path = "tests/test_qr_code_generator.py"
    elif args.integration_only:
        test_path = "tests/test_main_function.py"
    else:
        test_path = "tests/"
    
    # Add speed options
    if args.fast:
        base_cmd += ' -m "not slow"'
    
    # Final command
    cmd = f"{base_cmd} {test_path}"
    
    print("🧪 QR Code Generator Test Runner")
    print("=" * 40)
    print(f"Running command: {cmd}")
    
    success = run_command(cmd, "Running tests")
    
    if args.html_cov and success:
        print(f"\n📊 HTML coverage report generated in: htmlcov/index.html")
    
    if args.html_report and success:
        print(f"\n📋 HTML test report generated in: reports/report.html")
    
    if success:
        print("\n🎉 All tests completed successfully!")
        return 0
    else:
        print("\n💥 Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
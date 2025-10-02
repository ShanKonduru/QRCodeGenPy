#!/usr/bin/env python3
"""
Setup script for QR Code Generator Python package.
This provides additional compatibility for PyPI publishing.
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="qrcodegenpy-shankonduru",
    version="1.0.0",
    author="Shan Konduru",
    author_email="shankonduru@gmail.com",
    description="A comprehensive QR Code Generator library with CLI, Streamlit UI, and robust testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shankonduru/qrcodegenpy",
    project_urls={
        "Bug Tracker": "https://github.com/shankonduru/qrcodegenpy/issues",
        "Documentation": "https://github.com/shankonduru/qrcodegenpy/blob/main/README.md",
        "Source Code": "https://github.com/shankonduru/qrcodegenpy",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Utilities",
    ],
    py_modules=["QRCodeGenerator"],
    python_requires=">=3.12",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0", 
            "pytest-html>=4.1.1",
            "safety>=3.0.0",
            "bandit>=1.7.5",
            "pip-audit>=2.6.0",
            "build>=1.0.0",
            "twine>=4.0.0",
            "python-dotenv>=1.0.0",
        ],
        "ui": ["streamlit>=1.30.0"],
    },
    entry_points={
        "console_scripts": [
            "qrcode-gen=QRCodeGenerator:main",
        ],
    },
    keywords=["qr-code", "qr-generator", "barcode", "python", "cli", "streamlit"],
    include_package_data=True,
    zip_safe=False,
)
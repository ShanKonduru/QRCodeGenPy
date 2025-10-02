# Automation Scripts

This folder contains all automation scripts for the QR Code Generator project, organized by platform.

## Structure

```
scripts/
├── windows/          # Windows batch files (.bat)
├── unix/            # Unix/Linux/Mac shell scripts (.sh)
└── README.md        # This file
```

## Windows Scripts (`scripts/windows/`)

All Windows batch files (`.bat`) for use in Command Prompt or PowerShell:

| Script | Purpose |
|--------|---------|
| `setup_env.bat` | Create and setup virtual environment |
| `activate.bat` | Activate the virtual environment |
| `install_deps.bat` | Install project dependencies |
| `run_main.bat` | Run the main QR code generator |
| `run_tests.bat` | Execute all tests with coverage |
| `run_coverage.bat` | Generate coverage reports |
| `run_streamlit.bat` | Start the Streamlit web interface |
| `run_security_audit.bat` | Run security audits |
| `upload_pypi.bat` | Build and upload package to PyPI |

## Unix Scripts (`scripts/unix/`)

All Unix/Linux/Mac shell scripts (`.sh`) for use in bash or similar shells:

| Script | Purpose |
|--------|---------|
| `setup_env.sh` | Create and setup virtual environment |
| `activate.sh` | Activate the virtual environment |
| `install_deps.sh` | Install project dependencies |
| `run_main.sh` | Run the main QR code generator |
| `run_tests.sh` | Execute all tests with coverage |
| `run_coverage.sh` | Generate coverage reports |
| `run_streamlit.sh` | Start the Streamlit web interface |
| `run_security_audit.sh` | Run security audits |
| `upload_pypi.sh` | Build and upload package to PyPI |

## Usage

### Windows
```cmd
cd scripts\windows
.\setup_env.bat
.\install_deps.bat
.\run_tests.bat
```

### Unix/Linux/Mac
```bash
cd scripts/unix
chmod +x *.sh
./setup_env.sh
./install_deps.sh
./run_tests.sh
```

## Notes

- **Windows scripts** work in both Command Prompt and PowerShell
- **Unix scripts** require execute permissions: `chmod +x *.sh`
- All scripts should be run from the project root directory
- Environment variables are loaded from `.env` file (for PyPI scripts)
- Virtual environment is automatically activated by most scripts

## Cross-Platform Compatibility

Each script has been designed to:
- Handle virtual environment activation correctly
- Provide clear error messages and status updates
- Exit with appropriate error codes
- Include safety checks and confirmations (especially for destructive operations)

## Security

- **PyPI upload scripts** read credentials from `.env` file (not version controlled)
- **Security audit scripts** generate reports in `security_reports/` folder
- All scripts include appropriate error handling and validation
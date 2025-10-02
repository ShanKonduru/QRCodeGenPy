# QR Code Generator in Python

A comprehensive Python application for generating QR codes with both command-line and web interfaces. Features include customizable output directories, multiple content types, comprehensive testing, and a user-friendly Streamlit web UI.

## 🚀 Features

- **Easy to Use**: Simple class-based interface for QR code generation
- **Web Interface**: Modern Streamlit web UI for interactive QR code generation
- **Organized Output**: Automatically saves all QR codes to designated output folders
- **Timestamp Naming**: Automatic file naming with microsecond timestamps to prevent overwrites
- **Customizable Prefix**: Set custom prefixes for generated QR code files
- **Customizable Output Directory**: Choose where to save your QR code files
- **Multiple Content Types**: Support for URLs, text, email, phone, WiFi, vCard, and custom content
- **High Quality**: Optimized settings for clear, scannable QR codes
- **Comprehensive Testing**: 96% test coverage with unit and integration tests
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Professional Setup**: Automated scripts for environment setup and management
```

## 🧪 Testing

Run the built-in example:

```bash
python QRCodeGenerator.py
```

This will create a QR code for the LinkedIn profile URL and save it in the `output` folder.

### 🌐 Streamlit Web Interface

Launch the interactive web interface:

```bash
# Using the provided script (recommended)
streamlit run streamlit_app.py

# Or using batch/shell scripts
./run_streamlit.bat    # Windows
./run_streamlit.sh     # Linux/Mac
```

The web interface provides:
- **Interactive Forms**: Easy-to-use forms for different content types
- **Real-time Preview**: See your QR code generated instantly
- **Download Support**: Direct download of generated QR codes
- **Multiple Content Types**: Support for URLs, text, email, phone, WiFi, vCard
- **Customizable Settings**: Adjust file prefixes and output folders
- **Usage Statistics**: Track QR codes generated in your session

### 🛠️ Quick Setup Scripts

For easy environment management, use the provided scripts:

**Windows (.bat files):**
```bash
setup_env.bat      # Create virtual environment
activate.bat       # Activate environment and open interactive shell
install_deps.bat   # Install all dependencies
run_main.bat       # Run the main CLI application
run_tests.bat      # Run unit tests with coverage
run_coverage.bat   # Generate detailed coverage reports
run_streamlit.bat  # Launch web interface
```

**Linux/Mac (.sh files):**
```bash
./setup_env.sh      # Create virtual environment
./activate.sh       # Activate environment and open interactive shell
./install_deps.sh   # Install all dependencies
./run_main.sh       # Run the main CLI application
./run_tests.sh      # Run unit tests with coverage
./run_coverage.sh   # Generate detailed coverage reports
./run_streamlit.sh  # Launch web interface
```

### Running Unit Tests

The project includes comprehensive unit tests using pytest:

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ -v --cov=QRCodeGenerator --cov-report=term-missing

# Run only unit tests
pytest tests/test_qr_code_generator.py -v

# Run only integration tests
pytest tests/test_main_function.py -v

# Generate HTML coverage report
pytest tests/ --cov=QRCodeGenerator --cov-report=html:htmlcov
```

### Using the Test Runner

You can also use the included test runner script:

```bash
# Run all tests with coverage
python run_tests.py --coverage

# Run tests with HTML coverage report
python run_tests.py --html-cov

# Run only unit tests
python run_tests.py --unit-only --verbose

# Run tests quickly (skip slow tests)
python run_tests.py --fast
```

### Test Coverage

The project maintains high test coverage:

- **Unit Tests**: Test individual components and methods
- **Integration Tests**: Test complete workflows and main function
- **Edge Cases**: Test error conditions and boundary cases
- **Parametrized Tests**: Test multiple scenarios efficiently

Current test coverage: **96%**-based naming to prevent file conflicts.

## 🚀 Features

- **Easy to Use**: Simple class-based interface for QR code generation
- **Organized Output**: Automatically saves all QR codes to a designated output folder
- **Timestamp Naming**: Automatic file naming with timestamps to prevent overwrites
- **Customizable Prefix**: Set custom prefixes for generated QR code files
- **Customizable Output Directory**: Choose where to save your QR code files
- **High Quality**: Optimized settings for clear, scannable QR codes
- **Flexible Input**: Supports any text, URLs, or string data
- **Zero Configuration**: Works out of the box with sensible defaults

## 📋 Requirements

- Python 3.12+
- qrcode library
- Pillow (PIL) for image handling

## 🛠️ Installation

### Using Poetry (Recommended)

```bash
# Clone the repository
git clone https://github.com/ShanKonduru/QRCodeGenPy.git
cd QRCodeGenPy

# Install dependencies using Poetry
poetry install

# Activate the virtual environment
poetry shell
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/ShanKonduru/QRCodeGenPy.git
cd QRCodeGenPy

# Install dependencies
pip install -r requirements.txt
```

### Manual Installation

Install the required packages:

```bash
pip install qrcode[pil]
```

## 🎯 Quick Start

### Basic Usage

```python
from QRCodeGenerator import QRCodeGenerator

# Create a QR code generator instance (saves to 'output' folder by default)
generator = QRCodeGenerator()

# Generate a QR code for a URL
filename = generator.generate_qr_code("https://www.example.com")
print(f"QR code saved as: {filename}")
# Output: output/qr_code_20241001123456.png
```

### Custom File Prefix and Output Folder

```python
# Use a custom prefix and output folder
generator = QRCodeGenerator("my_website", "my_qr_codes")
filename = generator.generate_qr_code("https://www.mywebsite.com")
# Output: my_qr_codes/my_website_20241001123456.png
```

### Running the Example

```bash
python QRCodeGenerator.py
```

This will generate a QR code for the LinkedIn profile URL and save it in the `output` folder.

## 📖 API Documentation

### Class: `QRCodeGenerator`

#### Constructor

```python
QRCodeGenerator(file_prefix="qr_code", output_folder="output")
```

**Parameters:**

- `file_prefix` (str, optional): Prefix for the output filename. Defaults to "qr_code".
- `output_folder` (str, optional): Directory to save QR code images. Defaults to "output".

#### Methods

##### `generate_qr_code(input_string)`

Generates a QR code from the provided input string and saves it as a PNG image in the specified output folder.

**Parameters:**

- `input_string` (str): The text or URL to encode in the QR code.

**Returns:**

- `str`: The full path of the generated QR code image (includes folder and .png extension).

**Example:**
```python
generator = QRCodeGenerator()
filename = generator.generate_qr_code("Hello, World!")
```

## 🔧 QR Code Settings

The generated QR codes use the following optimized settings:

- **Version**: 1 (21x21 modules)
- **Error Correction**: Low (~7% error correction)
- **Box Size**: 10 pixels per module
- **Border**: 4 modules wide (minimum recommended)
- **Colors**: Black foreground on white background

## 📁 Project Structure

```
QRCodeGenPy/
├── QRCodeGenerator.py          # Main QR code generator class
├── requirements.txt            # pip dependencies
├── pyproject.toml             # Poetry configuration
├── poetry.lock               # Poetry lock file
├── pytest.ini               # Pytest configuration
├── run_tests.py              # Test runner script
├── README.md                 # This file
├── example_output_folders.py  # Example demonstrating output folders
├── 001.bat                  # Batch script
├── 002.bat                  # Batch script
├── tests/                    # Test directory
│   ├── __init__.py          # Test package init
│   ├── test_qr_code_generator.py  # Unit tests
│   └── test_main_function.py     # Integration tests
├── output/                   # Default QR code output directory
│   └── *.png                # Generated QR code files
└── htmlcov/                  # Coverage report (generated)
    └── index.html           # HTML coverage report
```

## 🎨 Examples

### Generate QR Code for Different Types of Data

```python
from QRCodeGenerator import QRCodeGenerator

# Create generator with custom prefix and output folder
generator = QRCodeGenerator("example", "my_qr_outputs")

# Website URL
website_qr = generator.generate_qr_code("https://www.github.com")
# Output: my_qr_outputs/example_20241001123456.png

# Contact information (vCard format)
contact_info = """BEGIN:VCARD
VERSION:3.0
FN:John Doe
ORG:Example Company
TEL:+1234567890
EMAIL:john@example.com
END:VCARD"""
contact_qr = generator.generate_qr_code(contact_info)

# WiFi connection info
wifi_info = "WIFI:T:WPA;S:MyNetworkName;P:MyPassword;;"
wifi_qr = generator.generate_qr_code(wifi_info)

# Plain text
text_qr = generator.generate_qr_code("Hello, QR Code World!")

# All files are saved in the 'my_qr_outputs' folder
```

## 🧪 Testing

Run the built-in example:

```bash
python QRCodeGenerator.py
```

This will create a QR code for the LinkedIn profile URL and display the filename.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Shan Konduru**
- LinkedIn: [https://www.linkedin.com/in/shankonduru/](https://www.linkedin.com/in/shankonduru/)
- Email: shankonduru@gmail.com

## 🙏 Acknowledgments

- [qrcode](https://github.com/lincolnloop/python-qrcode) library for QR code generation
- [Pillow](https://python-pillow.org/) for image processing
- Python community for excellent documentation and examples

## 📈 Version History

- **v0.1.0** - Initial release
  - Basic QR code generation
  - Timestamp-based file naming
  - Customizable file prefixes
  - Comprehensive documentation

---

Made with ❤️ by [Shan Konduru](https://www.linkedin.com/in/shankonduru/)
"""
Unit tests for QRCodeGenerator class.

This module contains comprehensive tests for the QRCodeGenerator class,
including functionality tests, edge cases, and error handling.
"""

import os
import tempfile
import shutil
import pytest
from PIL import Image
import sys
from pathlib import Path

# Add the parent directory to the path so we can import QRCodeGenerator
sys.path.insert(0, str(Path(__file__).parent.parent))

from QRCodeGenerator import QRCodeGenerator


class TestQRCodeGenerator:
    """Test class for QRCodeGenerator functionality."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.test_output_folder = os.path.join(self.test_dir, "test_output")
        
    def teardown_method(self):
        """Clean up after each test method."""
        # Remove the temporary directory and all its contents
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_init_default_parameters(self):
        """Test QRCodeGenerator initialization with default parameters."""
        generator = QRCodeGenerator()
        assert generator.file_prefix == "qr_code"
        assert generator.output_folder == "output"
        # Check that the output directory is created
        assert os.path.exists("output")

    def test_init_custom_parameters(self):
        """Test QRCodeGenerator initialization with custom parameters."""
        custom_prefix = "test_qr"
        generator = QRCodeGenerator(custom_prefix, self.test_output_folder)
        assert generator.file_prefix == custom_prefix
        assert generator.output_folder == self.test_output_folder
        # Check that the custom output directory is created
        assert os.path.exists(self.test_output_folder)

    def test_generate_qr_code_basic(self):
        """Test basic QR code generation functionality."""
        generator = QRCodeGenerator("test", self.test_output_folder)
        test_string = "https://www.example.com"
        
        result_path = generator.generate_qr_code(test_string)
        
        # Check that a file was created
        assert os.path.exists(result_path)
        
        # Check that the filename format is correct
        assert result_path.startswith(self.test_output_folder)
        assert "test_" in result_path
        assert result_path.endswith(".png")
        
        # Verify it's a valid image file
        img = Image.open(result_path)
        assert img.format == "PNG"
        img.close()

    def test_generate_qr_code_different_content_types(self):
        """Test QR code generation with different types of content."""
        generator = QRCodeGenerator("content_test", self.test_output_folder)
        
        test_cases = [
            "https://www.github.com",  # URL
            "Hello, World!",  # Plain text
            "mailto:test@example.com",  # Email
            "tel:+1234567890",  # Phone number
            "WIFI:T:WPA;S:MyNetwork;P:MyPassword;;",  # WiFi
            "BEGIN:VCARD\nVERSION:3.0\nFN:John Doe\nEND:VCARD",  # vCard
            "🎉 Unicode test! 中文 العربية",  # Unicode characters
            "",  # Empty string
            "Short string",  # Short string instead of very long one
        ]
        
        generated_files = []
        for i, test_content in enumerate(test_cases):
            # Add unique identifier to ensure different content
            result_path = generator.generate_qr_code(f"{test_content}__{i}")
            assert os.path.exists(result_path)
            assert result_path.endswith(".png")
            generated_files.append(result_path)
            
            # Verify it's a valid image
            img = Image.open(result_path)
            assert img.format == "PNG"
            img.close()
        
        # Check that all files are unique (different timestamps with microseconds)
        assert len(set(generated_files)) == len(generated_files)

    def test_filename_uniqueness(self):
        """Test that generated filenames are unique due to timestamps."""
        generator = QRCodeGenerator("unique_test", self.test_output_folder)
        
        # Generate multiple QR codes with microsecond precision timestamps
        files = []
        for i in range(5):
            result_path = generator.generate_qr_code(f"Test content {i}")
            files.append(result_path)
            assert os.path.exists(result_path)
        
        # All files should have unique names due to microsecond timestamps
        assert len(set(files)) == len(files)

    def test_output_folder_creation(self):
        """Test that output folders are created automatically."""
        nested_folder = os.path.join(self.test_dir, "level1", "level2", "level3")
        generator = QRCodeGenerator("folder_test", nested_folder)
        
        # Generate a QR code
        result_path = generator.generate_qr_code("Test folder creation")
        
        # Check that the nested folder structure was created
        assert os.path.exists(nested_folder)
        assert os.path.exists(result_path)

    def test_file_path_format(self):
        """Test that the returned file path format is correct."""
        generator = QRCodeGenerator("path_test", self.test_output_folder)
        result_path = generator.generate_qr_code("Test path format")
        
        # Check path components
        assert os.path.dirname(result_path) == self.test_output_folder
        filename = os.path.basename(result_path)
        assert filename.startswith("path_test_")
        assert filename.endswith(".png")
        
        # Check timestamp format in filename (should be YYYYMMDDHHMMSS + microseconds)
        timestamp_part = filename[len("path_test_"):-4]  # Remove prefix and .png
        assert len(timestamp_part) == 20  # YYYYMMDDHHMMSS + 6 digit microseconds
        assert timestamp_part.isdigit()

    def test_qr_code_properties(self):
        """Test that generated QR codes have the expected properties."""
        generator = QRCodeGenerator("prop_test", self.test_output_folder)
        result_path = generator.generate_qr_code("Property test")
        
        # Open and analyze the image
        img = Image.open(result_path)
        
        # Check basic properties
        assert img.format == "PNG"
        assert img.mode in ["RGB", "RGBA", "L", "1"]  # Include mode '1' for QR codes
        
        # QR codes should be square
        width, height = img.size
        assert width == height
        
        # Check that it's a reasonable size (should be > 20 pixels due to box_size=10)
        assert width > 20
        assert height > 20
        
        img.close()

    def test_special_characters_in_prefix(self):
        """Test QR code generation with special characters in prefix."""
        # Test with various prefix formats
        special_prefixes = [
            "test-qr",
            "test_qr",
            "test.qr",
            "TestQR",
            "123test",
        ]
        
        for prefix in special_prefixes:
            generator = QRCodeGenerator(prefix, self.test_output_folder)
            result_path = generator.generate_qr_code("Special prefix test")
            assert os.path.exists(result_path)
            assert prefix in os.path.basename(result_path)

    def test_large_content(self):
        """Test QR code generation with large content."""
        generator = QRCodeGenerator("large_test", self.test_output_folder)
        
        # Create a moderately large string that QR codes can handle
        large_content = "Large content test: " + "A" * 500  # Reduced from 2000
        
        result_path = generator.generate_qr_code(large_content)
        assert os.path.exists(result_path)
        
        # Verify it's a valid image
        img = Image.open(result_path)
        assert img.format == "PNG"
        img.close()

    def test_return_value_consistency(self):
        """Test that the returned path matches the actual file location."""
        generator = QRCodeGenerator("return_test", self.test_output_folder)
        result_path = generator.generate_qr_code("Return value test")
        
        # The returned path should exist
        assert os.path.exists(result_path)
        
        # The returned path should be absolute or properly formatted
        assert os.path.isabs(result_path) or result_path.startswith(self.test_output_folder)
        
        # The file should be readable
        img = Image.open(result_path)
        img.close()

    @pytest.mark.parametrize("content", [
        "https://www.example.com",
        "Plain text content",
        "Special chars: !@#$%^&*()",
        "Unicode: 🎉 中文 العربية",
        "Numbers: 1234567890",
    ])
    def test_parametrized_content_types(self, content):
        """Parametrized test for different content types."""
        generator = QRCodeGenerator("param_test", self.test_output_folder)
        result_path = generator.generate_qr_code(content)
        
        assert os.path.exists(result_path)
        assert result_path.endswith(".png")
        
        # Verify image validity
        img = Image.open(result_path)
        assert img.format == "PNG"
        img.close()


class TestQRCodeGeneratorEdgeCases:
    """Test class for QRCodeGenerator edge cases and error conditions."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.test_dir = tempfile.mkdtemp()
        self.test_output_folder = os.path.join(self.test_dir, "edge_test_output")

    def teardown_method(self):
        """Clean up after each test method."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_empty_string_content(self):
        """Test QR code generation with empty string."""
        generator = QRCodeGenerator("empty_test", self.test_output_folder)
        result_path = generator.generate_qr_code("")
        
        assert os.path.exists(result_path)
        
        # Verify it's a valid image (QR code can handle empty strings)
        img = Image.open(result_path)
        assert img.format == "PNG"
        img.close()

    def test_whitespace_only_content(self):
        """Test QR code generation with whitespace-only content."""
        generator = QRCodeGenerator("whitespace_test", self.test_output_folder)
        result_path = generator.generate_qr_code("   \n\t   ")
        
        assert os.path.exists(result_path)
        
        # Verify it's a valid image
        img = Image.open(result_path)
        assert img.format == "PNG"
        img.close()

    def test_very_long_content(self):
        """Test QR code generation with very long content."""
        generator = QRCodeGenerator("long_test", self.test_output_folder)
        
        # Create very long content (but within QR code limits)
        very_long_content = "Very long content: " + "X" * 1000  # Reduced from 5000
        
        result_path = generator.generate_qr_code(very_long_content)
        assert os.path.exists(result_path)
        
        # Verify it's a valid image
        img = Image.open(result_path)
        assert img.format == "PNG"
        img.close()
        assert img.format == "PNG"
        img.close()

    def test_unicode_content(self):
        """Test QR code generation with various Unicode characters."""
        generator = QRCodeGenerator("unicode_test", self.test_output_folder)
        
        unicode_content = "Unicode test: 🎉🚀💻 中文字符 العربية Русский язык"
        result_path = generator.generate_qr_code(unicode_content)
        
        assert os.path.exists(result_path)
        
        # Verify it's a valid image
        img = Image.open(result_path)
        assert img.format == "PNG"
        img.close()


if __name__ == "__main__":
    # Run the tests if this file is executed directly
    pytest.main([__file__, "-v"])
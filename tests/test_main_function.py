"""
Tests for the main function and integration tests.

This module tests the main function and provides integration tests
for the complete QRCodeGenerator workflow.
"""

import os
import sys
import tempfile
import shutil
from unittest.mock import patch
from io import StringIO
import pytest
from pathlib import Path

# Add the parent directory to the path so we can import modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from QRCodeGenerator import main, QRCodeGenerator


class TestMainFunction:
    """Test class for the main function."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.test_dir = tempfile.mkdtemp()
        # Store original directory to restore later
        self.original_cwd = os.getcwd()

    def teardown_method(self):
        """Clean up after each test method."""
        # Restore original directory
        os.chdir(self.original_cwd)
        
        # Clean up test directory
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        
        # Clean up any output directory created by main function
        if os.path.exists("output"):
            try:
                shutil.rmtree("output")
            except (OSError, PermissionError):
                # If we can't remove it, it might be in use by other tests
                pass

    def test_main_function_execution(self):
        """Test that the main function executes without errors."""
        # Change to test directory
        os.chdir(self.test_dir)
        
        # Capture stdout
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        
        # Check that output was printed
        output = captured_output.getvalue()
        assert "QR code generated successfully!" in output
        assert "File saved as:" in output
        assert ".png" in output
        
        # Check that a file was actually created
        assert os.path.exists("output")
        files = os.listdir("output")
        assert len(files) >= 1
        assert any(f.endswith(".png") for f in files)

    def test_main_function_creates_correct_file(self):
        """Test that the main function creates a QR code file with expected content."""
        # Change to test directory
        os.chdir(self.test_dir)
        
        # Run main function
        main()
        
        # Check the created file
        output_dir = "output"
        assert os.path.exists(output_dir)
        
        files = [f for f in os.listdir(output_dir) if f.endswith(".png")]
        assert len(files) >= 1
        
        # Check filename format
        qr_file = files[0]  # Get the first (or only) QR code file
        assert qr_file.startswith("qr_code_")
        assert qr_file.endswith(".png")
        
        # Check that it's a valid image file
        from PIL import Image
        img = Image.open(os.path.join(output_dir, qr_file))
        assert img.format == "PNG"
        img.close()

    def test_main_function_output_format(self):
        """Test that the main function output has the expected format."""
        # Change to test directory
        os.chdir(self.test_dir)
        
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            main()
        
        output = captured_output.getvalue().strip()
        
        # Check output format
        assert output.startswith("QR code generated successfully!")
        assert "output" in output  # Should mention the output directory
        assert "qr_code_" in output  # Should contain the default prefix
        assert ".png" in output


class TestIntegration:
    """Integration tests for the complete QRCodeGenerator workflow."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.test_dir = tempfile.mkdtemp()
        self.test_output_folder = os.path.join(self.test_dir, "integration_output")

    def teardown_method(self):
        """Clean up after each test method."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_end_to_end_workflow(self):
        """Test the complete end-to-end workflow."""
        # Create generator
        generator = QRCodeGenerator("integration_test", self.test_output_folder)
        
        # Test data representing different use cases
        test_scenarios = [
            ("Website", "https://www.github.com/ShanKonduru/QRCodeGenPy"),
            ("Email", "mailto:shankonduru@gmail.com"),
            ("Phone", "tel:+1234567890"),
            ("Text", "Hello from QR Code Generator!"),
        ]
        
        generated_files = []
        
        for scenario_name, content in test_scenarios:
            # Generate QR code
            result_path = generator.generate_qr_code(content)
            generated_files.append(result_path)
            
            # Verify file exists
            assert os.path.exists(result_path), f"File not created for {scenario_name}"
            
            # Verify file is in correct location
            assert result_path.startswith(self.test_output_folder), f"Wrong location for {scenario_name}"
            
            # Verify it's a valid image
            from PIL import Image
            img = Image.open(result_path)
            assert img.format == "PNG", f"Invalid image format for {scenario_name}"
            img.close()
        
        # Verify all files are unique
        assert len(set(generated_files)) == len(generated_files), "Generated files are not unique"
        
        # Verify all files exist in the output directory
        actual_files = os.listdir(self.test_output_folder)
        png_files = [f for f in actual_files if f.endswith(".png")]
        assert len(png_files) == len(test_scenarios), "Not all QR codes were created"

    def test_multiple_generators_different_folders(self):
        """Test using multiple generators with different output folders."""
        # Create multiple generators with different configurations
        generators = [
            QRCodeGenerator("web", os.path.join(self.test_dir, "websites")),
            QRCodeGenerator("contact", os.path.join(self.test_dir, "contacts")),
            QRCodeGenerator("misc", os.path.join(self.test_dir, "miscellaneous")),
        ]
        
        test_data = [
            "https://www.example.com",
            "mailto:test@example.com",
            "Random text content",
        ]
        
        # Generate QR codes with each generator
        for i, generator in enumerate(generators):
            result_path = generator.generate_qr_code(test_data[i])
            
            # Verify file exists
            assert os.path.exists(result_path)
            
            # Verify correct folder
            expected_folder = generator.output_folder
            assert result_path.startswith(expected_folder)
            
            # Verify correct prefix
            filename = os.path.basename(result_path)
            assert filename.startswith(generator.file_prefix)

    def test_concurrent_generation(self):
        """Test generating multiple QR codes in quick succession."""
        generator = QRCodeGenerator("concurrent", self.test_output_folder)
        
        # Generate multiple QR codes quickly
        contents = [f"Content number {i}" for i in range(10)]
        results = []
        
        for content in contents:
            result_path = generator.generate_qr_code(content)
            results.append(result_path)
            assert os.path.exists(result_path)
        
        # All results should be unique due to timestamps
        assert len(set(results)) == len(results)
        
        # All files should exist
        for result_path in results:
            assert os.path.exists(result_path)
            
            # Verify image validity
            from PIL import Image
            img = Image.open(result_path)
            assert img.format == "PNG"
            img.close()


if __name__ == "__main__":
    # Run the tests if this file is executed directly
    pytest.main([__file__, "-v"])
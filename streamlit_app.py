"""
Streamlit UI for QR Code Generator

A user-friendly web interface for generating QR codes from various types of content.
Users can input text, URLs, or other data and generate QR codes with customizable settings.
"""

import streamlit as st
import os
import tempfile
import base64
from datetime import datetime
from PIL import Image
import io

# Import our QR Code Generator
from QRCodeGenerator import QRCodeGenerator


def get_image_download_link(img_path, filename):
    """Generate a download link for the QR code image."""
    with open(img_path, "rb") as file:
        img_data = file.read()
    b64_img = base64.b64encode(img_data).decode()
    href = f'<a href="data:image/png;base64,{b64_img}" download="{filename}">📥 Download QR Code</a>'
    return href


def main():
    """Main Streamlit application."""
    # Page configuration
    st.set_page_config(
        page_title="QR Code Generator",
        page_icon="📱",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Title and description
    st.title("📱 QR Code Generator")
    st.markdown("Generate QR codes quickly and easily from any text or URL!")

    # Sidebar for settings
    st.sidebar.header("⚙️ Settings")
    
    # File prefix setting
    file_prefix = st.sidebar.text_input(
        "File Prefix", 
        value="qr_code", 
        help="Prefix for the generated QR code filename"
    )
    
    # Output folder setting
    output_folder = st.sidebar.text_input(
        "Output Folder", 
        value="streamlit_output", 
        help="Folder where QR codes will be saved"
    )

    # Content type selection
    content_type = st.sidebar.selectbox(
        "Content Type",
        ["Text", "URL", "Email", "Phone", "WiFi", "vCard", "Custom"],
        help="Select the type of content you want to encode"
    )

    # Main content area
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("📝 Input")
        
        # Dynamic input based on content type
        if content_type == "Text":
            content = st.text_area(
                "Enter your text:",
                placeholder="Hello, World!",
                height=150
            )
            
        elif content_type == "URL":
            content = st.text_input(
                "Enter URL:",
                placeholder="https://www.example.com"
            )
            
        elif content_type == "Email":
            email = st.text_input(
                "Email Address:",
                placeholder="user@example.com"
            )
            subject = st.text_input(
                "Subject (optional):",
                placeholder="Email subject"
            )
            body = st.text_area(
                "Message (optional):",
                placeholder="Email message",
                height=100
            )
            
            # Construct mailto URL
            content = f"mailto:{email}"
            if subject or body:
                params = []
                if subject:
                    params.append(f"subject={subject}")
                if body:
                    params.append(f"body={body}")
                if params:
                    content += "?" + "&".join(params)
                    
        elif content_type == "Phone":
            content = st.text_input(
                "Phone Number:",
                placeholder="+1234567890"
            )
            if content and not content.startswith("tel:"):
                content = f"tel:{content}"
                
        elif content_type == "WiFi":
            st.subheader("WiFi Settings")
            network_name = st.text_input("Network Name (SSID):")
            password = st.text_input("Password:", type="password")
            security = st.selectbox("Security Type:", ["WPA", "WEP", "nopass"])
            hidden = st.checkbox("Hidden Network")
            
            if network_name:
                content = f"WIFI:T:{security};S:{network_name};P:{password};H:{'true' if hidden else 'false'};;"
            else:
                content = ""
                
        elif content_type == "vCard":
            st.subheader("Contact Information")
            full_name = st.text_input("Full Name:")
            organization = st.text_input("Organization:")
            phone = st.text_input("Phone:")
            email = st.text_input("Email:")
            url = st.text_input("Website:")
            
            if full_name:
                content = f"""BEGIN:VCARD
VERSION:3.0
FN:{full_name}
ORG:{organization}
TEL:{phone}
EMAIL:{email}
URL:{url}
END:VCARD"""
            else:
                content = ""
                
        else:  # Custom
            content = st.text_area(
                "Enter your custom content:",
                placeholder="Enter any text, URL, or formatted data...",
                height=200
            )

        # Display preview of content
        if content:
            st.subheader("📋 Content Preview")
            st.code(content, language="text")

    with col2:
        st.header("🎯 QR Code")
        
        if content:
            try:
                # Create QR code generator
                generator = QRCodeGenerator(file_prefix, output_folder)
                
                # Generate QR code
                with st.spinner("Generating QR code..."):
                    qr_path = generator.generate_qr_code(content)
                
                # Display QR code
                if os.path.exists(qr_path):
                    # Load and display image
                    img = Image.open(qr_path)
                    st.image(img, caption="Generated QR Code", use_column_width=True)
                    
                    # Download link
                    filename = os.path.basename(qr_path)
                    download_link = get_image_download_link(qr_path, filename)
                    st.markdown(download_link, unsafe_allow_html=True)
                    
                    # File info
                    st.success(f"✅ QR code generated successfully!")
                    st.info(f"📁 Saved as: `{qr_path}`")
                    
                    # Image properties
                    st.subheader("📊 Image Properties")
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.metric("Width", f"{img.width}px")
                        st.metric("Format", img.format)
                    with col_b:
                        st.metric("Height", f"{img.height}px")
                        st.metric("Mode", img.mode)
                
            except Exception as e:
                st.error(f"❌ Error generating QR code: {str(e)}")
        else:
            st.info("👆 Enter content in the input section to generate a QR code")

    # Footer with additional information
    st.markdown("---")
    st.markdown("### 📚 How to Use")
    
    with st.expander("📖 Instructions"):
        st.markdown("""
        1. **Choose Content Type**: Select the type of content you want to encode
        2. **Enter Content**: Fill in the required fields based on your selection
        3. **Customize Settings**: Use the sidebar to adjust file prefix and output folder
        4. **Generate**: Your QR code will be generated automatically
        5. **Download**: Click the download link to save the QR code to your device
        
        **Supported Content Types:**
        - **Text**: Plain text content
        - **URL**: Website links and web addresses
        - **Email**: Email addresses with optional subject and message
        - **Phone**: Phone numbers for quick dialing
        - **WiFi**: WiFi network credentials for easy sharing
        - **vCard**: Contact information cards
        - **Custom**: Any custom formatted content
        """)

    with st.expander("💡 Tips"):
        st.markdown("""
        - **QR Code Quality**: The generated QR codes use optimized settings for best readability
        - **File Naming**: Files are automatically named with timestamps to prevent conflicts
        - **Large Content**: Keep content reasonably sized - very long text may create complex QR codes
        - **Testing**: Test your QR codes with different scanners to ensure compatibility
        - **WiFi Sharing**: Use the WiFi option to create QR codes for easy network sharing
        """)

    # Statistics in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📈 Session Statistics")
    
    # Initialize session state
    if 'qr_count' not in st.session_state:
        st.session_state.qr_count = 0
    
    # Count QR codes generated (this is a simple example)
    if content and st.sidebar.button("🔄 Reset Counter"):
        st.session_state.qr_count = 0
    
    st.sidebar.metric("QR Codes Generated", st.session_state.qr_count)


if __name__ == "__main__":
    main()
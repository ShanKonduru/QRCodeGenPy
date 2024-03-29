import qrcode
from datetime import datetime

class QRCodeGenerator:
    def __init__(self, file_prefix="qr_code"):
        self.file_prefix = file_prefix

    def generate_qr_code(self, input_string):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(input_string)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{self.file_prefix}_{current_datetime}.png"
        img.save(file_name)
        return file_name

if __name__ == "__main__":
    input_string = "https://www.linkedin.com/in/shankonduru/"
    file_prefix = ""
    
    if not file_prefix:
        file_prefix = "qr_code"

    qr_generator = QRCodeGenerator(file_prefix)
    file_name = qr_generator.generate_qr_code(input_string)
    print(f"QR code generated successfully! File saved as: {file_name}")

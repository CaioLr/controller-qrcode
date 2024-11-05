import qrcode
import qrcode.constants

def makeQRCode():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=2
    )

    qr.add_data('www.caioramos.me')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()

if __name__ == "__main__":
   makeQRCode()

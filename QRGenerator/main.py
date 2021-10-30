import qrcode

# a = qrcode.make("https://github.com")
# a.show()

a = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1
)

a.add_data("https://github.com")
a.make(fit=True)

img = a.make_image()
import qrcode


def generate_qrcode(url, save_path='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)
    return save_path

url = "http://118.25.67.226/images/e4109e697f9c40be9171936c846af1ac.png"
qrcode_path = generate_qrcode(url)
print(f"二维码已生成并保存为 {qrcode_path}")

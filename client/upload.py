import requests
import uuid
from PIL import Image
import io
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


def upload_image(image_path, nginx_url):
    try:
        # 打开图片并获取格式
        with open(image_path, 'rb') as f:
            image_data = f.read()
        image = Image.open(io.BytesIO(image_data))
        image_format = image.format.lower()
        
        if image_format not in ['jpg', 'jpeg', 'png', 'gif', 'webp', 'svg']:
            return "不支持的图片格式", None
        
        random_filename = f"{uuid.uuid4().hex}.{image_format}"
        print(random_filename)
        files = {'file': (random_filename, image_data)}
        response = requests.post(f"{nginx_url}/upload", files=files)
        
        if response.status_code == 200:
            return f"{nginx_url}/images/{random_filename}", random_filename
        else:
            return f"上传失败，状态码：{response.status_code}", None
    except Exception as e:
        return f"上传失败：{str(e)}", None

nginx_url = "http://118.25.67.226"
image_path = "xmbl.png"
download_link, random_filename = upload_image(image_path, nginx_url)
if download_link and random_filename:
    print(f"图片上传成功，下载链接：{download_link}")
    qrcode_path = generate_qrcode(download_link)
    print(f"二维码已生成并保存为 {qrcode_path}")
else:
    print(download_link)

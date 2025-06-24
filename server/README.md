# 安装步骤和细节

## 安装nginx

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install nginx
sudo mkdir -pv /var/www/images
sudo chown -R www-data:www-data /var/www/images/
sudo systemctl restart nginx
sudo nginx -t
sudo ufw allow 80/tcp
sudo apt -y install virtalenv
virtualenv -p python3 venv
cd venv/
source bin/activate
pip install flask pillow gunicorn
sudo chown -R ubuntu:ubuntu /var/www/images/
sudo chmod -R 755 /var/www/images
```
客户端上传代码,服务器端只提供下载.

## 服务器后端执行

```bash 
cd venv
source bin/activate 
gunicorn -w 4 server:app --bind 0.0.0.0:8080 
```



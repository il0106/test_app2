import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_LOGIN='ilyastarkovproekty@yandex.ru'
SMTP_PASSWORD='cifnetofhujpkbzy'
SMTP_SERVER='smtp.yandex.ru'
SMTP_PORT=465

verification_token = ''
user_email = 'il0106@yandex.ru'
base_url = ''



# Создаем письмо
msg = MIMEMultipart()
msg["From"] = SMTP_LOGIN
msg["To"] = user_email
msg["Subject"] = "Подтверждение регистрации"

# Создаем ссылку для верификации
verification_url = f"{base_url}/verify-email?token={verification_token}"

# HTML тело письма
html_body = f"""
<html>
<body>
    <h2>Добро пожаловать!</h2>
    <p>Спасибо за регистрацию. Для завершения регистрации, пожалуйста, подтвердите ваш email.</p>
    <p><a href="{verification_url}" style="background-color: #4CAF50; color: white; padding: 14px 20px; text-decoration: none; border-radius: 4px;">Подтвердить Email</a></p>
    <p>Или скопируйте эту ссылку в браузер:</p>
    <p>{verification_url}</p>
    <p>Если вы не регистрировались на нашем сайте, просто проигнорируйте это письмо.</p>
</body>
</html>
"""

msg.attach(MIMEText(html_body, "html"))

# Отправка через SMTP
with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
    server.login(SMTP_LOGIN, SMTP_PASSWORD)
    server.sendmail(SMTP_LOGIN, user_email, msg.as_string())

print(f"Email верификации отправлен на {user_email}")

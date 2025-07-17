import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
import os

from config import settings

class EmailService:
    def __init__(self):
        self.smtp_server = settings["SMTP_SERVER"]
        self.smtp_port = int(settings["SMTP_PORT"])
        self.smtp_login = settings["SMTP_LOGIN"]
        self.smtp_password = settings["SMTP_PASSWORD"]
        
    async def send_verification_email(self, user_email: str, verification_token: str, base_url: str = "http://localhost:3000") -> bool:
        """
        Отправляет email с ссылкой для верификации
        """
        try:
            # Создаем письмо
            msg = MIMEMultipart()
            msg["From"] = self.smtp_login
            msg["To"] = user_email
            msg["Subject"] = "Подтверждение регистрации"
            
            # Создаем ссылку для верификации
            verification_url = f"{base_url}/verify?token={verification_token}"
            
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
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.smtp_login, self.smtp_password)
                server.sendmail(self.smtp_login, user_email, msg.as_string())
            
            print(f"Email верификации отправлен на {user_email}")
            return True
            
        except Exception as e:
            print(f"Ошибка отправки email: {e}")
            return False
    
    async def send_password_reset_email(self, user_email: str, reset_token: str, base_url: str = "http://localhost:3000") -> bool:
        """
        Отправляет email для сброса пароля
        """
        try:
            # Создаем письмо
            msg = MIMEMultipart()
            msg["From"] = self.smtp_login
            msg["To"] = user_email
            msg["Subject"] = "Сброс пароля"
            
            # Создаем ссылку для сброса пароля
            reset_url = f"{base_url}/reset-password?token={reset_token}"
            
            # HTML тело письма
            html_body = f"""
            <html>
            <body>
                <h2>Сброс пароля</h2>
                <p>Вы запросили сброс пароля. Для создания нового пароля, нажмите на кнопку ниже.</p>
                <p><a href="{reset_url}" style="background-color: #2196F3; color: white; padding: 14px 20px; text-decoration: none; border-radius: 4px;">Сбросить пароль</a></p>
                <p>Или скопируйте эту ссылку в браузер:</p>
                <p>{reset_url}</p>
                <p>Если вы не запрашивали сброс пароля, просто проигнорируйте это письмо.</p>
                <p>Ссылка действительна в течение 1 часа.</p>
            </body>
            </html>
            """
            
            msg.attach(MIMEText(html_body, "html"))
            
            # Отправка через SMTP
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.smtp_login, self.smtp_password)
                server.sendmail(self.smtp_login, user_email, msg.as_string())
            
            print(f"Email сброса пароля отправлен на {user_email}")
            return True
            
        except Exception as e:
            print(f"Ошибка отправки email: {e}")
            return False

# Создаем экземпляр сервиса
email_service = EmailService() 
# Backend API

FastAPI приложение с аутентификацией и верификацией email.

## Настройка переменных окружения

1. Скопируйте файл `env.example` в `.env`:
```bash
cp env.example .env
```

2. Отредактируйте файл `.env` и заполните необходимые переменные:

### Обязательные переменные:
- `JWT_SECRET` - секретный ключ для JWT токенов
- `RESET_PASSWORD_TOKEN_SECRET` - секретный ключ для токенов сброса пароля
- `VERIFICATION_TOKEN_SECRET` - секретный ключ для токенов верификации
- `SMTP_LOGIN` - email для отправки писем
- `SMTP_PASSWORD` - пароль приложения для SMTP

### Опциональные переменные:
- `DATABASE_URL` - URL базы данных (по умолчанию: SQLite)
- `SMTP_SERVER` - SMTP сервер (по умолчанию: smtp.yandex.ru)
- `SMTP_PORT` - SMTP порт (по умолчанию: 465)
- `ALLOWED_ORIGINS` - разрешенные домены для CORS (через запятую)
- `DEBUG` - режим отладки (true/false)
- `HOST` - хост для запуска сервера
- `PORT` - порт для запуска сервера

## Запуск

### Локально:
```bash
python main.py
```

### Через Docker:
```bash
docker build -t backend .
docker run -p 8000:8000 --env-file .env backend
```

## API Endpoints

- `POST /auth/register` - регистрация пользователя
- `POST /auth/jwt/login` - вход в систему
- `POST /auth/jwt/logout` - выход из системы
- `GET /auth/verify/{token}` - верификация email
- `POST /auth/forgot-password` - запрос сброса пароля
- `POST /auth/reset-password` - сброс пароля
- `POST /resend-verification` - повторная отправка email верификации
- `GET /user/verification-status` - статус верификации пользователя 
#!/usr/bin/env python3
"""
Простой скрипт для тестирования основных endpoints API
"""

import requests
import json

# Конфигурация
BASE_URL = "http://localhost:8000"
TEST_EMAIL = "test@example.com"
TEST_PASSWORD = "testpassword123"

def test_api():
    """Тестирование основных endpoints"""
    
    print("🧪 Тестирование API endpoints")
    print("=" * 40)
    
    # Создаем сессию
    session = requests.Session()
    
    # 1. Тест регистрации
    print("\n1️⃣ Тест регистрации")
    print("-" * 20)
    
    register_data = {
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD
    }
    
    try:
        response = session.post(f"{BASE_URL}/auth/register", json=register_data)
        print(f"POST /auth/register")
        print(f"Status: {response.status_code}")
        
        if response.status_code == 201:
            print("✅ Пользователь успешно зарегистрирован")
        elif response.status_code == 422:
            print("⚠️ Пользователь уже существует")
        else:
            print(f"❌ Ошибка: {response.text}")
            
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return
    
    # 2. Тест логина
    print("\n2️⃣ Тест логина")
    print("-" * 20)
    
    login_data = {
        "username": TEST_EMAIL,
        "password": TEST_PASSWORD
    }
    
    try:
        response = session.post(f"{BASE_URL}/auth/jwt/login", data=login_data)
        print(f"POST /auth/jwt/login")
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            access_token = data.get("access_token")
            print("✅ Успешный вход")
            print(f"Token: {access_token}...")
        else:
            print(f"❌ Ошибка входа: {response.text}")
            return
            
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return
    
    # 3. Тест получения информации о пользователе
    print("\n3️⃣ Тест users/me")
    print("-" * 20)
    
    headers = {"Authorization": f"Bearer {access_token.split('.')[0]}"}
    
    try:
        response = session.get(f"{BASE_URL}/users/me", headers=headers)
        print(f"GET /users/me")
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            user_data = response.json()
            print("✅ Информация о пользователе получена")
            print(f"Email: {user_data.get('email')}")
            print(f"ID: {user_data.get('id')}")
            print(f"Active: {user_data.get('is_active')}")
        else:
            print(f"❌ Ошибка получения данных: {response.text}")
            
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return
    
    print("\n" + "=" * 40)
    print("✅ Все тесты завершены!")

if __name__ == "__main__":
    test_api() 
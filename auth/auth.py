from flask import request, jsonify
import requests


def decorator_autme_user(func, *args, **kwargs):
    try:
        async def test_autme_user(*args, **kwargs):
            resp = auth()
            if not resp["success"]:
                return {"success": False, "message": resp["message"]}, 400
            return await func(*args, **kwargs)

        return test_autme_user
    except Exception as e:
        return {"success": False, "message": "Укажите токен"}

def decorator_autme_admin(func, *args, **kwargs):
    try:
        async def test_autme_user(*args, **kwargs):
            resp = auth_admin()
            if not resp["success"]:
                return {"success": False, "message": resp["message"]}, 400
            return await func(*args, **kwargs)

        return test_autme_user
    except Exception as e:
        return {"success": False, "message": "Укажите токен"}

def auth():
    try:
        result = requests.get("http://eco-74.online:5425/api/check/token",
                                headers={"Authorization": request.headers["Authorization"]})
        return result.json()
    except Exception as e:
        return {"success": False, "message": "Ошибка! Сервер не доступен"}


def auth_admin():
    try:
        result = requests.get("http://eco-74.online:5425/api/check/token/admin",
                              headers={"Authorization": request.headers["Authorization"]})
        return result.json()
    except Exception as e:
        return {"success": False, "message": "Ошибка! Сервер не доступен"}

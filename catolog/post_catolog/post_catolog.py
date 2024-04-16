from datetime import datetime

from flask import request, jsonify

from database.main import *
from auth.auth import decorator_autme_admin

@decorator_autme_admin
async def new_catolog():
    try:
        body = request.json
        n_catolog = catolog()
        n_catolog.name = body["name"]
        result = session.query(product_type).filter(product_type.name == body["product_type"])
        for i in result:
            n_catolog.product_type = i.id
        if n_catolog.product_type is None:
            return jsonify({"message": "Проверьте вводимые данные!"}), 400
        if "description" in body:
            n_catolog.description = body["description"]
        n_catolog.price = body["price"]
        session.add(n_catolog)
        session.commit()
        return jsonify({"message": "Новая поизиция успешно добавлена"}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400

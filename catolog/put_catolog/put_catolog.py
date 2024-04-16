from datetime import datetime

from flask import request, jsonify

from database.main import *
from auth.auth import decorator_autme_admin


@decorator_autme_admin
async def update_catolog(catolog_id):
    try:
        body = request.json
        check_catolog: catolog = session.query(catolog).filter(catolog.id == catolog_id)
        for i in check_catolog:
            if "name" in body:
                i.name = body["name"]
            if "product_type" in body:
                result = session.query(product_type).filter(product_type.name == body["product_type"])
                success = False
                for j in result:
                    i.product_type = j.id
                    success = True
                if not success:
                    return jsonify({"message": "Такого типа не существует"}), 400
            if "description" in body:
                i.description = body["description"]
            if "price" in body:
                i.price = body["price"]
            session.commit()
            return jsonify({"message": "Изменения успешно внесены"}), 200
        return jsonify({"message": "Такой позиции не существует"}), 400
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
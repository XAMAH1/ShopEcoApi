from flask import request, jsonify

from auth.auth import decorator_autme_user
from database.main import *


@decorator_autme_user
async def get_all_catolog():
    try:
        catolog_all = []
        check_color: catolog = session.query(catolog).all()
        for i in check_color:
            catolog_all.append({
                "id": i.id,
                "name": i.name,
                "product_type": i.type_realt.name,
                "description": i.description,
                "price": i.price
            })
        return jsonify({"success": True, "catolog": catolog_all}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
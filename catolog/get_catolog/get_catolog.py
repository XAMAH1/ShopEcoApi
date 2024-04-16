from flask import request, jsonify

from auth.auth import decorator_autme_user
from database.main import *


@decorator_autme_user
async def get_all_catalog():
    try:
        catalog_all = []
        check_color: catalog = session.query(catalog).all()
        for i in check_color:
            catalog_all.append({
                "id": i.id,
                "name": i.name,
                "product_type": i.type_realt.name,
                "price": i.price
            })
        return jsonify({"success": True, "catalog": catalog_all}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"success": False, "message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
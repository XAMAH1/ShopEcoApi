from flask import request, jsonify

from database.main import *
from auth.auth import decorator_autme_user


@decorator_autme_user
async def get_cats(catolog_id):
    try:
        check_color = session.query(catolog).filter(catolog.id == catolog_id)
        for i in check_color:
            return jsonify({
                "success": False,
                "id": i.id,
                "name": i.name,
                "product_type": i.type_realt.name,
                "price": i.price
            }), 200
        return jsonify({"success": False, "message": "Ошибка! Такой позиции не существует"}), 400
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"success": False, "message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400
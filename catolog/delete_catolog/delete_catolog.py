from flask import request, jsonify

from database.main import *
from auth.auth import decorator_autme_admin


@decorator_autme_admin
async def delete_catolog(catolog_id):
    try:
        session.query(catolog).filter(catolog.id == catolog_id).delete()
        session.commit()
        return jsonify({"message": "Позиция успешно удалена"}), 200
    except Exception as e:
        print(e)
        session.rollback()
        return jsonify({"message": "Возникла ошибка на сервере! Проверьте вводимые данные и попробуйте еще раз"}), 400

import asyncio
from flask import Blueprint, request
from flask_cors import cross_origin

from catolog.get_catolog.get_catolog import get_all_catolog

catolog_profile = Blueprint('catolog_profile', __name__)


@catolog_profile.route("/cats", methods=["POST", "GET"])
@cross_origin()
def cats_all():
    # if request.method == "POST":
    #     return asyncio.run(new_cats())
    if request.method == "GET":
        return asyncio.run(get_all_catolog())


# @cats_profile.route("/cats/<int:cats_id>", methods=["PUT", "GET", "DELETE"])
# def current_color(cats_id):
#     if request.method == "PUT":
#         return asyncio.run(update_cats(cats_id))
#     if request.method == "GET":
#         return asyncio.run(get_cats(cats_id))
#     if request.method == "DELETE":
#         return asyncio.run(delete_cats(cats_id))
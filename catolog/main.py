import asyncio
from flask import Blueprint, request
from flask_cors import cross_origin

from catolog.get_catolog.get_catolog import get_all_catolog
from catolog.post_catolog.post_catolog import new_catolog
from catolog.put_catolog.put_catolog import update_catolog

catolog_profile = Blueprint('catolog_profile', __name__)


@catolog_profile.route("/catolog", methods=["POST", "GET"])
@cross_origin()
def cats_all():
    if request.method == "POST":
        return asyncio.run(new_catolog())
    if request.method == "GET":
        return asyncio.run(get_all_catolog())


@catolog_profile.route("/catolog/<int:catolog_id>", methods=["PUT", "GET", "DELETE"])
@cross_origin()
def current_color(catolog_id):
    if request.method == "PUT":
        return asyncio.run(update_catolog(catolog_id))
    # if request.method == "GET":
    #     return asyncio.run(get_cats(cats_id))
    # if request.method == "DELETE":
    #     return asyncio.run(delete_cats(cats_id))

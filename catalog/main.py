import asyncio
from flask import Blueprint, request
from flask_cors import cross_origin

from catalog.delete_catalog.delete_catalog import delete_catalog
from catalog.get_catalog.get_catalog import get_all_catalog
from catalog.get_catalog.get_current_catalog import get_catalog
from catalog.post_catalog.post_catalog import new_catalog
from catalog.put_catalog.put_catalog import update_catalog

catalog_profile = Blueprint('catalog_profile', __name__)


@catalog_profile.route("/catalog", methods=["POST", "GET"])
@cross_origin()
def cats_all():
    if request.method == "POST":
        return asyncio.run(new_catalog())
    if request.method == "GET":
        return asyncio.run(get_all_catalog())


@catalog_profile.route("/catalog/<int:catalog_id>", methods=["PUT", "GET", "DELETE"])
@cross_origin()
def current_color(catalog_id):
    if request.method == "PUT":
        return asyncio.run(update_catalog(catalog_id))
    if request.method == "GET":
        return asyncio.run(get_catalog(catalog_id))
    if request.method == "DELETE":
        return asyncio.run(delete_catalog(catalog_id))

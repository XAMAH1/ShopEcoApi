from flask import *
from flask_cors import CORS, cross_origin

from catolog.main import catolog_profile
from database.main import *
from config import API_HOST, API_PORT

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.register_blueprint(catolog_profile, url_prefix="/api")


@app.errorhandler(404)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": "Error path request"}, 404


@app.errorhandler(405)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": "Error method request"}, 404


@app.errorhandler(500)
def handle_request_entity_too_large_error(error):
    return {"success": False, "message": f"Возникла критическая ошибка сервера."}, 500


if __name__ == "__main__":
    app.run(debug=False, host=API_HOST[0], port=API_PORT)
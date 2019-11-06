from flask import Blueprint
from flask_restful import Api
from server.resources.image import ImageUpload


image_bp = Blueprint('image', __name__, url_prefix='/image')
image_api = Api(image_bp)

image_api.add_resource(ImageUpload, '/')
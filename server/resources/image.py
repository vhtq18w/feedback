import os

from config.base import BaseConfig
from flask_restful import reqparse, Resource
from server import photos
from server.models.image import Image
from werkzeug.datastructures import FileStorage


class ImageUpload(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('picture', type=FileStorage, location='files')
        args = parser.parse_args()
        picture = args['picture']
        filename = photos.save(picture),
        url = photos.url(filename)
        realurl = os.path.join(BaseConfig.DATA_IMAGE_DIR + filename[0])
        image = Image(
            filename=filename[0],
            url=url,
            realurl=realurl
        )
        image.insert()
        return {'id': image.id, 'url': image.url}, 201
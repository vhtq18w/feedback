import json
import os

from config.base import BaseConfig
from flask_restful import reqparse, Resource
from server import photos
from server.models.image import Image
from server.models.record import Record, RecordDetail
from werkzeug.datastructures import FileStorage


class RecordInfo(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('mail', type=str)
        parser.add_argument('image1', type=int)
        parser.add_argument('image2', type=int)
        parser.add_argument('image3', type=int)
        parser.add_argument('image4', type=int)
        parser.add_argument('image5', type=int)
        parser.add_argument('image6', type=int)
        parser.add_argument('image7', type=int)
        parser.add_argument('image8', type=int)
        parser.add_argument('image9', type=int)
        parser.add_argument('source', type=str)
        args = parser.parse_args()
        ip = reqparse.request.remote_addr
        record_detail = RecordDetail(
            title=args['title'],
            description=args['description'],
            source=args['source'],
            phone=args['phone'],
            mail=args['mail'],
            image1=args['image1'],
            image2=args['image2'],
            image3=args['image3'],
            image4=args['image4'],
            image5=args['image5'],
            image6=args['image6'],
            image7=args['image7'],
            image8=args['image8'],
            image9=args['image9']
        )
        record_detail.insert()
        record = Record(
            detail=record_detail.id,
            ip=ip
        )
        record.insert()

        return {'id': record.id}, 201


class RecordInfoWithImage(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('mail', type=str)
        parser.add_argument('picture', type=FileStorage, location='files', action='append')
        parser.add_argument('source', type=str)
        args = parser.parse_args()
        ip = reqparse.request.remote_addr
        record_detail = RecordDetail(
            title=args['title'],
            description=args['description'],
            source=args['source'],
            phone=args['phone'],
            mail=args['mail']
        )
        index = 0
        picture = reqparse.request.files.getlist("picture")
        for p in picture:
            f = photos.save(p)
            url = photos.url(f)
            realurl = os.path.join(BaseConfig.DATA_IMAGE_DIR + f)
            image = Image(
                filename=f,
                url=url,
                realurl=realurl
            )
            image.insert()
            if index == 0:
                record_detail.image1 = image.id
            elif index == 1:
                record_detail.image2 = image.id
            elif index == 2:
                record_detail.image3 = image.id
            elif index == 3:
                record_detail.image4 = image.id
            elif index == 4:
                record_detail.image5 = image.id
            elif index == 5:
                record_detail.image6 = image.id
            elif index == 6:
                record_detail.image7 = image.id
            elif index == 7:
                record_detail.image8 = image.id
            elif index == 8:
                record_detail.image9 = image.id
            index += 1
        record_detail.insert()
        record = Record(
            detail=record_detail.id,
            ip=ip
        )
        record.insert()
        return { 'id': record.id }, 201
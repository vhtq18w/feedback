from flask_restful import reqparse, Resource
from server.models.record import Record, RecordDetail


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
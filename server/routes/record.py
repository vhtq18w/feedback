from flask import Blueprint
from flask_restful import Api
from server.resources.record import RecordInfo


record_bp = Blueprint('record', __name__, url_prefix='/record')
record_api = Api(record_bp)

record_api.add_resource(RecordInfo, '/')
import os

from config.development import DevelopmentConfig
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import configure_uploads, IMAGES, patch_request_class, UploadSet
from server import routes


db = SQLAlchemy()
migrate = Migrate()
photos = UploadSet('photos', IMAGES)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    config = DevelopmentConfig
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    configure_uploads(app, photos)
    patch_request_class(app)

    with app.app_context():
        from .models.image import Image
        from .models.record import Record, RecordDetail

        @app.shell_context_processor
        def make_shell_context():
            return dict(
                app=app,
                db=db,
                Image=Image,
                Record=Record,
                RecordDetail=RecordDetail
            )

    try:
        os.makedirs(config.DATA_DIR)
        os.makedirs(config.DATA_IMAGE_DIR)
    except OSError:
        pass

    routes.init_route(app)

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app

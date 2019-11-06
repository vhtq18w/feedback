import os

from config.database import DatabaseConfig


class BaseConfig(DatabaseConfig):
    SECRET_KEY = os.getenv('SECRET_KEY', 'some secret words')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_DIR = os.path.abspath(os.path.dirname(CONFIG_DIR))
    DATA_DIR = os.path.join(PROJECT_DIR, "data")
    DATA_IMAGE_DIR = os.path.join(DATA_DIR, "images")
    UPLOADED_PHOTOS_DEST = DATA_IMAGE_DIR
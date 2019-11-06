from datetime import datetime
from server import db


class Record(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.now)
    ip = db.Column(db.String(40))

    def insert(self):
        db.session.add(self)
        db.session.commit()


class RecordDetail(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    source = db.Column(db.String(20))
    phone = db.Column(db.String(11))
    mail = db.Column(db.String(255))
    image1 = db.Column(db.Integer)
    image2 = db.Column(db.Integer)
    image3 = db.Column(db.Integer)
    image4 = db.Column(db.Integer)
    image5 = db.Column(db.Integer)
    image6 = db.Column(db.Integer)
    image7 = db.Column(db.Integer)
    image8 = db.Column(db.Integer)
    image9 = db.Column(db.Integer)

    def insert(self):
        db.session.add(self)
        db.session.commit()

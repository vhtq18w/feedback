from server import db


class Image(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    url = db.Column(db.String(255))
    realurl = db.Column(db.String(255))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_url_by_id(cls, id):
        url = cls.Query().filter_by(id=id).first()
        return url

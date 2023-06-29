from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.mutable import Mutable
from sqlalchemy.dialects.postgresql import ARRAY
db = SQLAlchemy()

class MutableList(Mutable, list):
    def append(self, value):
        list.append(self, value)
        self.changed()

    @classmethod
    def coerce(cls, key, value):
        if not isinstance(value, MutableList):
            if isinstance(value, list):
                return MutableList(value)
            return Mutable.coerce(key, value)
        else:
            return value


class Product(db.Model):
    __tablename__ = 'product'

    productid = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    productname = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    tags = db.Column(MutableList.as_mutable(ARRAY(db.Integer)))
    price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    domain = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Product(ProductId={})>'.format(self.productid)


from app import db
import datetime

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer(), primary_key=True)
    created_on = db.Column(db.DateTime(), default=db.func.current_timestamp())
    updated_on = db.Column(db.DateTime(), default=db.func.current_timestamp(),
                                            onupdate=db.func.current_timestamp())


from sqlalchemy.dialects.postgresql import JSON
from app import db
import uuid
# from .choice import ChoiceModel
from .base import Base
from marshmallow import Schema, fields
from sqlalchemy.dialects.postgresql import JSON

class ChoiceModel(Base, db.Model):
    __tablename__ = 'option'

    id = db.Column(db.Integer, primary_key = True)
    choice_text = db.Column(db.String())
    params = db.Column(JSON)
    image_url = db.Column(db.String())
    is_archived = db.Column(db.Boolean(), default = False)
    meta = db.Column(JSON)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    
    def __init__(self, id, choice_text, image_url, params, is_archived, meta, question_id):
        if(self.id == ""):
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.choice_text = choice_text
        self.image_url = image_url
        self.params = params
        self.is_archived = is_archived
        self.meta = meta
        self.question_id = question_id
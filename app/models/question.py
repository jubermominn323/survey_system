from app import db
import uuid
from .choice import ChoiceModel
import enum
from .base import Base
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import validates
from marshmallow import Schema, fields

class QUESTION_TYPE(enum.Enum):
    MCQ = "mcq"
    BOOLEAN = "boolean"
    QUESTION_GRP = "question_grp"
    SCALE = "scale"
    ENTRY = "entry"
    UPLOAD = "upload"
    PREFERENCE_ORDERING = "preference_ordering"
    THANK_YOU_PAGE = "thank_you_page"
    
list(QUESTION_TYPE)
# print([v.value for v in QUESTION_TYPE])

class QuestionModel(Base, db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(250), nullable = False)
    question_type = db.Column(db.String())
    description = db.Column(db.String())
    media = db.Column(db.String())
    params = db.Column(JSON)
    is_archived = db.Column(db.Boolean(), default = False)
    meta = db.Column(JSON)
    form_id = db.Column(db.Integer, db.ForeignKey('form.id'))
    option = db.relationship('ChoiceModel', backref = 'question')
    
    def __init__(self, id, text, question_type,description, media, params, meta, is_archived, form_id):
        if(self.id == ""):
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.text = text
        self.question_type = question_type
        self.description = description
        self.media = media
        self.params = params
        self.meta = meta
        self.is_archived = is_archived
        self.form_id = form_id

    @validates('question_type')
    def validate_question_type(self, cls, que_type):
        if que_type not in [v.value for v in QUESTION_TYPE]:
            raise AssertionError ("Invalid type of question")
        else:
            return que_type
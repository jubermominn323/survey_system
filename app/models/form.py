from app import db
import uuid
from .question import QuestionModel
from .base import Base
from sqlalchemy.dialects.postgresql import JSON

class FormModel(Base, db.Model):
    __tablename__ = 'form'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(), nullable = False)
    created_by = db.Column(db.String())
    welcome_img_url = db.Column(db.String())
    description = db.Column(db.String())
    button_label = db.Column(db.String())
    is_archived = db.Column(db.Boolean(), default = False)
    meta = db.Column(JSON)
    que_rel = db.relationship('QuestionModel', backref = 'form')

    def __init__(self, id, title, created_by, welcome_img_url, description, button_label, is_archived, meta):
        self.id = id
        self.title = title
        self.created_by = created_by
        self.welcome_img_url = welcome_img_url
        self.description = description
        self.button_label = button_label
        self.is_archived = is_archived
        self.meta = meta

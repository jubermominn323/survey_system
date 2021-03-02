from flask import request
from flask_restful import Resource
from app.models.form import FormModel
from app.models.question import QuestionModel
from app.models.choice import ChoiceModel
from app import db
import uuid

class FormApi(Resource):
    def post(self):
        data = request.get_json()
        
        # if data['id'] == "":
        #     data['id'] = uuid.uuid4()
        
        new_form = FormModel(id = data['id'] ,title = data['title'], created_by = data['created_by'],
                            welcome_img_url = data['welcome_img_url'],
                            description = data['description'], button_label = data['button_label'],
                            is_archived = data['is_archived'], meta = data['meta'])
        # db.session.add(new_form)

        que_data = data['question']
        for que in que_data:
            new_que = QuestionModel(id = que['id'] ,text = que['text'], question_type = que['question_type'],
                                description = que['description'], media = que['media'],
                                params = que['params'], is_archived = que['is_archived'],
                                meta = que['meta'], form_id = data['id'])
            db.session.add(new_que)

            choice_data = que['option']
            for choice in choice_data:
                new_choice = ChoiceModel(id = choice['id'], choice_text = choice['choice_text'], image_url = choice['image_url'],
                                params = choice['params'], is_archived = choice['is_archived'],
                                meta = choice['meta'], question_id = choice['question_id'])
                db.session.add(new_choice)
                
        db.session.add(new_form)
        db.session.commit()
        return {
            "message":"Successfull"
        },200

class FormsApi(Resource):
    def get(self, id):
        get_data = FormModel.query.filter_by(id=id).first()
        response = {
            "Title": get_data.title,
            "Created By": get_data.created_by,
            "Welcome Image URL": get_data.welcome_img_url,
            "Description": get_data.description,
            "Button Label": get_data.button_label,
            "Is Archived": get_data.is_archived,
            "Meta": get_data.meta
        }

        return {"Form Data": response}

    def put(self, id):
        data = request.get_json()
        to_update = FormModel.query.filter_by(id=id).first()
        to_update.title = data['title']
        to_update.created_by = data['created_by']
        to_update.welcome_img_url = data['welcome_img_url']
        to_update.button_label = data['button_label']
        to_update.is_archived = data['is_archived']
        to_update.meta = data['meta']

        db.session.add(to_update)
        db.session.commit()

    def delete(self, id):
        to_archive = FormModel.query.filter_by(id=id).first()
        db.session.delete(to_archive)
        # to_archive.is_archived = True
        db.session.commit()

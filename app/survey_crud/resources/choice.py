from flask import request
from flask_restful import Resource
from app.models.choice import ChoiceModel
# from app.models.choice import choice_schema
from app import db

class ChoiceApi(Resource):
    def post(self):
        data = request.get_json()
        new_choice = ChoiceModel(choice_text = data['choice_text'], image_url = data['image_url'],
                                params = data['params'], is_archived = data['is_archived'],
                                meta = data['meta'], question_id = data['question_id'])
        db.session.add(new_choice)
        db.session.commit()
    
    # def get(self):
    #     choice_data = ChoiceModel.query.all()
    #     print(choice_data)

class ChoicesApi(Resource):
    def get(self, id):
        get_data = ChoiceModel.query.filter_by(id=id).first()

        response = {
            "Choice Text": get_data.choice_text,
            "Image URL": get_data.image_url,
            "Params": get_data.params,
            "Is Archived": get_data.is_archived,
            "Meta": get_data.meta,
            "QuestionID": get_data.question_id
        }

        return {"Choices": response}

    def put(self, id):
        data = request.get_json()
        to_update = ChoiceModel.query.filter_by(id=id).first()

        to_update.choice_text = data['choice_text']
        to_update.image_url = data['image_url']
        to_update.params = data['params']
        to_update.is_archived = data['is_archived']
        to_update.meta = data['meta']
        to_update.question_id = data['question_id']

        db.session.add(to_update)
        db.session.commit()

    def delete(self, id):
        to_archive = ChoiceModel.query.filter_by(id=id).first()
        # to_archive.is_archived = True
        db.session.delete(to_archive)
        db.session.commit()
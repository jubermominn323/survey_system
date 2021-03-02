from flask import request
from flask_restful import Resource
from flask import jsonify
from app.models.question import QuestionModel
from app import db

class QuestionApi(Resource):
    def post(self):
        data = request.get_json()
        new_que = QuestionModel(text = data['text'], question_type = data['question_type'],
                                description = data['description'], media = data['media'],
                                params = data['params'], is_archived = data['is_archived'],
                                meta = data['meta'], form_id = data['form_id'])
        db.session.add(new_que)
        db.session.commit()
        return {"message":"Question added successfully."},200
    
class QuestionsApi(Resource):
    def get(self, id):
        get_data = QuestionModel.query.filter_by(id=id).first()
        
        response = {
            "Text":get_data.text,
            "Question Type": get_data.question_type,
            "Description": get_data.description,
            "media": get_data.media,
            "params": get_data.params,
            "Is Archived": get_data.is_archived,
            "Meta": get_data.meta,
            "FormID": get_data.form_id 
        }

        return {"message":"Success", "Question": response}

    def put(self, id):
        data = request.get_json()
        to_update = QuestionModel.query.filter_by(id=id).first()

        to_update.text = data['text']
        to_update.question_type = data['question_type']
        to_update.description = data['description']
        to_update.media = data['media']
        to_update.params = data['params']
        to_update.is_archived = data['is_archived']
        to_update.meta = data['meta']
        to_update.form_id = data['form_id']

        db.session.add(to_update)
        db.session.commit()
    
    def delete(self, id):
        to_archive = QuestionModel.query.filter_by(id=id).first()
        db.session.delete(to_archive)
        # to_archive.is_archived = True
        db.session.commit()
        return {"message":f"{to_archive.text} deleted successfully."}
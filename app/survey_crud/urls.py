from app.survey_crud.resources.question import QuestionApi, QuestionsApi
from app.survey_crud.resources.form import FormApi, FormsApi
from app.survey_crud.resources.choice import ChoiceApi, ChoicesApi
from app.survey_crud.resources.check_validation import CheckValidation

def initialize_routes(api):
    api.add_resource(FormApi, '/addForm')
    api.add_resource(FormsApi, '/addForm/<int:id>')
    api.add_resource(QuestionApi, '/addQues')
    api.add_resource(QuestionsApi, '/addQues/<int:id>')
    api.add_resource(ChoiceApi, '/addChoice')
    api.add_resource(ChoicesApi, '/addChoice/<int:id>')
    api.add_resource(CheckValidation, '/checkValidation/<int:id>')
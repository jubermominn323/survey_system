import unittest2
import os
import requests
from app import db, app

class testClass(unittest2.TestCase):
    API_URL = "http://127.0.0.1:5000/"
    QUE_URL = "{}/addQues".format(API_URL)
    QUE_OBJ = {
        "text": "Hello Juber, How are you",
        "question_type": "mcq",
        "description": "social",
        "media": "msk.com",
        "params": "ndf",
        "meta":  [{"2":"B"}],
        "is_archived":True,
        "form_id":11
    }

    def get_each_question_url(self, id):
        return "{}/{}".format(testClass.QUE_URL, id)

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    # def tearDown():
    #     pass

    def test_main_page(self):
        response = requests.get(testClass.API_URL)
        self.assertEqual(response.status_code, 200)
    
    def test_get_question(self):
        id = 73
        # API_URL = "http://127.0.0.1:5000/addQues"
        r = requests.get(self.get_each_question_url(id))
        self.assertEqual(r.status_code, 200)

    def test_post_question(self):
        r = requests.post(testClass.QUE_URL, json=testClass.QUE_OBJ)
        self.assertEqual(r.status_code, 200)

    def test_put_question(self):
        id = 73
        new_obj = {
            "text": "Hello Juber,",
            "question_type": "boolean",
            "description": "social",
            "media": "msk.com",
            "params": "ndf",
            "meta":  [{"2":"B"}],
            "is_archived":True,
            "form_id":11
        }

        r = requests.put(self.get_each_question_url(id), json=new_obj)
        self.assertEqual(r.status_code, 200)

    def test_delete_question(self):
        id = 73
        r = requests.delete(self.get_each_question_url(id))
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest2.main()
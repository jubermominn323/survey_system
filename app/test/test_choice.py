import unittest2
import os
import requests
from app import db, app

class testClass(unittest2.TestCase):
    API_URL = "http://127.0.0.1:5000/"
    CHOICE_URL = "{}/addChoice".format(API_URL)

    CHOICE_OBJ = {
            "choice_text":"It is a Choice text for Juber",
            "image_url":"www.xckjbvhxk.jxc",
            "params":"It is description",
            "is_archived":False,
            "meta":[{"1":"A"}],
            "question_id": 74
    }

    def get_each_choice_url(self, id):
        return "{}/{}".format(testClass.CHOICE_URL, id)

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    # def tearDown():
    #     pass

    def test_get_choice(self):
        id = 5
        r = requests.get(self.get_each_choice_url(id))
        self.assertEqual(r.status_code, 200)

    def test_post_choice(self):
        r = requests.post(testClass.CHOICE_URL, json=testClass.CHOICE_OBJ)
        self.assertEqual(r.status_code, 200)

    def test_put_choice(self):
        id = 4
        new_obj = {
            "choice_text":" Juber",
            "image_url":"xk.jxc",
            "params":"It is description kldnfv",
            "is_archived":False,
            "meta":[{"1":"A"}],
            "question_id": 74
        }

        r = requests.put(self.get_each_choice_url(id), json=new_obj)
        self.assertEqual(r.status_code, 200)

    def test_delete_choice(self):
        id = 3
        r = requests.delete(self.get_each_choice_url(id))
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest2.main()
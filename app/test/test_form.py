import unittest2
import os
import requests
from app import db, app

class testClass(unittest2.TestCase):
    API_URL = "http://127.0.0.1:5000/"
    FORM_URL = "{}/addForm".format(API_URL)

    FORM_OBJ = {
    "id":7,
    "title":"It is new form",
    "created_by":"schemer",
    "welcome_img_url":"www.dsdffeek.jxc",
    "description":"It is description",
    "button_label":"Submit",
    "is_archived":False,
    "meta":"",
    "question":[
        {
            "id":14,
            "text": "Enter your name",
            "question_type": "entry",
            "description": "Enter",
            "media": "mskcms",
            "params": "nsdfnsdkj",
            "meta":  "nsdc",
            "is_archived":False,
            "form_id":7,
            "option":[
                {
                    "id":104,
                    "choice_text":"please enter name",
                    "image_url":"www.xckjbvhxk.jxc",
                    "params":[
                        {
                            "type":"email",
                            "value":"juber@gmail.com"
                        }
                    ],
                    "is_archived":False,
                    "meta":[{"1":"A"}],
                    "question_id":14
                }
            ]
        },
        {
            "id":15,
            "text": "Enter your sirname",
            "question_type": "boolean",
            "description": "Enter",
            "media": "mskcms",
            "params": "nsdfnsdkj",
            "meta":  "nsdc",
            "is_archived":False,
            "form_id":7,
            "option":[
                {
                    "id":105,
                    "choice_text":"please enter sirname",
                    "image_url":"www.xckjbvhxk.jxc",
                    "params":[
                        {
                            "type":"yes_no",
                            "value":False
                        }
                    ],
                    "is_archived":False,
                    "meta":[{"1":"A"}],
                    "question_id":15
                }
            ]
        },
        {
            "id":16,
            "text": "Give your opinion ",
            "question_type": "scale",
            "description": "Enter",
            "media": "mskcms",
            "params": "nsdfnsdkj",
            "meta":  "nsdc",
            "is_archived":False,
            "form_id":7,
            "option":[
                {
                    "id":106,
                    "choice_text":"opinion scale",
                    "image_url":"www.xckjbvhxk.jxc",
                    "params":[
                        {
                            "type":"opinion_scale",
                            "scale_start_at_1":False,
                            "steps":11,
                            "value":11
                        }
                    ],
                    "is_archived":False,
                    "meta":[{"1":"A"}],
                    "question_id":16
                }
            ]
        },
        {
            "id":17,
            "text": "Rate us!",
            "question_type": "scale",
            "description": "Enter",
            "media": "mskcms",
            "params": "nsdfnsdkj",
            "meta":  "nsdc",
            "is_archived":False,
            "form_id":7,
            "option":[
                {
                    "id":107,
                    "choice_text":"rate us!",
                    "image_url":"www.xckjbvhxk.jxc",
                    "params":[
                        {
                            "type":"rating",
                            "value":3
                        }
                    ],
                    "is_archived":False,
                    "meta":[{"1":"A"}],
                    "question_id":17
                }
            ]
        }
    ]
}

    def get_each_form_url(self, id):
        return "{}/{}".format(testClass.FORM_URL, id)

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown():
        pass

    def test_get_form(self):
        id = 16
        # API_URL = "http://127.0.0.1:5000/addQues"
        r = requests.get(self.get_each_form_url(id))
        self.assertEqual(r.status_code, 200)

    def test_post_form(self):
        r = requests.post(testClass.FORM_URL, json=testClass.FORM_OBJ)
        self.assertEqual(r.status_code, 200)

    def test_put_form(self):
        id = 15
        new_obj = {
            "title":"It is a title for Juber",
            "created_by":"Juber",
            "welcome_img_url":"www.xckjbvhxk.jxc",
            "description":"It is description",
            "button_label":"Save",
            "is_archived":False,
            "meta":[{"1":"A"}]
        }

        r = requests.put(self.get_each_form_url(id), json=new_obj)
        self.assertEqual(r.status_code, 200)

    def test_delete_form(self):
        id = 14
        r = requests.delete(self.get_each_form_url(id))
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest2.main()
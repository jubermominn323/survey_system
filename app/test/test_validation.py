import unittest2
import os
import requests
from app import db, app

class testClass(unittest2.TestCase):
    API_URL = "http://127.0.0.1:5000/"
    FORM_URL = "{}/checkValidation".format(API_URL)

    def get_each_form_url(self, id):
        return "{}/{}".format(testClass.FORM_URL, id)

    def test_validation(self):
        id = 7
        r = requests.get(self.get_each_form_url(id))
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest2.main()
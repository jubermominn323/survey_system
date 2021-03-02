from app.models.form import FormModel
from flask import json, request
from flask import jsonify
import _json
import re
import boto3
from flask.wrappers import Response
from flask_restful import Resource
from app import db

class CheckValidation(Resource):
    def get(self, id):
        data = FormModel.query.filter_by(id=id).first()
        que_data = data.que_rel
        
        def validate_mail(value):
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if not (re.search(regex, value)):
                return {"error":"Invalid Email"},400
            else:
                return

        def validate_phone_no(value):
            Pattern = re.compile("^[789]\d{9}$")
            if not Pattern.match(value):
                return {"error":"Invalid Phone Number"},400
            else:
                return
            
        def validate_website(value):
            regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

            if not (re.search(regex, value)):
                return {"error":"Invalid URL"},400
            else:
                return

        def validate_entry(params):
            # print(params)
            parsedData = json.loads(params)

            for val in parsedData:
                if val['type'] == "email":
                    resp = validate_mail(val['value'])
                    return resp
                if val['type'] == "phone_number":
                    resp = validate_phone_no(val['value'])
                    return resp
                if val['type'] == "website":
                    resp = validate_website(val['value'])
                    return resp


        def validate_opinion_scale(value, scale_start_at_1, steps):
            print(steps)
            if scale_start_at_1:
                if steps < 11 and steps > 0:
                    if value > steps or value < 0:
                        return {"error":"Invalid Scale, value greater than steps or value less than 0."},400
                else:
                    return {"error":"Invalid Scale, steps are greater than 10 or less than 1."},400
            elif not scale_start_at_1:
                if steps < 12 and steps > -1:
                    if value > steps or value < 0:
                        return {"error":"Invalid Scale, value greater than steps or value less than 0."},400
                else:
                    return {"error":"Invalid Scale, steps are greater than 11 or less than 0."},400

        def validate_rating(value):
            if value > 5 or value < 0:
                return {"error":"Invalid Rating, must be between 0 to 5."},400

        def validate_scale(params):
            parsedData = json.loads(params)
            for val in parsedData:
                if val['type'] == "opinion_scale":
                    resp = validate_opinion_scale(val['value'], val['scale_start_at_1'], val['steps'])
                    return resp
                if val['type'] == "rating":
                    resp = validate_rating(val['value'])
                    return resp

        def validate_bool(params):
            parsedData = json.loads(params)
            for val in parsedData:
                if val['type'] == "yes_no":
                    if not type(val['value']) == bool:
                        return {"error":"Invalid Boolean Value"},400
                else:
                    return {"error":"Invalid Type"}
        
        for que in que_data:
            if que.question_type == 'entry':
                choice_data = que.option
                for opt in choice_data:
                    res = validate_entry(opt.params)
                    if res != None:
                        return res
    
            if que.question_type == "scale":
                choice_data = que.option
                for opt in choice_data:
                    res = validate_scale(opt.params)
                    if res != None:
                        return res

            # print(choice_data)
            if que.question_type == 'boolean':
                choice_data = que.option
                for opt in choice_data:
                    res = validate_bool(opt.params)
                    if res != None:
                        return res

        # client = boto3.resource('sqs',
        #                 endpoint_url='http://localhost:9324',
        #                 region_name='elasticmq',
        #                 aws_secret_access_key='x',
        #                 aws_access_key_id='x',
        #                 use_ssl=False)
        # queue = client.get_queue_by_name(QueueName='queue1')

        # region = boto3.sqs.regioninfo.RegionInfo(name='elasticmq',
        #                                 endpoint="http://localhost:9324")
        # conn = boto3.connect_sqs(aws_access_key_id='x',
        #                 aws_secret_access_key='x',
        #                 is_secure=False,
        #                 port=9324,
        #                 region=region)

        # response = queue.send_message(MessageBody = data)
        # return response
"""This classs Statistic used as resource to make a api resource of data output or response"""
from flask_restful import Resource, request
from flask import jsonify
from functions.processStatistics import processStatistics
import json

class Statistics(Resource):
    def get(self):
        """This get method for getting list can be default date range nor with range specification
        processStatistics("2019-04-14", "2019-04-14") """
        try:
            # message = processStatistics("201904-14", "2019-04-14")
            message = processStatistics()
            data = []
            for msg in message:
                data.append({'websiteId': msg['websiteId'],
                            'chat': msg['chats'],
                            'missedChats': msg['missedChats']})
            return data, 200
        except:
            return {"message":"Invalid dates, Please check dates"}, 500
        
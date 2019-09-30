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
            # dataList = processStatistics("201904-14", "2019-04-14")
            dataList = processStatistics()
            data = []
            for dl in dataList:
                data.append({'websiteId': dl['websiteId'],
                            'chat': dl['chats'],
                            'missedChats': dl['missedChats']})
            return data, 200
        except:
            return {"message":"Invalid dates, Please check dates"}, 500
        
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
            # error date 2019,04-14
            # start=2019,4-12&end=2019-4-13
            # http://localhost:5000/?start=2019-4-12&end=2019-4-13
            if request.args.get('start') and request.args.get('end'):
                start = request.args.get('start')
                end = request.args.get('start')
                dataList = processStatistics(start, end)
            else:
                dataList = processStatistics()

            data = []
            for dl in dataList:
                data.append({'websiteId': dl['websiteId'],
                             'chat': dl['chats'],
                             'missedChats': dl['missedChats']})
            return data, 200
        except:
            return {"message":"Invalid dates, Please check dates"}, 500
        
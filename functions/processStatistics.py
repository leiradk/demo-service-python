"""Functions for processing the list of the statistics"""

import requests
import json
import datetime

def processStatistics(start = datetime.date(2019,1,1), end = datetime.date(2019,12,31)):
    """This is a function that you can specified date or by default 2019-1-1 to 2019-12-31"""
    try:
        baseURL = 'https://bitbucket.org/!api/2.0/snippets/tawkto/aA8zqE/4f62624a75da6d1b8dd7f70e53af8d36a1603910/files/webstats.json'
        response = requests.get(baseURL)
        resData = json.loads(json.dumps(response.text))

        resData = json.loads(resData)
        data = []
        
        for dataList in resData:
            dataDate = processDate(dataList['date'])
            start = processDate(str(start))
            end = processDate(str(end))
            if start <= dataDate and end >= dataDate:  
                data.append(dataList)

        return data[::-1]
    except:
        raise Exception("Invalid dates, Please check dates")

def processDate(datestr: str):
    """Process the date to compare one's date at this format %Y-%m-%dT%H:%M:%S.%fZ (2019-04-01T00:00:00.000Z) and %Y-%m-%dT%H:%M:%SZ (2019-04-01T00:00:00Z)"""
    try:
        dtime = datetime.datetime.strptime(datestr,"%Y-%m-%dT%H:%M:%S.%fZ").date()
        return dtime
    except:
        try:
            dtime = datetime.datetime.strptime(datestr,"%Y-%m-%dT%H:%M:%SZ").date()
            return dtime
        except:
            try:
                datestr = datestr.replace("/","-")
                dtime = datetime.datetime.strptime(datestr,"%Y-%m-%d").date()
                return dtime
            except:
                dtime = datetime.datetime.strptime(datestr,"%Y-%m-%d").date()
                return dtime

import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':'HW8WBBF6YKMBQOL7YJJMZV78CO7WX1KX',
  'secret':'WE5OOUMQJT59MXPV',
  'usetype':'stage',
  'phone': '9056486858',
  'message':'hiiiii',
  'senderid':'Studypoint'
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest('https://www.sms4india.com/api/v1/sendCampaign','HW8WBBF6YKMBQOL7YJJMZV78CO7WX1KX', 'WE5OOUMQJT59MXPV', 'stage', '9056486858', 'Studypoint', 'hiiiiiiiiiii' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""

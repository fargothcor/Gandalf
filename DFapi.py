import apiai
import json


def get_smart_response(text):
    request = apiai.ApiAI('37ba0c86b0424b768a918211f4416581').text_request()
    request.lang = 'ru'
    request.session_id = 'BatlabAIBot'
    request.query = text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    return response


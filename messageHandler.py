from apiVk import sendMessage
import DFapi


def createAnswer(data, token):
    userID = data['user_id']
    message = DFapi.get_smart_response(data['body'])
    sendMessage(userID, message)

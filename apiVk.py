import vk
from Gandalf.config import TOKEN
session = vk.Session()
api = vk.API(session, v=5.50)


def sendMessage(user_id, message, attachment=""):
    api.messages.send(access_token=TOKEN, user_id=str(user_id), message=message, attachment=attachment)

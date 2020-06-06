import vk
from Gandalf.config import TOKEN
from random import randint
session = vk.Session()
api = vk.API(session, v=5.107)


def sendMessage(user_id, message, attachment=""):
    api.messages.send(
        access_token=TOKEN,
        peer_id=str(user_id),
        message=message,
        attachment=attachment,
        random_id=randint(0, 99999999),
        dont_parse_links=0
        )

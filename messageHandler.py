from Gandalf.apiVk import sendMessage
import Gandalf.DFapi as DFapi
import os
import importlib
from Gandalf.command_class import command_list


def load_modules():
   files = os.listdir("Gandalf/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("Gandalf.commands." + m[0:-3])


def create_answer(data):
    userID = data['user_id']
    text = data['body']
    if text[0] == '/':
        load_modules()
        for c in command_list:
            if text == c.key:
                message = c.process(text)
    else:
        message = DFapi.get_smart_response(text)
    sendMessage(userID, message)

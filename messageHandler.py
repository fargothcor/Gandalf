from Gandalf.apiVk import sendMessage
import Gandalf.DFapi as DFapi
import os
import importlib
from Gandalf.command_class import command_list
userInCommands = {}


def load_modules():
    files = os.listdir("Gandalf/commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("Gandalf.commands." + m[0:-3])


def create_answer(data):
    userID = data['message']['peer_id']
    text = data['message']['text']
    if userID in userInCommands:
        message = userInCommands[userID].process(text)
        userInCommands.pop(userID)
    elif text[0] == '/':
        load_modules()
        for c in command_list:
            if text == c.key:
                if c.isLong == 1:
                    userInCommands[userID] = c
                    message = c.description
                else:
                    message = c.process()
    else:
        message = DFapi.get_smart_response(text)
    sendMessage(userID, message)

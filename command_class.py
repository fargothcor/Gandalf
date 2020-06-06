command_list = []


class Command:
    def __init__(self):
        self.key = ''
        command_list.append(self)
        self.args = ''
        self.description = ''
        self.isLong = 0

    def process(self):
        pass

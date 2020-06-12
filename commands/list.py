import Gandalf.command_class as cc


def solve():
    resp = ''
    for c in cc.command_list:
        resp += c.key + ' - ' + c.description
    return resp


foo = cc.Command()
foo.key = '/help'
foo.description = 'Все команды'
foo.isLong = 0
foo.process = solve

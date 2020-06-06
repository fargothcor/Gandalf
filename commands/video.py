import math
import Gandalf.command_class as cc


def hoho():
    return 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


foo = cc.Command()
foo.key = '/video'
foo.description = 'Отправлю вам видос за ваш счет'
foo.isLong = 0
foo.process = hoho
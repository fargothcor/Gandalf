from random import randint as ri
import Gandalf.command_class as cc


def hoho():
    videos = [
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'https://www.youtube.com/watch?v=SRwrg0db_zY',
        'https://www.youtube.com/watch?v=V9AbeALNVkk',
        'https://www.youtube.com/watch?v=djV11Xbc914'
    ]
    return videos[ri(0, len(videos))]


foo = cc.Command()
foo.key = '/video'
foo.description = 'Отправлю вам видос за ваш счет'
foo.isLong = 0
foo.process = hoho
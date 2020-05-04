import math
import Gandalf.command_class as cc


def solve(s):
    if len(s.split()) != 3:
        return 'А?'
    else:
        a, b, c = map(int, s.split())
        x1 = (-b - math.sqrt(b*b - 4*a*c))
        x2 = (-b + math.sqrt(b*b - 4*a*c))
        return str(x1) + str(x2)


foo = cc.Command()
foo.key = '/equation'
foo.description = 'Решаю уравнения вида ax^2+bx+c=0 за вас. Введи коэффициенты a b c через пробел, и я скажу x1 и x2/'
foo.process = solve

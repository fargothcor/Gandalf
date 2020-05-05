import math
import Gandalf.command_class as cc


def solve(s):
    if len(s.split()) != 3:
        return 'А?'
    else:
        a, b, c = map(int, s.split())
        if (b*b - 4*a*c) > 0:
            x1 = (-b - math.sqrt(b*b - 4*a*c))
            x2 = (-b + math.sqrt(b*b - 4*a*c))
            alt = f"\n Альтернативный вид: x1 = ({-b} - &#8730;{b * b - 4 * a * c})/{2 * a}, " \
                f"x2 = ({-b} + &#8730;{b * b - 4 * a * c})/{2 * a}"
            return str(round(x1, 3)) + ' ' + str(round(x2, 3)) + alt
        else:
            return 'Это уравнение не имеет решений'


foo = cc.Command()
foo.key = '/equation'
foo.description = 'Решаю уравнения вида ax^2+bx+c=0 за вас. Введи коэффициенты a b c через пробел, и я скажу x1 и x2/'
foo.process = solve

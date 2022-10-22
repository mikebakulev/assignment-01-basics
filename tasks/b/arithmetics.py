"""
Вам даны три переменные x, y и z, в которые записаны два случайных целых и
одно случайное вещественное число, соответственно.

В этом задании вам запрещено заводить новые переменные и подключать модули.

Выведите по очереди:
- сами три числа через пробел
    > уже написано за вас
- [a] их сумму
- [b] их произведение
- [c] округленное вверх до целого произведение x и z
- [d] частное x и z
- [e] неполное частное при делении x на z
- [f] остаток от деления x на y
- [g] y в степени z
- [h] куб произведения трех их попарных сумм
- [i] число z с ровно пятью знаками после точки
    > подсказка: используйте форматную строку (f-string)

Запишите в переменную FLOATS, сколько среди пунктов [a]-[h] нецелых результатов
в смысле type(результата) == float.
"""

from test.common.context import get_integer, get_float  # не обращайте внимание

x = get_integer()
y = get_integer()
z = get_float()
print(x, y, z)  # вывести три числа через пробел

# Место для вашего кода
# спасибо
FLOATS = 0

print(x + y + z)
if (x + y + z)!=int(x + y + z):
    FLOATS+=1
    #print('-------')
print(x * y * z)
if (x * y * z)!= int(x * y * z):
    FLOATS+=1
    #print('-------')
if int(x*z)==z*x:
    print(int(x*z))
    if (int(x * z) ) != int(int(x * z) ):
        FLOATS += 1
        # print('-------')
else:
    print(int(x * z) + 1)
    if (int(x * z) + 1)!=int(int(x * z) + 1):
        FLOATS+=1
        #print('-------')
print(x/z)
if (x/z)!=int(x/z) :
    FLOATS += 1
    #print('-------')
print(x//z)
if (int(x//z))!= int(int(x//z)):
    FLOATS +=1
    #print('-------')
print(x % y)
if (x % y)!=int(x % y):
    FLOATS+=1
    #print('-------')
print(y**z)
if (y**z)!= int(y**z) :
    FLOATS+=1
    #print('-------')
print(((x+y)*(x+z)*(z+y))**3)
if (((x+y)*(x+z)*(z+y))**3)!=int(((x+y)*(x+z)*(z+y))**3):
    FLOATS+=1
    #print('-------')
print(('{:.5f}'.format(z)))
if (float('{:.5f}'.format(z)))!= int(float('{:.5f}'.format(z))):
    FLOATS+=1
    #print('-------')
print(FLOATS)


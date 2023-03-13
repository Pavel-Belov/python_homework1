"""
Задача 8: Требуется определить, можно ли от шоколадки
размером n × m долек отломить k долек, если разрешается
сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).

*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""

while True:
    print('Введите размер шоколадки')
    input_n = input('n: ')
    input_m = input('m: ')
    input_k = input('Введите k долек, которые нужно отломить: ')

    if input_n.isdigit() == False or input_m.isdigit() == False or input_k.isdigit() == False:
        print('Данные введены некорректно, повторите попытку')
    else:
        break

n = int(input_n)
m = int(input_m)
k = int(input_k)

if (k >= n and k < n * m and k % n == 0) or (k >= m and k < n * m and k % m == 0):
    print(k, '-> yes')
else:
    print(k, '-> no')
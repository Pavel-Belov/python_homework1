# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random

while True:
    n = input('Введите количество элементов массива: ')
    x = input('Введите число для проверки: ')

    if not n.isdigit() or not x.isdigit():
        print('Данные введены неверно. Повторите попытку.')
    else:
        break

my_list = [random.randint(1, int(n)) for i in range(int(n))]
print(f'Массив случайных чисел: {my_list}')

up = 1
up_element = 0
up_flag = False
if int(x) < int(n):
    while not up_flag:
        for i in my_list:
            if i == int(x) + up:
                up_element = i
                up_flag = True
        if not up_flag:
            up += 1

down = 1
down_element = 0
down_flag = False
if int(x) > 1:
    while not down_flag:
        for i in my_list:
            if i == int(x) - down:
                down_element = i
                down_flag = True
        if not down_flag:
            down += 1

if up_element == 0:
    print(f'Ближайший элемент к числу {x} равен {down_element}')
elif down_element == 0:
    print(f'Ближайший элемент к числу {x} равен {up_element}')
elif up > down:
    print(f'Ближайший элемент к числу {x} равен {down_element}')
elif up < down:
    print(f'Ближайший элемент к числу {x} равен {up_element}')
elif up == down:
    print(f'Ближайший наименьший элемент к числу {x} равен {down_element}')
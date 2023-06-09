# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью,поэтому ко времени сбора
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

import random

while True:
    n = input('Введите число кустов черники: ')
    if not n.isdigit():
        print('Данные введены неверно. Повторите попытку.')
    else:
        break

bush = [random.randint(1, 50) for i in range(int(n))]
print(f'{n} -> {bush}')
sum = 0
max = sum
index = 0
for i in range(len(bush)):
    if i == 0:
        sum = bush[-1] + bush[0] + bush[1]
    elif i == len(bush) - 1:
        sum = bush[-2] + bush[-1] + bush[0]
    else:
        sum = bush[i - 1] + bush[i] + bush[i + 1]
    if sum > max:
        max = sum
        index = i

print(f"Куст {index + 1}: -> Ягод: {max}")
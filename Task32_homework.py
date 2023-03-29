# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

while True:
    try:
        min = int(input("Введите нижнюю границу диапазона: "))
        max = int(input("Введите верхнюю границу диапазона: "))
        n = int(input("Введите количество элементов массива: "))
        break
    except:
        print("Данные введены неверно")

data = [random.randint(min - 10, max + 10) for i in range(n)]
print(data)

result = []
for i in range(len(data)):
    if data[i] >= min and data[i] <= max:
        result.append(i)

print(result)
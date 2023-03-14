# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2 в ступени k)), не превосходящие числа N.
# 10 -> 1 2 4 8

while True:
    try:
        n = int(input("Введите число N: "))
        output = list()
        for i in range(n):
            result = 2 ** i
            if result > n:
                print(output)
                break
            output.append(result)
    except:
        print("Данные некорректны! Введите число N")
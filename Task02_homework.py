"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

while True:
    input_num = input('Введите трёхзначное число: ')

    if input_num.isdigit() == False or len(input_num) != 3:
        print('Данные введены некорректно, повторите попытку')
    else:
        break

sum = 0
num = int(input_num)

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
else:
    print('Сумма цифр числа равна:', sum)
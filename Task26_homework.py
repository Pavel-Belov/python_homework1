# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# если степень отрицительная то корень а в степени б

import math

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

def power(a, b):
    if b > 0:
        return a * power(a, b - 1)
    elif b < 0:
        return (1 / a) * power(a, b + 1)
    else:
        return 1

print(f"A = {a}; B = {b} -> {power(a, b)}")
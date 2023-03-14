# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

while True:
    try:
        s = int(input("Введите сумму загаданных чисел: "))
        p = int(input("Введите произведение загаданных чисел: "))

        x = 0
        y = 0
        while x + y != s and x * y != p:
            x += 1
            if x + y != s:
                y += 1
            
        if x <= 1000 and y <= 1000:
            print(s, p, "->", x, y)
            break
        else:
            print("Петя загадал слишком большое число!")
    except:
        print("Петя ввёл некорректные данные!")
            
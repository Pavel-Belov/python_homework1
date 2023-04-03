# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

# *Пример:*

# **Ввод:**       пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:**      Парам пам-пам  

vowels = ['а','е','ё','и','о','у','ы','э','ю','я']
vinni_say = "пара-ра-рам рам-пам-папам па-ра-па-да"
print(vinni_say)
vinni_phrases = vinni_say.split()

def calculate_vowels(str, check_str):
    count_vowels = 0
    for i in str:
        for j in check_str:
            if i == j:
                count_vowels += 1
    return count_vowels

def check_rhythm(calc_func, vinni_phrases):
    iter = 0
    for i in vinni_phrases:
        counter = calc_func(i, vowels)
        if iter == 0:
            counter_prev = counter
        if counter_prev != counter:
            return False
        iter += 1
    return True

if check_rhythm(calculate_vowels, vinni_phrases):
    print("Парам пам-пам")
else:
    print("Пам парам")
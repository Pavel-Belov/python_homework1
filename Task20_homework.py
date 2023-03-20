# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

def create_dict(dictionary, list):
    point = 1
    for i in list:
        for j in i:
            dictionary[j] = point
        if point == 5:
            point += 3
        elif point == 8:
            point += 2
        else:
            point += 1

def check_right_input(dictionary, text):
    right_input_list = list()
    for i in text:
        for item in dictionary:
            if i.upper() == item:
                flag_input = True
                break
            else:
                flag_input = False
        right_input_list.append(flag_input)

    flag = True
    for i in right_input_list:
        if not i:
            flag = False
    flag_input = flag
    right_input_list.clear()

    return flag_input

def get_sum(dictionary, text):
    sum = 0
    for i in text:
        for item in dictionary:
            if i.upper() == item:
                sum += int(dictionary[item])
    return sum

l1_en = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
l2_en = ['D', 'G']
l3_en = ['B', 'C', 'M', 'P']
l4_en = ['F', 'H', 'V', 'W', 'Y']
l5_en = ['K']
l8_en = ['J', 'X']
l10_en = ['Q', 'Z']
l_en = [l1_en, l2_en, l3_en, l4_en, l5_en, l8_en, l10_en]
d_en = {}
create_dict(d_en, l_en)

l1_ru = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
l2_ru = ['Д', 'К', 'Л', 'М', 'П', 'У']
l3_ru = ['Б', 'Г', 'Ё', 'Ь', 'Я']
l4_ru = ['Й', 'Ы']
l5_ru = ['Ж', 'З', 'Х', 'Ц', 'Ч']
l8_ru = ['Ш', 'Э', 'Ю']
l10_ru = ['Ф', 'Щ', 'Ъ']
l_ru = [l1_ru, l2_ru, l3_ru, l4_ru, l5_ru, l8_ru, l10_ru]
d_ru = {}
create_dict(d_ru, l_ru)

while True:
    text = input('Напишите слово: ')
    check_en = check_right_input(d_en, text)
    check_ru = check_right_input(d_ru, text)
    if not check_en and not check_ru:
        print('Слово может содержать либо только английские, либо только русские буквы.')
    else:
        break

if check_en:
    result = get_sum(d_en, text)
else:
    result = get_sum(d_ru, text)

print(f'Стоимость введённого слова равна {result}')
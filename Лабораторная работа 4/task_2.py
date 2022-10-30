# процентное соотношение в п. 5 считается относительно букв в полученном словаре
# словарь с буквами не сортируется

def get_count_char(str_):
    str_ = "".join(main_str.split())  # избавляемся от пробелов
    str_ = str_.lower()  # переводим в нижний регистр
    for char in str_:
        if char.isalpha():  # если буква, то...
            if char in dict_:
                dict_[char] += 1  # добавляем в словарь
            else:
                dict_[char] = 1
    return dict_


def frequency(char_dict):
    char_sum = sum(dict_.values())  # Суммируем количество всех букв в словаре dict_ (257)
    PERCENT_CONST = 100
    for char in dict_:
        percent_dict[char] = round(dict_[char] / char_sum * PERCENT_CONST, 2)

    return percent_dict


dict_ = {}
percent_dict = {}
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))  # вывод по количеству
print(frequency(get_count_char(dict_)))  # вывод в процентах

# for letter_, count in letter_dict.items():
#     print(letter_, "-", count)  # вывод символов с количеством в столбик

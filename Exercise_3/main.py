"""Задача 20: В настольной игре Скрабл (Scrabble) каждая
буква имеет определенную ценность. Напишите программу,
которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое
содержит либо только английские, либо только русские буквы."""


import sys


class LanguageError(Exception):
    pass


eng_one_point_dict = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1,
                      "L": 1, "N": 1, "S": 1, "T": 1, "R": 1}
eng_two_points_dict = {"D": 2, "G": 2}
eng_three_points_dict = {"B": 3, "C": 3, "M": 3, "P": 3}
eng_four_points_dict = {"F": 4, "H": 4, "V": 4, "W": 4, "Y": 4}
eng_five_points_dict = {"K": 5}
eng_eight_points_dict = {"J": 8, "X": 8}
eng_ten_points_dict = {"Q": 10, "Z": 10}
full_eng_dict = {**eng_one_point_dict, **eng_two_points_dict,
                 **eng_three_points_dict, **eng_four_points_dict,
                 **eng_five_points_dict, **eng_eight_points_dict,
                 **eng_ten_points_dict}

rus_one_point_dict = {"А": 1, "В": 1, "Е": 1, "И": 1, "Н": 1,
                      "О": 1, "Р": 1, "С": 1, "Т": 1}
rus_two_points_dict = {"Д": 2, "К": 2, "Л": 2, "М": 2,
                       "П": 2, "У": 2}
rus_three_points_dict = {"Б": 3, "Г": 3, "Ё": 3, "Ь": 3, "Я": 3}
rus_four_points_dict = {"Й": 4, "Ы": 4}
rus_five_points_dict = {"Ж": 5, "З": 5, "Х": 5, "Ц": 5, "Ч": 5}
rus_eight_points_dict = {"Ш": 8, "Э": 8, "Ю": 8}
rus_ten_points_dict = {"Ф": 10, "Щ": 10, "Ъ": 10}
full_rus_dict = {**rus_one_point_dict, **rus_two_points_dict,
                 **rus_three_points_dict, **rus_four_points_dict,
                 **rus_five_points_dict, **rus_eight_points_dict,
                 **rus_ten_points_dict}


def count_points_of_word(word, lang, dict_rus, dict_eng):
    """The method counts points of each letter of user word"""
    points = 0
    if lang == "rus":
        for i in word:
            for j in dict_rus:
                if i == j:
                    points += dict_rus[j]
    else:
        for i in word:
            for j in dict_eng:
                if i == j:
                    points += dict_eng[j]
    return points


def testing_count_points_of_word(test_word="CONSEQUENCES", test_lang="eng"):
    """The method tests count_points_of_word method"""
    print("Testing of the \"count_points_of_word\" method has been launched...")
    expected = 25
    actual = count_points_of_word(test_word, test_lang, full_rus_dict, full_eng_dict)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_count_points_of_word()
print()


try:
    users_word = input("Enter your word: ").upper()
    count_rus = 0
    count_eng = 0
    for i in users_word:
        for j in full_rus_dict:
            if i == j:
                count_rus += 1
        for z in full_eng_dict:
            if i == z:
                count_eng += 1
    if count_rus != len(users_word) and count_eng != len(users_word):
        raise LanguageError("Mixed word or value entered! \nEnter a word ONLY in English "
                            "or ONLY in Russian, WITHOUT using other characters!")
except LanguageError as ex:
    print(ex)
    sys.exit()


print()
language = str
if count_rus == len(users_word):
    language = "rus"
else:
    language = "eng"

RESULT = count_points_of_word(users_word, language, full_rus_dict, full_eng_dict)
print(f"Congratulations! The word is written with a sort of enthusiasm! :)"
      f"\nYour word: {users_word} \nLanguage: {language} \nYour points: {RESULT}")

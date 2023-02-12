"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X."""


import sys


def fill_list_of_numbers(list, n):
    """The method fills empty list"""
    count = 1
    while count <= n:
        try:
            number = int(input(f"Enter number at index {count - 1}: "))
        except ValueError as ex:
            print(f"Error: {ex}")
            sys.exit()
        list.append(number)
        count += 1
    return list


def find_element_closest_in_value(list, n, minimal_difference=sys.maxsize):
    """The method finds element closest in value to number \"n\""""
    closest_element = 0
    for i in list:
        if n - i < minimal_difference:
            closest_element = i
            minimal_difference = n - i
    return closest_element


def testing_find_element_closest_in_value(test_list=[1, 2, 3, 4, 5], test_n=6):
    """The method tests find_element_closest_in_value method"""
    print("Testing of the \"find_element_closest_in_value\" method has been launched...")
    expected = 5
    actual = find_element_closest_in_value(test_list, test_n)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_find_element_closest_in_value()
print()


try:
    number_of_elements = int(input("Enter number of elements: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


print()
list_of_numbers = []
filled_list_of_numbers = fill_list_of_numbers(list_of_numbers, number_of_elements)
print()


try:
    number_n = int(input("Enter your number \"n\": "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


RESULT = find_element_closest_in_value(filled_list_of_numbers, number_n)
print()
print(f"Tne list of numbers -> {filled_list_of_numbers} \n"
      f"Your number \"n\" -> {number_n} \n"
      f"The number closest in value to number \"n\" -> {RESULT}")

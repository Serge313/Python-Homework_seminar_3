"""Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]."""


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


def how_many_times_n_appears(list, n):
    """The method finds how many times \"n\" number appears in the list"""
    count = 0
    for i in list:
        if i == n:
            count += 1
    return count


def testing_how_many_times_n_appears(test_list=[5, 1, 6, 5, 9], test_n=5):
    """The method tests how_many_times_n_appears method"""
    print("Testing of the \"how_many_times_n_appears\" method has been launched...")
    expected = 2
    actual = how_many_times_n_appears(test_list, test_n)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_how_many_times_n_appears()
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


RESULT = how_many_times_n_appears(filled_list_of_numbers, number_n)
print()
print(f"Tne list of numbers -> {filled_list_of_numbers} \n"
      f"Your number \"n\" -> {number_n} \n"
      f"The number of times number \"n\" appears in the list -> {RESULT}")

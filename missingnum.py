__author__ = 'HP'


def convert(final_array):  # list to an integer
    num = int(''.join(map(str, final_array)))
    return num


def find_missing(first_array, second_array):  # finding the missing number

    if len(first_array) > len(second_array):
        final_array = list(set(first_array) - set(second_array))
        return convert(final_array)
    elif len(second_array) > len(first_array):
        final_array = list(set(second_array) - set(first_array))
        return convert(final_array)
    elif len(second_array) == 0 and len(first_array) == 0:
        return 0
    elif len(first_array) == len(second_array):
        return 0
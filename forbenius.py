# Isabella Gomez A15305555
# ECE143 HW7

import numpy as np
import math
import itertools

def solvefrob(coefs,b):
    '''
    This function takes in a list of positive integers and

    :param coefs: list of positive integers
    :param b: positive integer
    :return:
    '''

    # check that coefs is a list of positive ints
    assert type(coefs) == list
    for i in range(len(coefs)):
        assert type(coefs[i]) == int
        assert coefs[i] > 0

    # check that b is greater than 0
    assert type(b) == int
    assert b > 0

    '''combo_list=[]
    # get combinations
    for i in range(len(coefs)):
        combos = list(itertools.combinations(coefs, i+1))
        # adding all possible combinations of numbers
        for j in range(len(combos)):
            combo_list.append(combos[j])

    # see if they add to b
    list_to_format = []
    final_dict = {}
    index = 0
    for i in range(len(combo_list)):
        for j in range(len(combo_list[i])):
            pass
    print(combo_list)'''

    matching_numbers = []

    def recursion(subset):
        for number in coefs:
            if sum(subset + [number]) < b:
                recursion(subset + [number])
            elif sum(subset + [number]) == b:
                matching_numbers.append(subset + [number])

    recursion([])

    format_dict = {}
    format_list = []
    index = 0
    for i in range(len(matching_numbers)):
        unique_elems = list(set(matching_numbers[i]))
        for j in range(len(unique_elems)):
            for k in range(len(matching_numbers[i])):
                if matching_numbers[i][k] == unique_elems[j]:
                    index = index + 1
            format_dict[unique_elems[j]]=index
            index = 0
        format_list.append(format_dict)
        format_dict = {}

    # finalize the lists
    final_list = []
    for i in range(len(format_list)):
        key_list = list(format_list[i].keys())
        entry = [0] * (len(coefs))
        for j in range(len(coefs)):
            for k in range(len(key_list)):
                if key_list[k] == coefs[j]:
                    entry[j] = format_list[i][key_list[k]]
        final_list.append(entry)

    # get rid of repeated sequences
    unique_final_list = []
    final_list.sort()
    list(final_list for final_list, _ in itertools.groupby(final_list))
    for i in range(len(final_list)):
        if final_list[i] not in unique_final_list:
            unique_final_list.append(final_list[i])

    for j in range(len(unique_final_list)):
        unique_final_list[j] = tuple(unique_final_list[j])

    return unique_final_list



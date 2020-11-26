from itertools import *
def next_permutation(t:tuple)->tuple:
    '''
    This function will that a tuple and print our the next permutation

    :param t: tuple with list that will be permutated
    :return: tuple with next permutation
    '''

    # check that t is a tuple
    assert type(t) == tuple
    for i in range(len(t)):
        assert type(t[i]) == int
    # check for duplicates
    set_t = set(t)
    assert len(set_t) == len(t)

    # change t into a list
    list_t = list(t)

    # find next permutation
    found = False
    i = len(list_t) - 2
    # sort to find point where list[i] < list[i+1]
    while i >= 0:
        if list_t[i] < list_t[i + 1]:
            found = True
            break
        i = i - 1

    # if at end of permutation list return first one
    if not found:
        list_t.sort()
    else:
        max_index = findMaxIndex(i + 1, list_t, list_t[i])
        list_t[i], list_t[max_index] = list_t[max_index], list_t[i]
        list_t[i + 1:] = list_t[i + 1:][::-1]
    return tuple(list_t)

def findMaxIndex(index,my_list,curr_pos):
    ans = -1
    index = 0
    for i in range(index,len(my_list)):
       if my_list[i]>curr_pos:
          if ans == -1:
             ans = curr_pos
             index = i
          else:
             ans = min(ans,my_list[i])
             index = i
    return index

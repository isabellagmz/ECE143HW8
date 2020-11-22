# Isabella Gomez A15305555
# ECE143 HW7

import numpy as np
import math

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

    # make sure b has gcd with at least one of these numbers
    for i in range(b):
        pass

    return


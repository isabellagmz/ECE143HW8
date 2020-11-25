# Isabella Gomez A15305555
# ECE143 HW7

from forbenius import solvefrob
from water import get_trapped_water
from polinomial import Polynomial

class Homework8:
    def __init__(self):
        pass

if __name__ == '__main__':
    my_Homework8 = Homework8()
    some_list = [1,2,3,5]
    #print(solvefrob(some_list, 4))

    my_polinomial = Polynomial()

    print(solvefrob(some_list,10))

    '''p = Polynomial({0:8,1:2,3:4})
    q = Polynomial({0:8,1:2,2:8,4:4})

    #print(4*p +5 - 3*p -1)
    p = Polynomial({2: 1, 0: -1})
    q = Polynomial({1: 1, 0: -1})

    print(p/q)'''

    '''p = Polynomial({2: 1, 0: -1})
    q = Polynomial({1: 1, 0: -1})
    print(repr(p))
    print(repr(q))
    print(p/q)'''

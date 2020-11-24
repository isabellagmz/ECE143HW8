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
    some_list = [1,2,3,4]
    #print(solvefrob(some_list, 4))

    my_polinomial = Polynomial()
    p = Polynomial({0:8,1:2,3:4})
    q = Polynomial({0:8,1:2,2:8,4:4})

    '''print(repr(p))
    print(p*3)
    print(3*p)
    x = 3*p
    p = Polynomial({0: 8, 1: 2, 3: 4})
    print(p*4 + 5 - x - 1)
    print(p-p==0)
    print(p==q)'''
    #print(p.subs(10))
    '''p = Polynomial({0:8,1:0,3:4})'''

    p = Polynomial({2: 1, 0: -1})
    q = Polynomial({1: 1, 0: -1})
    print(repr(p))
    print(repr(q))
    print(p/q)

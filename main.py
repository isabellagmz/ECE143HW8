# Isabella Gomez A15305555
# ECE143 HW7

from forbenius import solvefrob
from water import get_trapped_water
from polinomial import Polynomial
from grid_path import count_paths
from permutation import next_permutation

class Homework8:
    def __init__(self):
        pass

if __name__ == '__main__':
    my_Homework8 = Homework8()

    p = Polynomial({0: 8, 1: 2, 3: 4})  # keys are powers, values are coefficients
    q = Polynomial({0: 8, 1: 2, 2: 8, 4: 4})

    print(repr(p))
    print(p * 3)  # integer multiply
    print(3 * p) # multiplication is commutative!
    print(p + q)  # add two polynomials
    print(p * 4 + 5 - 3 * p - 1)  # compose operations and add/subtract constants
    print(type(p - p))  # zero requires special handling but is still a Polynomial
    print(p * q)  # polynomial by polynomial multiplication works as usual
    print(p.subs(10))  # substitute in integers and evaluate
    print((p - p) == 0)
    print(p == q)

    p = Polynomial({0: 8, 1: 0, 3: 4})  # keys are powers, values are coefficients

    print(repr(p))

    p = Polynomial({2: 1, 0: -1})
    q = Polynomial({1: 1, 0: -1})

    print(p/q)
    print(p  / Polynomial({1:1,0:-3}))

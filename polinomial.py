class Polynomial(object):
    '''
    Class to solve polynomial problem
    '''

    def __init__(self, the_dict = None):
        self.the_dict = the_dict

    def __repr__(self):
        eq_str = ''
        had_prev = False

        # sort the dictionary
        dict_items = self.the_dict.items()
        sorted_items = sorted(dict_items)

        for key in range(len(sorted_items)):
            if sorted_items[key][0] == 0:
                eq_str = eq_str + str(sorted_items[key][1]) + ' '
                had_prev = True
                if sorted_items[key][1] == 0:
                    eq_str = ''
                    had_prev = False
            elif sorted_items[key][0] == 1:
                if sorted_items[key][1] != 0:
                    if had_prev:
                        eq_str = eq_str + '+ '
                    if sorted_items[key][1] != 1:
                        eq_str = eq_str + str(sorted_items[key][1]) + ' '
                    eq_str = eq_str + 'x '
                    had_prev = True
            else:
                if sorted_items[key][1] != 0:
                    if had_prev:
                        eq_str = eq_str + '+ '
                    eq_str = eq_str + str(sorted_items[key][1]) + ' x^(' + str(sorted_items[key][0]) + ') '
        eq_str = eq_str.strip()
        return eq_str

    def __mul__(self, other):
        for key in self.the_dict.keys():
            self.the_dict[key] = self.the_dict[key] * other
        return Polynomial(self.the_dict)

    def __rmul__(self, other):
        for key in self.the_dict.keys():
            self.the_dict[key] = self.the_dict[key] * other
        return Polynomial(self.the_dict)

    def __add__(self, other):
        # adding an integer
        if isinstance(other, int):
            if 0 in self.the_dict.keys():
                self.the_dict[0] = other + self.the_dict[0]
            else:
                self.the_dict[0] = other

        # adding a polynomial
        else:
            for key in list(self.the_dict.keys()):
                for key1 in list(other.the_dict.keys()):
                    if key == key1:
                        self.the_dict[key] = self.the_dict[key] + other.the_dict[key]
                    elif key1 not in self.the_dict.keys():
                        self.the_dict[key1] = other.the_dict[key1]
        return Polynomial(self.the_dict)

    def __sub__(self, other):
        # subtracting integer
        if isinstance(other, int):
            if 0 in self.the_dict.keys():
                self.the_dict[0] = self.the_dict[0] - other
            else:
                self.the_dict[0] = other
        # subtracting a polynomial
        else:
            for key in list(self.the_dict.keys()):
                for key1 in list(other.the_dict.keys()):
                    if key == key1:
                        self.the_dict[key] = self.the_dict[key] - other.the_dict[key]
                    elif key1 not in self.the_dict.keys():
                        self.the_dict[key1] = -other.the_dict[key1]

        return Polynomial(self.the_dict)

    def __rsub__(self, other):
        # make polynomial negative
        for key in list(self.the_dict.keys()):
            self.the_dict[key] = - self.the_dict[key]

        # subtracting integer
        if isinstance(other, int):
            if 0 in self.the_dict.keys():
                self.the_dict[0] = other + self.the_dict[0]
            else:
                self.the_dict[0] = other

        return Polynomial(self.the_dict)

    def __eq__(self, other):
        if other == 0 and self.__repr__() == '':
            return True
        if self.__repr__() == other.__repr__():
            return True
        return False

    def __truediv__(self, other):

        return 0

    def subs(self, sub_int):
        total = 0
        for key in list(self.the_dict.keys()):
            mult = (sub_int ** key) * self.the_dict[key]
            total = total + mult

        return total

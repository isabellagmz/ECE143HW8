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
        new_dict={}

        #integer multiplication
        if isinstance(other, int):
            for key in self.the_dict.keys():
                new_dict[key] = self.the_dict[key] * other
        # polynomial multiplication
        else:
            for key in list(self.the_dict.keys()):
                for key1 in list(other.the_dict.keys()):
                    mult = self.the_dict[key] * other.the_dict[key1]
                    mult_degree = key + key1
                    # check if degree already in store
                    degree_list = list(new_dict.keys())
                    if mult_degree in degree_list:
                        new_dict[mult_degree] = new_dict[mult_degree] + mult
                    else:
                        new_dict[mult_degree] = mult
        return Polynomial(new_dict)

    def __rmul__(self, other):
        new_dict = {}
        for key in self.the_dict.keys():
            new_dict[key] = self.the_dict[key] * other
        return Polynomial(new_dict)

    def __add__(self, other):
        new_dict = {}
        #populate new dict with self values
        for key in list(self.the_dict.keys()):
            new_dict[key] = self.the_dict[key]

        # adding an integer
        if isinstance(other, int):
            if 0 in self.the_dict.keys():
                new_dict[0] = other + self.the_dict[0]
            else:
                new_dict[0] = other

        # adding a polynomial
        else:
            for key in list(new_dict.keys()):
                for key1 in list(other.the_dict.keys()):
                    if key == key1:
                        new_dict[key] = self.the_dict[key] + other.the_dict[key]
                    elif key1 not in new_dict.keys():
                        new_dict[key1] = other.the_dict[key1]
        return Polynomial(new_dict)

    def __sub__(self, other):
        new_dict = {}

        # populate new dict with self values
        for key in list(self.the_dict.keys()):
            new_dict[key] = self.the_dict[key]

        # subtracting integer
        if isinstance(other, int):
            if 0 in new_dict.keys():
                new_dict[0] = self.the_dict[0] - other
            else:
                new_dict[0] = other

        # subtracting a polynomial
        else:
            for key in list(new_dict.keys()):
                for key1 in list(other.the_dict.keys()):
                    if key == key1:
                        new_dict[key] = self.the_dict[key] - other.the_dict[key]
                    elif key1 not in new_dict.keys():
                        new_dict[key1] = -other.the_dict[key1]

        return Polynomial(new_dict)

    def __rsub__(self, other):
        new_dict = {}
        # make polynomial negative
        for key in list(self.the_dict.keys()):
            new_dict[key] = - self.the_dict[key]

        # subtracting integer
        if isinstance(other, int):
            if 0 in new_dict.keys():
                new_dict[0] = other + self.the_dict[0]
            else:
                new_dict[0] = other

        return Polynomial(new_dict)

    def __eq__(self, other):
        if other == 0 and self.__repr__() == '':
            return True
        if self.__repr__() == other.__repr__():
            return True
        return False

    def __truediv__(self, other):
        new_dict={}

        # check it is not dividing by zero
        if other.__repr__() == '':
            return 'Division by zero'

        # integer division
        if isinstance(other, int):
            return 'other is int'

        # find degree of denominator
        deg_den = max(list(other.the_dict.keys()))
        deg_num = max(list(self.the_dict.keys()))

        # if there is a remainder, do not implement
        if deg_num < deg_den:
            return NotImplemented

        # implementing long polynomial division
        new_denom = self
        new_num = {}

        for key in list(new_denom.the_dict.keys()):
            for key1 in list(other.the_dict.keys()):
                # get value and degree of next element
                #if new_denom.the_dict[key] % other.the_dict[key1] != 0:
                    #return NotImplemented
                div = int(new_denom.the_dict[key] / other.the_dict[key1])
                div_degree = key - key1

                # append to temp dict and final dict
                new_num[div_degree] = div #makes the new number to return
                new_dict[div_degree] = div

                # subraction
                temp_subtraction = Polynomial.__mul__(Polynomial(new_num), other)
                print('temp_sub:')
                print(temp_subtraction.__repr__())
                if temp_subtraction.__repr__() == '':

                    return Polynomial(new_dict)

                new_denom = Polynomial.__sub__(self, temp_subtraction)
                print('new_denom:')
                print(new_denom)
                new_num = {}

            break

        return Polynomial(new_dict)

    def subs(self, sub_int):
        total = 0
        for key in list(self.the_dict.keys()):
            mult = (sub_int ** key) * self.the_dict[key]
            total = total + mult

        return total
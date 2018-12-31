'''
A submodule for enabling dimensional analysis on
various physics results.
'''

from enum import Enum
from fractions import Fraction

class Units:
    A = 2
    cd = 3
    K = 5
    kg = 7
    m = 11
    mol = 13
    s = 17

    values = [A, cd, K, kg, m, mol, s]
    names = {A:   'A',
             cd:  'cd',
             K:   'K',
             kg:  'kg',
             m:   'm',
             mol: 'mol',
             s:   's'}

    def name(self, value):
        return self.names[value]

    def get_units(self, x):
        results = []
        for value in self.values:
            while x % value == 0:
                x /= value
                results.append(value)

        return results

UNITS = Units()


class Dimensional:

    def __init__(self, value, units):
        
        self.value = value

        frac = Fraction(units).limit_denominator()
        self.units_num = frac.numerator
        self.units_denom = frac.denominator

    def __str__(self):
        num_factors = UNITS.get_units(self.units_num)
        denom_factors = UNITS.get_units(self.units_denom)

        num_string = "".join([UNITS.name(x) for x in num_factors])
        denom_string = "/" + "/".join([UNITS.name(x) for x in denom_factors])

        if denom_string == "/":
            return "{} {}".format(self.value, num_string)

        return "{} {}{}".format(self.value, num_string, denom_string)

    def __add__(self, other):
        if self.units_num == other.units_num and self.units_denom == other.units_denom:
            return Dimensional(self.value + other.value,
                self.units_num / self.units_denom)

        raise Exception("{} and {} have different units".format(self, other))

    def __sub__(self, other):
        if self.units_num == other.units_num and self.units_denom == other.units_denom:
            return Dimensional(self.value + other.value,
                self.units_num / self.units_denom)

        raise Exception("{} and {} have different units".format(self, other))


if __name__ == "__main__":
    time_0 = Dimensional(3, UNITS.s)
    time_1 = Dimensional(5, UNITS.s)

    vel_0 = Dimensional(2, UNITS.m / UNITS.s)
    vel_1 = Dimensional(5, UNITS.m / UNITS.s)

    super_time = time_0 + time_1
    print(super_time, vel_0)
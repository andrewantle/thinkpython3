'''
Creating a New Data Type

Think Python - Appendix B:
<http://www.greenteapress.com/thinkpython/thinkCSpy/html/app02.html>
'''

DEBUG = True


class Fraction(object):
    '''A fraction class, consisting of a numerator and denominator.'''

    def __init__(self, numerator, denominator=1):
        '''Initialize a new fraction.'''
        gcd = greatest_common_divisor(numerator, denominator)
        self.numerator = numerator / gcd
        self.denominator = denominator / gcd   # Reduced!

    def __str__(self):
        '''Return the string representation of this instance.'''
        return "%d/%d" % (self.numerator, self.denominator)

    def __add__(self, other):
        '''Add two fractions; A/B + C/D == (AD + BC)/(BD).'''
        result = None

        if isinstance(other, int):
            other = Fraction(other)

        product1 = self.numerator * other.denominator       # AD
        product2 = self.denominator * other.numerator       # BC
        numerator = product1 + product2                     # AD + BC
        denominator = self.denominator * other.denominator  # BD
        result = Fraction(numerator, denominator)           # (AD + BC)/(BD)

        return result

    # A + B == B + A; 4 + Fraction(5, 6) == Fraction(5, 6) + 4
    __radd__ = __add__

    def __mul__(self, other):
        '''Multiply two fractions.'''
        result = None

        if isinstance(other, int):
            other = Fraction(other)

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        result = Fraction(numerator, denominator)

        return result

    # AB == BA; 4 * Fraction(5, 6) == Fraction(5, 6) * 4
    __rmul__ = __mul__


def greatest_common_divisor(value1, value2):
    '''Find the greatest common divisor (GCD) of two integers.'''
    result = 0

    remainder = value1 % value2

    if remainder == 0:
        result = value2
    else:
        result = greatest_common_divisor(value2, remainder)

    return result

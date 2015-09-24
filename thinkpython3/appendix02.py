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
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        '''Return the string representation of this instance.'''
        return "%d/%d" % (self.numerator, self.denominator)

    def __mul__(self, other):
        '''Multiply two fractions.'''
        result = None

        if isinstance(other, int):
            other = Fraction(other)

        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        result = Fraction(numerator, denominator)

        return result

    # ab == ba; 4 * Fraction(5, 6) == Fraction(5, 6) * 4
    __rmul__ = __mul__

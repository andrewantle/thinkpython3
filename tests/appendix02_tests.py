from nose.tools import *
from thinkpython3.appendix02 import *


def setup():
    print("SETUP!")


def teardown():
    print("TEARDOWN!")


def test_fraction():
    '''Test the Fraction class.'''
    fraction = Fraction(5, 6)

    if DEBUG:
        print(fraction)

    assert fraction.numerator == 5
    assert fraction.denominator == 6

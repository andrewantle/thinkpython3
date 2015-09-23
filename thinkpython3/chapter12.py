'''
Classes and Objects

Think Python - Chapter 12:
    <http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap12.html>
'''


class Point(object):
    '''This class is an example of operator overloading.'''

    def __init__(self, x=0, y=0):
        '''Initialize a new point.'''
        self.x = x
        self.y = y

    def __str__(self):
        '''Return the string representation of this instance.'''
        return '<Point (%s, %s)>' % (self.x, self.y)

    def __add__(self, other):
        '''Overload the `+` operator.'''
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''Overload the `-` operator.'''
        return Point(self.x - other.x, self.y - other.y)


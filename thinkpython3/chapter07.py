'''
Strings

Think Python - Chapter 7:
<http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap07.html>
'''


def find_first_index(source, to_find, start=0):
    '''Find the first index of the character to find in the source string,
    starting from 0 by default.

    >>> source = "I Love Star Trek"
    >>> find_first_index(source, 'o')
    3
    >>> find_first_index(source, 'z')
    -1
    >>> find_first_index("", 'x')
    -1
    >>> find_first_index(source, 'e', 6)
    14
    >>> find_first_index(source, 'o', "Hola")
    3
    '''
    to_find_index = -1
    stop = len(source) - 1

    # Boundary check
    start, stop = boundary_check(start, stop)

    for index in range(start, stop):
        if source[index] == to_find:
            to_find_index = index
            break   # Found it, stop searching

    return to_find_index


def boundary_check(start, stop):
    '''Boundary check the start and stop parameters.

    >>> boundary_check(-100, -200)
    (0, 0)
    '''
    if not isinstance(start, int):
        try:
            start = int(start)
        except ValueError:
            start = 0
    if start < 0:
        start = 0
    if stop < 0:
        stop = 0
    if start > stop:
        start = stop

    return start, stop

'''
Functions

From a newer version of Think Python - Chapter 3: 
    <http://www.greenteapress.com/thinkpython/html/thinkpython004.html>

Exercise 5: 2x2 grid

>>> main()
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
'''


def main():
    '''This is where the program begins.'''
    print_grid()


def print_grid():
    '''Print two rows, then print the beams.'''
    do_two(print_row)
    print_beams()


def do_two(f):
    '''Execute the given function two times.'''
    f()
    f()


def print_row():
    '''Print the beams, then print four sets of posts.'''
    print_beams()
    do_four(print_posts)


def print_beams():
    '''Print two sets of beams, then print a final `+`.'''
    do_two(print_beam)
    print('+')


def print_beam():
    '''Print a beam.'''
    print('+ - - - -', end='')


def do_four(f):
    '''Execute the given function four times.'''
    do_two(f)
    do_two(f)


def print_posts():
    '''Print two sets of posts, then a final `|`.'''
    do_two(print_post)
    print('|')


def print_post():
    '''Print a post.'''
    print('|        ', end='')


if __name__ == '__main__':
    main()

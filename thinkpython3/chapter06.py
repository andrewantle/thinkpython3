'''
Iteration

Think Python - Chapter 6:
    <http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap06.html>
'''

from time import sleep


def main():
    '''This is where the program begins.'''
    countdown(10)
    print_times_table(20)


def countdown(number):
    '''Iterate from the given number to zero, then print "Blastoff!".'''
    if number < 0:
        number = 0

    # Use a `while` loop when you don't know the start, stop, and/or step.
    #
    # For example:
    # number = input('Please enter a positive integer: ')
    # while number > 0:
    #     print('%d...' % number)
    #     sleep(1)
    #     number -= 1
    
    # We know the start, stop, and step, so a `for` loop is the
    # right tool for the job.
    start = number
    stop = 0
    step = -1

    for index in range(start, stop, step):
        print('%d...' % index)
        sleep(1)
    print('Blastoff!')


def print_times_table(number):
    '''Iterate from 1 up to the given number, printing the times table.'''
    if number < 0:
        number = 0

    stop = number + 1

    for row in range(1, stop):
        # for column in range(1, stop):   # Full
        for column in range(1, row + 1):  # Half
            cell = row * column
            print('%4d' % cell, end='')
        print()


if __name__ == '__main__':
    main()

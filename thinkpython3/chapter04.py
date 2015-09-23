'''
Conditionals and Recursion

Think Python - Chapter 4:
<http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap04.html>
'''

from time import sleep


count = {'iteration': 0}


def main():
    '''This is where the program begins.'''
    countdown(10)
    recurse()


def countdown(number):
    '''Recurse from number to zero, then print "Blastoff!"'''
    if number == 0:
        print('Blastoff!')
    else:
        print(number)
        sleep(1)
        countdown(number - 1)


def recurse():
    '''Test the maximum recursion depth.'''
    count['iteration'] += 1
    print('Count: %d' % count['iteration'])
    recurse()


if __name__ == '__main__':
    main()

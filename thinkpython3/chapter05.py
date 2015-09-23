'''
Fruitful Functions

Think Python - Chapter 5:
<http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap05.html>
'''


def main():
    '''This is where the program begins.'''
    result = factorial(5)
    print(result)
    assert result == 120

    result = fibonacci(10)
    print(result)
    assert result == 89

    result = fibonacci('Bob')
    print(result)
    assert result == -1


def factorial(number):
    '''Determine the factorial of a number; e.g., 5! == 120.

    >>> factorial(5)
    120
    '''
    result = 1

    if number > 0:
        result = number * factorial(number - 1)

    return result


def factorial_verbose(number):
    '''Determine the factorial of a number; mouthier.'''
    result = 1
    print('number: %d' % number)

    if number > 0:
        print('result = %d * factorial(%d)' % (number, number - 1))
        result = n * factorial(n - 1)
        print('result: %d' % result)

    return result


def fibonacci(number):
    '''Determine the fibonacci value of a number; e.g., f(10) == 55.

    >>> fibonacci(10)
    55
    '''
    result = -1

    if is_valid_data(number):
        if number == 0 or number == 1:
            result = 1
        else:
            result = fibonacci(number - 1) + fibonacci(number - 2)

    return result


def is_valid_data(number):
    '''Determine whether or not the data is valid.'''
    result = True
    message = '==> Please correct the following error(s):\n'

    if not isinstance(number, int):
        result = False
        message += '-number must be an integer\n'
    elif number < 0:
        result = False
        message += '-number must not be negative\n'

    if not result:
        print(message)

    return result


if __name__ == '__main__':
    main()

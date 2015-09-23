from nose.tools import *
from thinkpython3.chapter20 import *


def setup():
    print("SETUP!")



def teardown():
    print("TEARDOWN!")



def test_tree():
    '''Test the Tree class.'''
    left = Tree(2)
    right = Tree(3)
    tree = Tree(1, left, right)

    if DEBUG:
        print(tree)
        print(tree.left)
        print(tree.right)

    assert tree.cargo == 1
    assert tree.left.cargo == 2
    assert tree.right.cargo == 3



def test_total():
    '''Test the total function.'''
    left = Tree(2)
    right = Tree(3)
    tree = Tree(1, left, right)
    result = total(tree)

    if DEBUG:
        print(result)

    assert result == 6



def test_display():
    '''Test the display_* functions.'''
    tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))  # 1 + 2 * 3 == 7

    if DEBUG:
        display_prefix(tree)    # + 1 * 2 3
        print()
        display_postfix(tree)   # 1 2 3 * +
        print()
        display_infix(tree)     # 1 + 2 * 3
        print()
        display_indented(tree)
        print()



def test_get_token_list():
    '''Test the get_token_list function.'''
    expression = '(3+7)*9'
    token_list = get_token_list(expression)

    if DEBUG:
        print(expression)
        print(token_list)
    
    # Build up the tests little by little
    # assert token_list == []
    # assert token_list == ['end']
    # assert token_list == ['(', '3', '+', '7', ')', '*', '9', 'end']
    assert token_list == ['(', 3, '+', 7, ')', '*', 9, 'end']



def test_get_token():
    '''Test the get_token function.'''
    expression = '(3+7)*9'
    token_list = get_token_list(expression)

    if DEBUG:
        print(token_list)

    # Remove the first token
    result = get_token(token_list, '(')
    assert result

    if DEBUG:
        print(token_list)

    assert token_list == [3, '+', 7, ')', '*', 9, 'end']

    # Try to get a token that's not there
    result = get_token(token_list, 'A')
    assert not result

    # Remove all tokens
    for token in [3, '+', 7, ')', '*', 9, 'end']:
        result = get_token(token_list, token)

        if DEBUG:
            print(token)
            print(token_list)
            print(result)

        assert result

    assert token_list == []



def test_get_token_from_empty_list():
    '''Test the get_token function on an empty list.'''
    token_list = []

    # Try to get a token from an empty list
    result = get_token(token_list, 'ABC')
    assert not result



def test_get_number():
    '''Test the get_number function.'''
    token_list = [9, 11, 'end']
    token = get_number(token_list)

    if DEBUG:
        print(token_list)
        print(token)

    assert isinstance(token, Tree)
    assert token.cargo == 9



def test_get_product():
    '''Test the get_product function.'''

    # Simple product
    token_list = [9, '*', 11, 'end']
    tree = get_product(token_list)

    if DEBUG:
        display_postfix(tree)
        print()

    # Not a product
    token_list = [9, '+', 11, 'end']
    tree = get_product(token_list)

    if DEBUG:
        display_postfix(tree)
        print()

    # Arbitrarily long product
    token_list = [2, '*', 3, '*', 5, '*', 7, 'end']
    tree = get_product(token_list)

    if DEBUG:
        display_infix(tree)
        print()



def test_get_sum():
    '''Test the get_sum function.'''
    token_list = [9, '*', 11, '+', 5, '*', 7, 'end']
    tree = get_sum(token_list)

    if DEBUG:
        display_infix(tree)
        print()

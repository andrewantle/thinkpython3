'''
Trees

Think Python - Chapter 20:
    <http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap20.html>

A tree is either:

-   the empty tree, represented by `None`, or
-   a node that contains an object reference (`cargo`)
    and two tree references (`left` and `right`).
'''

DEBUG = False


class Tree(object):
    '''A binary tree implementation.'''

    def __init__(self, cargo, left=None, right=None):
        '''Initialize a new empty tree.'''
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        '''Return the string representation of this instance.'''
        return str(self.cargo)


def total(tree):
    '''Total the values of the tree.'''
    result = 0

    if tree is not None:
        result = tree.cargo + total(tree.left) + total(tree.right)

    return result


def display_prefix(tree):
    '''Preorder traverse the tree and display the contents. (+ 3 7)'''
    if tree is not None:
        print(tree.cargo, end=' ')      # First
        display_prefix(tree.left)
        display_prefix(tree.right)


def display_postfix(tree):
    '''Postorder traverse the tree and display the contents. (3 7 +)'''
    if tree is not None:
        display_postfix(tree.left)
        display_postfix(tree.right)
        print(tree.cargo, end=' ')      # Last


def display_infix(tree):
    '''Inorder traverse the tree and display the contents. (3 + 7)'''
    if tree is not None:
        display_infix(tree.left)
        print(tree.cargo, end=' ')      # Middle
        display_infix(tree.right)


def display_indented(tree, level=0):
    '''Generate a graphical representation of the tree, indented by level.'''
    if tree is not None:
        display_indented(tree.right, level + 1)
        print('\t' * level + str(tree))
        display_indented(tree.left, level + 1)


def get_token_list(expression):
    '''Get the token list from an expression string.'''
    token_list = []

    for token in expression:

        if token in '0123456789':
            token = int(token)
        token_list.append(token)

    token_list.append('end')    # Easier to parse

    return token_list


def get_token(token_list, expected):
    '''If the first token is what we expected, remove it from the list.'''
    result = False

    if token_list != []:

        if token_list[0] == expected:
            del token_list[0]
            result = True

    return result


def get_number(token_list):
    '''If the next token in the token list is a number, remove it and
    return a leaf node containing the number; otherwise, return None.
    '''
    result = None

    if token_list != []:

        if get_token(token_list, '('):
            result = get_sum(token_list)    # Get the subexpression
            get_token(token_list, ')')
        else:
            token = token_list[0]

            if isinstance(token, int):
                #del token_list[0]      # This works, but I don't know why.
                token_list[0:1] = []    # Safer? replace instead of delete,
                result = Tree(token)    # token is by ref ==> token_list[0]

    return result


def get_product(token_list):
    '''Build an expression tree for products; e.g., 3 * 7.'''
    result = None
    operator = '*'

    left = get_number(token_list)

    if get_token(token_list, operator):
        right = get_product(token_list)
        result = Tree(operator, left, right)
    else:
        result = left   # x * 1 == x

    return result


def get_sum(token_list):
    '''Build an expression tree for sums; e.g., 3 + 7.
    A sum is a tree with a `+` at the root, a product on the left (x * 1),
    and a sum on the right.  This way, we can represent any expression
    as a sum of products.
    '''
    result = None
    operator = '+'

    left = get_product(token_list)

    if get_token(token_list, operator):
        right = get_sum(token_list)
        result = Tree(operator, left, right)
    else:
        result = left   # x * 1 == x

    return result

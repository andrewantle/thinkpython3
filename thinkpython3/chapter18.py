'''
Stacks

Think Python - Chapter 18:
<http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap18.html>
'''


class Stack(object):
    '''A Last In, First Out (LIFO) linked list implementation.'''

    def __init__(self):
        '''Initialize a new empty list.'''
        self.items = []

    def push(self, item):
        '''Add a new item to the end of the list.'''
        self.items.append(item)

    def pop(self):
        '''Remove and return an item from the list.
        The item that is returned is the last one that was added.
        '''
        return self.items.pop()

    def is_empty(self):
        '''Determine if the stack is empty.'''
        return self.items == []


def main():
    '''This is where the program begins.'''
    test_stack()


def test_stack():
    '''Test the Stack class.'''
    stack = Stack()
    stack.push(54)
    stack.push(45)
    stack.push('+')

    while not stack.is_empty():
        item = stack.pop()
        print(item, end=' ')

    print()


if __name__ == '__main__':
    main()

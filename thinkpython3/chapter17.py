'''
Linked Lists

Think Python - Chapter 17:
<http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap17.html>

A linked list is either:

-   the empty list, represented by `None`, or
-   a node that contains a cargo object and a reference to a linked list.
'''


# DEBUG
record = {'count': 0}


class Node(object):
    '''A node class containing cargo and a reference to the next node.'''

    def __init__(self, cargo=None, next=None):
        '''Initialize a new node.'''
        self.cargo = cargo
        self.next = next

    def __str__(self):
        '''Return the string representation of this instance.'''
        return str(self.cargo)

    def print_backward(self):
        '''Print the linked list of nodes backward.'''
        if self.next is not None:
            tail = self.next
            tail.print_backward()

        print(self.cargo, end='')


class LinkedList(object):
    '''A linked list class containing a sequence of connected nodes.'''

    def __init__(self):
        '''Initialize a new linked list.'''
        self.head = None
        self.length = 0

    def add_first(self, cargo):
        '''Add a node to the head of the list.'''
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

    def print_backward(self):
        '''Print this list backward.'''
        print('[', end='')

        if self.head:
            self.head.print_backward()

        print(']')


def print_list(node):
    '''Print a list.'''
    print('[', end='')

    while node is not None:
        print(node, end='')
        node = node.next
        if node is not None:
            print(', ', end='')

    print(']')


def print_backward(node):
    '''Print a list backward:
    1. Separate the list into two pieces:
       a. the first node (head), and
       b. the rest (tail)
    2. Print the tail backward
    3. Print the head
    '''
    if node is not None:
        print('Node: %s' % node)
        record['count'] += 1
        print('Count: %d' % record['count'])

        head = node
        print('Head: %s' % head)
        
        tail = node.next
        print('Tail: %s' % tail)
        
        print('Calling print_backward...')
        print()
        print_backward(tail)
        
        print(head, end=', ')


def print_backward_nicely(node):
    '''Print a list backward, with pretty brackets.'''
    print('[', end='')
    print_backward(node)
    print(']')


def remove_second(node):
    '''Remove the second node in the list and return a reference to it.'''
    second = None

    '''
    From PEP 8:

        ...Beware of writing `if x` when you really mean
        `if x is not None`; e.g., when testing whether a
        variable or argument that defaults to `None` was
        set to some other value. The other value might have a
        type (such as a container) that could be false
        in a boolean context!
    '''
    # So use this instead of only `if node:`.
    if node is not None:
        first = node
        second = node.next
        if second is not None:
            first.next = second.next
            second.next = None

    return second


def main():
    '''This is where the program begins.'''
    # test1()
    test2()
    # test3()
    # node = Node()
    # print(type(node))
    # linked_list = LinkedList()
    # print(type(linked_list))


def test1():
    '''Test the Node class with integer cargo.'''
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    print_list(node1)

    #print_backward(node1)
    
    removed = remove_second(node1)
    print_list(removed)
    print_list(node1)
    
    removed2 = remove_second(removed)
    print_list(removed2)
    
    print('Record - Count: %d' % record['count'])
    print_backward_nicely(node1)
    print('Record - Count: %d' % record['count'])


def test2():
    '''Test the Node class with string cargo.'''
    node1 = Node('Curling')
    node2 = Node('Soccer')
    node3 = Node('Moose')
    node1.next = node2
    node2.next = node3
    print_backward(node1)
    print()


def test3():
    '''Test the LinkedList class.'''
    linked_list = LinkedList()


if __name__ == '__main__':
    main()

'''
Queues

Think Python - Chapter 19:
    <http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap19.html>
'''

from thinkpython3.chapter17 import Node


class Queue:
    '''A First In, First Out (FIFO) linked list implementation.'''

    def __init__(self):
        '''Initialize a new empty list.'''
        self.head = None
        self.length = 0

    def push(self, item):
        '''Add a new item to the list.'''
        node = Node(item)
        node.next = None

        if self.head is not None:
            last = self.head    # Find the last node

            while last.next is not None:
                last = last.next
            
            last.next = node    # Append the new node
        else:
            self.head = node    # The list is empty, so the new node goes first

        self.length += 1

    def pop(self):
        '''Remove and return an item from the list.
        The item that is returned is the first one that was added.
        '''
        cargo = self.head.cargo

        self.head = self.head.next
        self.length -= 1

        return cargo

    def is_empty(self):
        '''Check whether the list is empty.'''
        return self.length == 0


def main():
    '''This is where the program begins.'''
    test_queue()


def test_queue():
    '''Test the Queue class.'''
    queue = Queue()
    queue.push(54)
    queue.push(45)
    queue.push('+')

    while not queue.is_empty():
        item = queue.pop()
        print(item, end=' ')

    print()


if __name__ == '__main__':
    main()

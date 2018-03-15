
class Node(object):

    def __init__(self, cargo):
        self.previous = None
        self.next = None
        self.cargo = cargo

class Deque(object):

    def __init__(self, iterable=None):
        self.counter = 0
        self.head = None
        self.tail = None

        if iterable:
            for item in iterable:
                self.enqueue_back(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Deque({})'.format(self.length())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        return (self.counter == 0)

    def length(self):
        """Return the number of items in this stack"""
        return self.counter

    def peek_front(self):
        '''Return the first item in deque without removing it,
        or None if empty.'''
        if self.head is None:
            return None
        else:
            return self.head.cargo

    def peek_back(self):
        '''Return the last item in deque without removing it,
        or None if empty.'''
        if self.tail is None:
            return None
        else:
            return self.tail.cargo

    def enqueue_front(self, item):
        '''Push item onto front of deque.'''
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.counter = 1
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            self.counter += 1


    def enqueue_back(self, item):
        '''Push item onto back of deque.'''
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.counter = 1
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.counter += 1

    def dequeue_front(self):
        '''Pop item from front of deque.'''
        # Deque is empty
        if self.head is None:
            raise ValueError('Deque is empty!')
        else:
            cargo = self.head.cargo
            if self.counter == 1:
            # CASE:  Deque only has one Node
                self.head = None
                self.tail = None
            else:
                old_node = self.head
                self.head = old_node.next
                self.head.previous = None
                old_node.previous = None
                old_node.next = None
            self.counter -= 1
            return cargo

    def dequeue_back(self):
        '''Pop item from back of deque.'''
        # Deque is empty
        if self.head is None:
            raise ValueError('Deque is empty!')
        else:
            cargo = self.tail.cargo
            if self.counter == 1:
            # CASE:  Deque only has one Node
                self.head = None
                self.tail = None
            else:
                old_node = self.tail
                self.tail = old_node.previous
                self.tail.next = None
                old_node.previous = None
                old_node.next = None
            self.counter -= 1
            return cargo

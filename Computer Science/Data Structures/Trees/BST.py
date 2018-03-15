
class Node(object):


    def __init__(self, cargo):
        self.left_child = None
        self.right_child = None
        self.cargo = cargo

class Binary_Search_Tree(object):

    def __init__(self, iterable=None):
        self.root = None
        if iterable:
            for item in iterable:
                self.insert(item)

    def insert(self, item, node=None):
        # Start at the root if no node is passed in
        if node is None:
            node = self.root
        # CASE: Root is empty
        if self.root is None:
            self.root = Node(item)

        # CASE: Traverse to the left.  Duplicates will always go to the left
        elif item <= node.cargo:
            # If no child, insert new item as left child node
            if node.left_child is None:
                node.left_child = Node(item)
            # Otherwise, continue traversing to the left
            else:
                self.insert(item, node.left_child)

        # CASE: Traverse to the right
        elif item > node.cargo:
            if node.right_child is None:
                node.right_child = Node(item)
            else:
                self.insert(item, node.right_child)



    def search(self, item, node=None):
        pass


    def delete(self, item, node=None):
        pass

        # CASE:  Root Node


        # CASE: Leaf Node

        # CASE:  Branch Node--replace with leftmost child on right, or rightmost child on left

    def in_order_traversal(self, node=None, accumulator=None):
        if accumulator is None:
            accumulator = []
            node = self.root

        if node is None:
            return accumulator

        if node.left_child is not None:
            self.in_order_traversal(node.left_child, accumulator)

        accumulator.append(node.cargo)

        if node.right_child is not None:
            self.in_order_traversal(node.right_child, accumulator)

        return accumulator


    def pre_order_traversal(self, node=None, accumulator=None):
        if node is None:
            node = self.root

        if accumulator is None:
            tree_contents = []

        tree_contents.append(node.cargo)
        self.in_order_traversal(node.left_child, tree_contents)
        self.in_order_traversal(node.right_child, tree_contents)

    def post_order_traversal(self, node=None, accumulator=None):
        if node is None:
            node = self.root

        if accumulator is None:
            tree_contents = []

        self.in_order_traversal(node.left_child, tree_contents)
        self.in_order_traversal(node.right_child, tree_contents)
        tree_contents.append(node.cargo)


        return tree_contents

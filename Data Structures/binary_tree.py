## Binary Tree Algorithm


Class Node():

    def __init__(self, cargo):
        self.cargo = cargo
        self.left = None
        self.right = None


class Binary_Tree():

    def __init__(self):
        self.root = None
        self.count = 0

"""
TEST CASE:
        15
       /  \
      7   38
     /    / \
    4   22   44
   / \        \
  2   6       50
"""


    def add(self, data, node=None):
        """
            case:  Tree is empty.  Create node, set as root.
            case:  Tree is not empty. Traverse tree and set at correct spot.
            Traversal:

        """
        if self.root is None:
            newNode = Node(data)
            self.root = newNode
        else:
            #traverse until correct node is found.
            ...

    def _traverse(self, value, parent=self.root, node=None):
        """
            1.   Start at parent
            2a.  If node.cargo == value, return cargo.
            2a.  If value is less than root value, grab left child.
            2b.  If value is greater than root value, grab right child.
            3a.  If node is None, raise ValueError.
            3b.  If node exists, repeat recursive step.
        """
        if self.root is None:
            raise ValueError("This binary tree is empty!")

        currentNode = node

        if currentNode.cargo == value:
            return currentNode
        else:
            if value < currentNode.cargo:
                return traverse(value, currentNode.left)
            else:
                return traverse(value, currentNode.right)
-

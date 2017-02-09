from BST import Binary_Search_Tree
import pytest


def test_init_BST():
    """
         14
       /    \
      7      20
     / \     / \
    1   8   15  21
    """
    bst = Binary_Search_Tree([14, 7, 20, 1, 8, 15, 21])
    assert bst is not None
    assert bst.root.cargo == 14
    assert bst.root.left_child.cargo == 7
    assert bst.root.right_child.cargo == 20
    assert bst.root.left_child.left_child.cargo == 1
    assert bst.root.left_child.right_child.cargo == 8
    assert bst.root.right_child.left_child.cargo == 15
    assert bst.root.right_child.right_child.cargo == 21

def test_insert():
    bst = Binary_Search_Tree()
    bst.insert(14)
    assert bst.root.cargo == 14
    bst.insert(7)
    bst.insert(20)
    assert bst.root.left_child.cargo == 7
    assert bst.root.right_child.cargo == 20
    bst.insert(1)
    bst.insert(8)
    bst.insert(15)
    bst.insert(21)
    assert bst.root.left_child.left_child.cargo == 1
    assert bst.root.left_child.right_child.cargo == 8
    assert bst.root.right_child.left_child.cargo == 15
    assert bst.root.right_child.right_child.cargo == 21

def test_in_order_traversal():
    data = [14, 7, 20, 1, 8, 15, 21]
    bst = Binary_Search_Tree(data)
    in_order_tree_contents = bst.in_order_traversal()
    print(in_order_tree_contents)
    assert in_order_tree_contents == sorted(data)

def test_pre_order_traversal():
    pass

def test_post_order_traversal():
    pass

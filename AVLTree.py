# username - yiftahbaruch
# id1      - 214448300
# name1    - Yiftah Schlesinger
# id2      - 323832949
# name2    - Eitan Admoni

from __future__ import annotations

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @param key: key of your node
    @type value: any
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0
        self.BF = 0

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self) -> int or None:
        return self.key

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        return self.value

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self) -> AVLNode:
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self) -> AVLNode:
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self) -> AVLNode:
        return self.parent

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self) -> int:
        return self.height

    """returns the size of the subtree

    @rtype: int
    @returns: the size of the subtree of self, 0 if the node is virtual
    """

    def get_size(self) -> int:
        return self.size

    """ returns the BF of the subtree
    @:rtype: int
    """

    def get_BF(self) -> int:
        return self.BF

    def get_right_should_reverse (self, should_reverse=False):
        if should_reverse:
            return self.get_left()
        return self.get_right()

    def get_left_should_reverse (self, should_reverse=False):
        if should_reverse:
            return self.get_right()
        return self.get_left()

    def set_right_should_reverse (self, node, should_reverse=False):
        if should_reverse:
            self.set_left(node)
        else:
            self.set_right(node)
    def set_left_should_reverse (self, node, should_reverse=False):
        if should_reverse:
            self.set_right(node)
        else:
            self.set_left(node)

    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key
        return None

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value
        return None

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node: AVLNode):
        self.left = node
        node.set_parent(self)
        return None

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node: AVLNode):
        self.right = node
        node.set_parent(self)
        return None

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node: AVLNode):
        self.parent = node
        return None

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h
        return None

    """sets the size of node

    @type s: int
    @param s: the size
    """

    def set_size(self, s):
        self.size = s
        return None

    """sets the BF of the node
    @type bf: int
    """

    def set_BF(self, bf):
        self.BF = bf

    def update_size(self):
        if not self.is_real_node():
            self.set_size(0)
        else:
            self.set_size(self.get_left().get_size() + self.get_right().get_size())

    def update_height(self):
        self.set_height(max(self.get_right().get_height(), self.get_left().get_height()) + 1)

    def update_BF(self):
        self.set_BF(self.get_left().get_height() - self.get_right().get_height())

    """Update properties of node
    Requirements: children's properties are updated
    """

    def update(self):
        self.update_size()
        self.update_height()
        self.update_BF()

    """
    returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        if self.get_key() is None:
            return False
        return True


    def is_right_child(self):
        return self.get_parent().get_right() == self


    """
    Creates a virtual node with a parent
    
    @type parent: AVLNode or None
    @rtype: AVLNode
    """

    @staticmethod
    def create_virtual_node():
        node = AVLNode(None, None)
        return node

    """find successor of the node
    
    @rtype: AVLNode
    """

    def find_successor(self) -> AVLNode | None:
        if self.get_right().is_real_node():
            current_node = self.get_right()
            while current_node.is_real_node():
                current_node = current_node.get_left()
            return current_node.get_parent()
        key = self.get_key()
        parent = self.get_parent()
        while parent.is_real_node() and parent.get_key() < key:
            parent = parent.get_parent()
        if not parent.is_real_node():
            return None
        return parent


R = 0
L = 1
RL = 2
LR = 3

"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = AVLNode.create_virtual_node()
        self.root.set_right(AVLNode.create_virtual_node())
        self.min = self.root

    # add your fields here

    """searches for a node in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: node corresponding to key.
    """

    def search(self, key):
        crnt_node = self.get_root()  # type: AVLNode
        while crnt_node.is_real_node():
            dif = key - crnt_node.get_key()
            if dif == 0:  # current node is the one searched for
                return crnt_node
            if dif > 0:  # bigger goes right, smaller goes left
                crnt_node = crnt_node.get_right()
            else:
                crnt_node = crnt_node.get_left()
        return None

    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, key, val):
        if not self.get_root().is_real_node():
            node = AVLNode(key, val)
            node.set_right(AVLNode.create_virtual_node())
            node.set_left(AVLNode.create_virtual_node())
            node.update()
            self.set_root(node)
            self.min = self.get_root()
            return 0
        current_node = self.get_root()
        while current_node.is_real_node():
            if current_node.get_key() > key:
                current_node = current_node.get_left()
            else:
                current_node = current_node.get_right()
        current_node.set_key(key)
        current_node.set_value(val)
        current_node.set_left(AVLNode.create_virtual_node())
        current_node.set_right(AVLNode.create_virtual_node())
        current_node.update()
        if self.min.get_key() > current_node.get_key():
            self.min = current_node
        return self.balance(current_node)

    @staticmethod
    def basic_roll(node: AVLNode, is_left_roll=False):
        rootParent = node.get_parent()
        leftChild = node.get_left_should_reverse(is_left_roll)
        leftRightChild = leftChild.get_right_should_reverse(is_left_roll)
        node.set_right_should_reverse(leftRightChild, is_left_roll)
        node.update()
        leftChild.set_right_should_reverse(leftChild, is_left_roll)
        leftChild.update()
        if node.is_right_child():
            rootParent.set_right(leftChild)
        else:
            rootParent.set_left(leftChild)
        rootParent.update()

    """Perform a basic roll operation
    @:param node: the root node of the roll
    For example, roll right is for the case:
    A->((B->(C)) becomes B->(C, A)
    Returns the new root node of the subtree
    """

    @staticmethod
    def roll(node: AVLNode, direction: int):
        if direction in (R, L):
            left_roll = direction == L
            AVLTree.basic_roll(node, is_left_roll=left_roll)
            return 1
        elif direction == RL:
            AVLTree.roll(node.right, R)
            AVLTree.roll(node, L)
        else:
            AVLTree.roll(node.left, L)
            AVLTree.roll(node, R)
        return 2

    @staticmethod
    def calcNeededRoll(node: AVLNode):
        if node.get_BF() == -2:
            if node.get_right().get_BF() <= 0:
                return L
            return RL
        if node.get_left().get_BF() >= 0:
            return R
        return LR

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node : AVLNode):
        parent = node.get_parent()
        toBalance = parent
        if node.get_right().is_real_node() and node.get_left().is_real_node():
            successor = node.find_successor()
            newKey, newValue = successor.get_key(), successor.get_value()
            succParent = successor.get_parent()
            succParent.set_left(AVLNode.create_virtual_node())  # successor is always a left son
            node.set_key(newKey)
            node.set_value(newValue)
            toBalance = succParent
        else:
            newNode = node.get_right()
            if not newNode.is_real_node():
                newNode = node.get_left()
            if node.is_right_child():
                node.get_parent().set_right(newNode)
            else:
                node.get_parent().set_left(newNode)
            parent.update()
        return self.balance(toBalance, True)

    def balance(self, node, is_delete=False):
        balance_number = 0
        parent = node.get_parent()
        while parent != self.root:
            previus_height = parent.get_height()
            parent.update()
            if abs(parent.get_BF()) == 2:
                if not is_delete:
                    return AVLTree.roll(parent, AVLTree.calcNeededRoll(parent))
                balance_number += AVLTree.roll(parent, AVLTree.calcNeededRoll(parent))
            elif previus_height == parent.get_height:
                break
            else:
                balance_number += 1
            parent = parent.get_parent()
        return balance_number

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        sorted_lst = []
        current_node = self.min
        for i in range(self.root.get_size()):
            sorted_lst += (current_node.get_key(), current_node.get_value())
            current_node = current_node.find_successor()
        return sorted_lst

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return self.get_root().get_size()

    """splits the dictionary at a given node

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):
        return None

    """joins self with key and another AVLTree

    @type tree: AVLTree 
    @param tree: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree are larger than key,
    or the other way around.
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined +1
    """

    def join(self, tree, key, val):
       return None

    """compute the rank of node in the self

    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary which we want to compute its rank
    @rtype: int
    @returns: the rank of node in self
    """

    def rank(self, node):
        rank = 0
        current_node = self.root
        while current_node.get_key() != node.get_key():
            if current_node.get_key() > node.get_key():
                current_node = current_node.get_left()
            else:
                rank += current_node.get_left().get_size() + 1
                current_node = current_node.get_right()
        rank += current_node.get_left().get_size()
        return rank

    """finds the i'th smallest item (according to keys) in self

    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: int
    @returns: the item of rank i in self
    """

    def select(self, i):
        rank = 0
        current_node = self.root
        while current_node.get_left().get_size() + rank != i:
            if current_node.get_left().get_size() < i:
                current_node = current_node.get_left()
            else:
                rank += current_node.get_left().get_size() + 1
                current_node = current_node.get_right()
        return current_node

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root.get_right()

    def set_root(self, node):
        self.root.set_right(node)



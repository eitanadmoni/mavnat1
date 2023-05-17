#username - yiftahbaruch
#id1      - 214448300
#name1    - Yiftah Schlesinger
#id2      - 323832949
#name2    - Eitan Admoni

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
	def set_left(self, node : AVLNode):
		self.left = node
		node.set_parent(self)
		return None

	def is_right_child (self):
		return self.get_parent().get_right() == self


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node : AVLNode):
		self.right = node
		node.set_parent(self)
		return None


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node : AVLNode):
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

	def update_size (self):
		if not self.is_real_node():
			self.set_size(0)
		else:
			self.set_size(self.get_left().get_size() + self.get_right().get_size())

	def update_height (self):
		self.set_size(max(self.get_right().get_size(), self.get_left().get_size()) + 1)

	def update_BF (self):
		self.set_BF(self.get_left().get_height() - self.get_right().get_height())

	"""Update properties of node
	Requirements: children's properties are updated
	"""
	def update (self):
		self.update_size()
		self.update_height()
		self.update_BF()




	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if(self.get_key() == None):
			return False
		return True

	"""
	Creates a virtual node with a parent
	
	@type parent: AVLNode or None
	@rtype: AVLNode
	"""
	@staticmethod
	def create_virtual_node(parent=None):
		node = AVLNode(None, None)
		node.set_parent(parent)
		return node


	"""find successor of the node
	
	@rtype: AVLNode
	"""
	def find_successor(self):
		current_node = self.get_right()
		while current_node.is_real_node():
			current_node = current_node.get_left()
		return current_node.get_parent()



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
		self.root = AVLNode(None, None)
		# add your fields here



	"""searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key.
	"""
	def search(self, key):
		crnt_node = self.get_root() # type: AVLNode
		while crnt_node.is_real_node():
			dif = key - crnt_node.get_key()
			if dif == 0: # current node is the one searched for
				return crnt_node
			if dif > 0: # bigger goes right, smaller goes left
				crnt_node = crnt_node.get_right()
			else:
				crnt_node = crnt_node.get_left()
		return crnt_node




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
		if self.root.is_real_node():
			self.root = AVLNode(key, val)
			self.root.set_size(1)
			self.root.set_height(0)
			self.root.set_right(AVLNode.create_virtual_node(self.root))
			self.root.set_left(AVLNode.create_virtual_node(self.root))
			self.root.set_BF(0)
			return 0
		else:
			current_node = self.root
			while current_node.is_real_node():
				if current_node.get_key() > key:
					current_node = current_node.get_left()
				else:
					current_node = current_node.get_right()
			current_node.set_key(key)
			current_node.set_value(val)
			current_node.set_size(1)
			current_node.set_height(0)
			current_node.set_BF(0)
			current_node.set_left(AVLNode.create_virtual_node())
			current_node.set_right(AVLNode.create_virtual_node())
			return balance_after_insertion(current_node)


	"""Perform a basic roll operation
	@:param node: the root node of the roll
	For example, roll right is for the case:
	A->((B->(C)) becomes B->(C, A)
	Returns the new root node of the subtree
	"""
	@staticmethod
	def roll (node: AVLNode, direction: int):
		rootParent = node.get_parent()
		isRightChild = node.is_right_child()
		leftChild = node.get_left()
		rightChild = node.get_left()
		if direction == R: #right roll.
			leftRightChild = leftChild.get_left()
			node.set_left(leftRightChild)
			node.update()
			leftChild.set_right(node)
			leftChild.update()
			if isRightChild:
				rootParent.set_right(leftChild)
			else:
				rootParent.set_left(leftChild)
			rootParent.update()
			return 1
		elif direction == L: #left roll.
			rightLeftChild = rightChild.get_left()
			node.set_right(rightLeftChild)
			node.update()
			rightChild.set_left(node)
			rightChild.update()
			if isRightChild:
				rootParent.set_right(rightChild)
			else:
				rootParent.set_right(rightChild)
		elif direction == RL:
			AVLTree.roll(node.right, R)
			AVLTree.roll(node, L)
			return 2
		else:
			AVLTree.roll(node.left, L)
			AVLTree.roll(node, R)
			return 2
		rootParent.update()
		return 1






	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		current_node = self.root
		while current_node.key != node.key:
			if current_node.key > node.key:
				current_node = current_node.get_left()
			else:
				current_node = current_node.right
		if not current_node.get_right().is_real_node() or not current_node.get_left().is_real_node():
			parent = current_node.get_parent()
			current_node.right.set_parent(parent)
			current_node.left.set_parent(parent)
			parent.set_right(current_node.right)
			parent.set_left(current_node.left)
		else:
			successor = current_node.find_successor()
			current_node.set_key(successor.get_key())
			successor.get_right().set_parent(successor.get_parent())
			successor.get_parent().set_left(successor.get_right())
		return balance_after_delete(current_node)




	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		return None


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
				rank += current_node.get_left().get_size +1
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
		return None


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root

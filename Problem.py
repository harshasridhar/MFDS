class Node:
	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def print(self, order='inorder'):
		if order == 'inorder':
			if self.left is not None:
				self.left.print(order)
			if self.right is not None:
				self.right.print(order)
			print(self.value,end=' ')
		elif order == "pre":
			print(self.value,end=' ')
			if self.left is not None:
				self.left.print(order)
			if self.right is not None:
				self.right.print(order)
	def getTreeRepresentation(self, order="in"):
		treeRepr = ""
		if order == "in":
			if self.left is not None:
				treeRepr += self.left.getTreeRepresentation(order)
			treeRepr += str(self.value) + " "
			if self.right is not None:
				treeRepr += self.right.getTreeRepresentation(order)
		elif order == "pre":
			treeRepr += str(self.value) + " "	
			if self.left is not None:
				treeRepr += self.left.getTreeRepresentation(order)
			if self.right is not None:
				treeRepr += self.right.getTreeRepresentation(order)
		elif order == "post":
			if self.left is not None:
				treeRepr += self.left.getTreeRepresentation(order)
			if self.right is not None:
				treeRepr += self.right.getTreeRepresentation(order)
			treeRepr += str(self.value) + " "
		return treeRepr

class Problem:
	def buildTree(self, pre, ino):
		if len(pre)==0:
			return None
		root_element = pre.pop(0)
		# print('Root Element is {}'.format(root_element))
		# print('Given pre {} ino {}'.format(pre,ino))
		if len(ino) == 1 or root_element not in ino or len(pre) == 0:
			return Node(ino[0])
		if len(pre) == 1 and len(ino)==0:
			return Node(pre[0])
		root = Node(root_element)
		left_subtree=ino[:ino.index(root_element)]
		right_subtree=ino[ino.index(root_element)+1:]
		# print('Left Subtree : {}'.format(left_subtree))
		# print('Right Subtree: {}'.format(right_subtree))
		if len(left_subtree) != 0:
			root.left = self.buildTree(pre,left_subtree)
		# print('Left done root is {}'.format(root.value))
		if len(right_subtree) != 0:
			root.right = self.buildTree(pre,right_subtree)
		# print('Right done root is {}'.format(root.value))
		return root

	def findNextNode(self, postorder, inorder):
		tempPostOrder=postorder[::-1]
		elementIndexMap = {element:tempPostOrder.index(element) for element in inorder}
		return sorted(elementIndexMap.items(), key=lambda x: x[1])[0][0]

	def buildTreeFromPostOrderAndInorder(self, postorder, inorder):
		if len(postorder)==0:
			return None
		root_element = self.findNextNode(postorder, inorder)
		postorder.remove(root_element)
		if len(inorder) == 1 or root_element not in inorder or len(postorder) == 0:
			return Node(inorder[0])
		if len(postorder) == 1 and len(inorder)==0:
			return Node(postorder[0])
		root = Node(root_element)
		left_subtree=inorder[:inorder.index(root_element)]
		right_subtree=inorder[inorder.index(root_element)+1:]
		if len(left_subtree) != 0:
			root.left = self.buildTreeFromPostOrderAndInorder(postorder,left_subtree)
		if len(right_subtree) != 0:
			root.right = self.buildTreeFromPostOrderAndInorder(postorder,right_subtree)
		return root

	
# pre=[1,2,4,8,9,10,11,5,3,6,7]
# ino=[8,4,10,9,11,2,5,1,6,3,7]
# pre="1,2,4,8,9,10,11,5,3,6,7".split(",")
# ino="8,4,10,9,11,2,5,1,6,3,7".split(",")
# post="8,10,11,9,4,5,2,6,7,3,1".split(",")
# # pre="1,2".split(',')
# # ino='1,2'.split(',')
# p=Problem()
# # tree= p.buildTree(pre,ino)
# tree=p.buildTreeFromPostOrderAndInorder(post,ino)
# tree.print(order='pre')
class avlNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
	def height(self):
		left_ht = 0
		if self.left:
			left_ht = self.left.height()
		right_ht = 0
		if self.right:
			right_ht = self.right.height()
		return 1+max(left_ht,right_ht)
		
	def check_balance(self):
		left_ht = 0
		if self.left:
			left_ht = self.left.height()
		right_ht = 0
		if self.right:
			right_ht = self.right.height()
		return (left_ht - right_ht)	
		
	def balance(self):
		check = self.check_balance() 
		#print "------ AA GAYA CHECK ----- {0}".format(check)
		if check == 3: 		#left subtree is greater than right
			if self.left.check_balance() == 2:	#left-left case
				self.rightRotate()
			else:								#left-right case
				self.left.leftRotate()
				self.rightRotate()
				
		elif check == -3: 	#right subtree is greater than left
			if self.right.check_balance() == -2:	#right-right case
				self.leftRotate()
			else:								#right-leftcase
				self.right.rightRotate()
				self.leftRotate()
			
	def setChildren(self,left,right):
		self.left = left
		self.right = right
	
	def rightRotate(self):
		self.data, self.left.data = self.left.data, self.data
		temp_right = self.right
		self.setChildren(self.left.left,self.left)
		self.right.setChildren(self.right.right, temp_right)
		
		
	def leftRotate(self):
		self.data, self.right.data = self.right.data, self.data
		temp_left = self.left
		self.setChildren(self.right, self.right.right)
		self.left.setChildren(temp_left, self.left.left)	
		
	def avl_insert(self,value):
		if value <= self.data:
			if self.left is None:
				self.left = avlNode(value)
			else:
				self.left.avl_insert(value)
		else:
			if self.right is None:
				self.right = avlNode(value)
			else:
				self.right.avl_insert(value)
		self.balance()			#check for any height differences greater than 1 and balance 
		
	def avl_print(self,offset = 0):    
		print " "*offset + str(self.data)
		if self.left:
			self.left.avl_print(offset+2)
		if self.right:
			self.right.avl_print(offset+2)
	def childCount(self):
		if self is None:
			return None
		count = 0
		if self.left:
			count += 1
		if self.right:
			count += 1
		return count
	
	def lookup(self,value, parent = None):
		if value < self.data:
			if self.left is None:
				return None, None
			else:
				return self.left.lookup(value,self)
		elif value > self.data:
			if self.right is None:
				return None,None
			else:
				return self.right.lookup(value,self)
		else:
			return self, parent
		
		
	def avl_delete(self,value):
		node, parent = self.lookup(value)
		'''
		if node:
			print "node IS HERE ==> {0}\n".format(node.data)
		if parent:
			print "parent IS HERE ==> {0}\n".format(parent.data)
		'''
		
			
		if node is not None:
			children = node.childCount()
		if children == 0: 	#leaf node
			if parent.left is node:
				parent.left = None
			else:
				parent.right = None
			del node
		elif children == 1:	#one child
			if node.left:
				n = node.left
			else:
				n = node.right
			if parent.left is node:
				parent.left = n
			else:
				parent.right = n
			del node
		else:			#two children
			parent = node
			successor = node.right
			while successor.left:
				parent = successor
				successor = successor.left
			node.data = successor.data
			if parent.left == successor:
				parent.left = successor.right
			else:
				parent.right = successor.right
		parent.balance()
	
	def preorder(self):
		print self.data
		if self.left:
			self.left.preorder()
		if self.right:
			self.right.preorder()				
			

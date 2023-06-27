class Node:
	def __init__(self, token=None):
		self.token = token
		self.level = 0
		self.children = []
	
	def add(self, token):
		self.addNode(Node(token))
		
	def addNode(self, node):
		node.level = self.level + 1
		self.children.append(node)
		
	def toString(self):
		s = "    " * self.level
		
		if self.token == None:
			s += "ROOT\n"
		else:
			s += self.token.cargo + "\n"
			
		for child in self.children:
			s += child.toString()
		return s
		

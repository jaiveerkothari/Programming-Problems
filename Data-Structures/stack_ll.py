# Python implementation of a stack  using a linked list

class _Node:
	def __init__(self):
		self.data = None
		self.next = None

class Stack_LL:
	def __init__(self):
		self.top = None

	def push(self, value):
		if self.top != None:
			newNode = _Node()
			newNode.data = value
			newNode.next = self.top
			self.top = newNode
		else:
			self.top = _Node()
			self.top.data = value
			self.top.next = None

	def pop(self):
		if self.top != None:
			topVal = self.top.data
			self.top = self.top.next
		else:
			topVal = None 
		return topVal

	def peek(self):
		if self.top != None:
			return self.top.data
		else:
			return None

	def show(self):
		output = []
		i = self.top
		while i != None:
			output.append(i.data)
			i = i.next
		print output

def tests():
	s = Stack_LL()
	s.push(3)
	s.push(5)
	assert s.peek()==5
	x = s.pop()
	assert s.peek()==3






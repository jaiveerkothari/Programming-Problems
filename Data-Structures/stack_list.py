# Python implementation of a stack the list object
class Stack_List:
	def __init__(self):
		self.elements = []

	def push(self, value):
		self.elements.append(value)

	def pop(self):
		return self.elements.pop()
		
	def peek(self):
		return self.elements[len(self.elements)-1]

	def show(self):
		print self.elements



def tests():
	s = Stack_List()
	s.push(3)
	s.push(5)
	assert s.peek()==5
	x = s.pop()
	assert s.peek()==3



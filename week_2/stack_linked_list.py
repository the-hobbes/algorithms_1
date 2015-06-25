class Stack():
	'''Implementing a stack, using a linked list.
		Every operation takes constant time in the worst case. There are no
		loops in the stack implementation.
	'''

	def __init__(self):
		self.first_node = self._Node() # top of the stack
		self.SIZE = 1 # size of the stack

	class _Node():
		'''Inner class, implementing a linked list.'''
		item = '' # the string item
		next = None # the next object in the linked list


	def push(self, item):
		'''Insert an item onto the stack'''
		old_first = self.first_node
		self.first_node = self._Node()
		self.first_node.item = item
		self.first_node.next = old_first # remember that 'next' is a node object
		self.SIZE += 1

	def pop(self):
		'''Remove an item from the top of the stack'''
		if self.isEmpty():
			raise Exception('Attempted to pop from empty stack.')

		item = self.first_node.item
		self.first_node = self.first_node.next
		self.SIZE -= 1
		return item

	def isEmpty(self):
		'''Is the stack empty?'''
		return self.first_node == None


def client_code(test_string):
	'''Read strings. 
		If string is '-', pop a string from the stack and print.
		Otherwise, push the string onto the stack.
	'''
	stk = Stack()
	output = []
	for string in test_string.strip().split():
		if string == '-':
			output.append(stk.pop())
			continue # don't push a '-' into the stack
		stk.push(string)
	return output

def main():
	'''Client for testing'''
	test_string = 'to be or not to - be - - that - - - is'
	observed_result = client_code(test_string)
	expected_result = ['to', 'be', 'not', 'that', 'or', 'be']

	assert observed_result == expected_result


if __name__ == '__main__':
	main()
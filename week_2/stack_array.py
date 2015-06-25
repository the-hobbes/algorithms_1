class Stack():
	''' Implementing a stack with an array, which is even faster than a linked
		list.
		With languages such as Java, the length of the array must be declared
		ahead of time, which can cause issues when the items of the array
		exceed the space allocated. You can use something like an arraylist 
		though, which will dynamically increase the amount of space in an array
		for you as you add to it (although it may be inefficient).
		The way that dynamic arrays in java and python implement size handling
		is to double the size of the array when it is full, and to half the size
		of the array when it becomes a quarter full. 
	'''
	def __init__(self):
		self.stack = [] # array object itself

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		if self.isEmpty():
			raise Exception('Attempted to pop from empty stack.')

		popped_item = self.stack[-1]
		self.stack[-1] = None # let the garbage collector reclaim this memory
		self.stack = self.stack[:-1] # everything except the last item
		return popped_item

	def isEmpty(self):
		return len(self.stack) == 0


''' Client code remains the same as the linked list implementation'''

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
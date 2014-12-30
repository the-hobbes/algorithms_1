#!/usr/bin/python

'''
  Create a stack, with an array as the underlying data structure.

  Complexity analysis:
  - a defect is that the stack overflows when N exceeds capacity. 
'''

class StackOfStrings():
  # stack implementation using an array

  
  def __init__(self, capacity):
    # note that capacity is a cheat, to be fixed later
    self.stack = [None] * capacity
    self.top = 0

  def push(self, item):
    # add new item at s[n]
    self.stack[self.top] = item
    self.top = self.top + 1

  def pop(self):
    # remove item at s[n-1]
    item = self.stack[self.top - 1]
    self.stack[self.top] = None
    self.top = self.top - 1
    return item

  def is_empty(self):
    return self.top == 0


def main():
  # client code/tests
  stk = StackOfStrings(10)
  stk.push('a')
  stk.push('b')
  stk.push('c')
  stk.pop()
  stk.pop()
  assert stk.pop() == 'a'
  assert stk.is_empty() == True


main()


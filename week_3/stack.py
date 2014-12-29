#!/usr/bin/python

'''
  Create a stack.
  Specifically, a stack of strings.
  Underlying data structure is a linked list.
  
  Performance of the linked list implementation:
    - every operation takes constant time in the worst case.
    - there are no loops or complex structures 
    - constant time, but we can do better. what about an array
      implementation of a stack?
'''

class StackOfStrings():
  # stack implementation using linked lists


  class Node():
    # node class to implement linked lists
    item = ''
    nxt = None


  def __init__(self):
    # create an empty stack
    self.first = None  # top of the stack

  def push(self, item):
    # insert a new string into the stack
    old_first = self.first
    self.first = StackOfStrings.Node()
    self.first.item = item
    self.first.nxt = old_first

  def pop(self):
    # remove and return the most recently added string
    item = self.first.item
    self.first = self.first.nxt
    return item

  def is_empty(self):
    # check to see if the stack is empty
    return self.first == None

def main():
  # client code
  stk = StackOfStrings()
  stk.push('a')
  stk.push('b')
  stk.push('c')
  stk.pop()
  stk.pop()
  assert stk.pop() == 'a'
  assert stk.is_empty() == True


main()

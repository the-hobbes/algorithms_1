#!/usr/bin/python

'''
  Creating an array that grows/shrinks dynamically.
  - python has a builtin for this already.
  - we want to ensure resizing occurs infrequently.

'''

class RepeatedDoubling():
  '''
    Repeated doubling:
    - when an array fills up, create a new array that is twice
      the size of the current array.
  '''

  def __init__(self):
    self.array = []
    self.idx = 0

  def push(self, item):
    if len(self.array) == 0:
      self.array = self.resize(1)
    if len(self.array) <= self.idx:
      self.array = self.resize(len(self.array) * 2)
    
    self.array[self.idx] = item
    self.idx += 1 
    self.print_me()

  def resize(self, capacity):
    new_array = [None] * capacity
    for index in range(len(self.array)):
      new_array[index] = self.array[index]

    return new_array

  def print_me(self):
    print 'Length = ' + str(len(self.array))
    print 'Contents = '
    print self.array

def main():
  # Repeated Doubling test code
  rd = RepeatedDoubling()
  rd.push('first')
  rd.push('second')
  rd.push('third')
  rd.push('fourth')
  rd.push('fifth')
  rd.push('sixth')
  rd.push('seventh')
  rd.push('eighth')
  rd.push('ninth')



main()

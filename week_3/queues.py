#!/usr/bin/python
'''
  API for a queue:
    QueueOfStrings()  create an empty queue
    enqueue(item)     insert a new string into queue
    dequeue()         remove/return least recently added string
    is_empty()        is the queue empty?

  Head and tail:
    Enqueue = add a new item at tail.
    Dequeue = remove an item at head.
'''

class QueueOfStringsLinkedList():
  '''
    Queue =   
      first - node - node - node - last
    Create a queue using a linked list as the data structure.
  '''

  class Node():
    item = ''
    nxt = None

  def __init__(self):
    self.last = QueueOfStringsLinkedList.Node()
    self.first = QueueOfStringsLinkedList.Node()

  def enqueue(self, item):
    # save a link to the last node
    # create a new node for the end
    # link the new node to the end of the list

    old_last = self.last
    self.last = QueueOfStringsLinkedList.Node()
    self.last.item = item
    self.last.nxt = None
    
    # handle empty queue
    if self.is_empty():
      self.first = self.last
    else:
      old_last.nxt = self.last  
    
  def dequeue(self):
    # save item to return
    # delete first node
    # return saved item
    
    item = self.first.item
    self.first = self.first.nxt

    # handle empty queue
    if self.is_empty():
      self.last = QueueOfStringsLinkedList.Node()

    return item
  
  def is_empty(self):
    if self.first == None:
      return True
    elif self.first.item  == '':
      return True
    
    return False
  
  def print_queue(self):
    node = self.first
    while(node.item):
      print node.item
      if node.nxt == None:
        break
      node = node.nxt


class QueueOfStringsResizingArray():
  '''
    Create a queue using a resizing array as the data structure.
    I am using the same concept as in resizing_arrays.py.
  '''


  def __init__(self):
    self.q = []
    self.head = 0
    self.tail = 0
    self.N = 0 # number of elements in the queue

  def enqueue(self, item):
    # add a new item at q[tail]
    if len(self.q) == self.N:
      self.resize(len(self.q) * 2)
    if len(self.q) == 0:
      self.resize(2)

    self.q[self.tail + 1] = item
    self.tail += 1
    if self.tail == len(self.q):
      self.tail = 0
    self.N += 1    

  def dequeue(self):
    # remove an item from q[head]
    item = self.q[self.head]
    self.q[self.head] = None
    self.N -= 1
    self.head += 1
    
    if self.head == len(self.q):
      self.head = 0

    if len(self.q) != 0 and len(self.q)/4 == self.N:
      self.resize(len(self.q)/2)

  def resize(self, capacity):
    new_array = [None] * capacity
    for i in range(0, self.N):
      new_array[i] = self.q[self.first + i % len(self.q)]    
    self.q = new_array
    self.head = 0
    self.tail = self.N

  def is_empty(self):
    return self.N == 0

  def print_queue(self):
    print self.q


def test_ll():
  print '---Linked List Queue:---'
  ll_queue = QueueOfStringsLinkedList() 
  ll_queue.enqueue('a')
  ll_queue.enqueue('b')
  ll_queue.enqueue('c')
  ll_queue.print_queue()
  print '---Dequeue---'
  print ll_queue.dequeue()

def test_array():
  print '---Array Queue---'
  array_queue = QueueOfStringsResizingArray()
  array_queue.enqueue('a')
  array_queue.print_queue()
  print array_queue.dequeue()
  # TODO: there is a bug in this: i fill it with none. also, the starting size should be handled more gracefully

def main():
  # test_ll()
  test_array() 


main()


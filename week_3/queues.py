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
    self.head = None
    self.tail = None
    self.capacity = None

  def enqueue(self, item):
    # add a new item at q[tail]
    pass

  def dequeue(self):
    # remove an item from q[head]
    pass

  def resize(self, capacity):
    new_array = [None] * capacity
    for index in range(len(self.q)):
      if self.q[index]:
        new_array[index] = self.q[index]

    return new_array

  def is_empty(self):
    pass

  def print_queue(self):
    pass

def main():
  print '---Linked List Queue:---'
  ll_queue = QueueOfStringsLinkedList() 
  ll_queue.enqueue('a')
  ll_queue.enqueue('b')
  ll_queue.enqueue('c')
  ll_queue.print_queue()
  print '---Dequeue---'
  print ll_queue.dequeue()

  print '---Array Queue---'
  array_queue = QueueOfStringsResizingArray()
  array_queue.enqueue('a')
  array_queue.print_queue()


main()


#!/usr/bin/python
'''
  API for a queue:
    QueueOfStrings()  create an empty queue
    enqueue(item)     insert a new string into queue
    dequeue()         remove/return least recently added string
    is_empty()        is the queue empty?
'''

class QueueOfStringsLinkedList():
  '''
    Queue =
      first - node - node - node - last
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
    old_last.nxt = self.last
  
    #TODO: add the special case for empty queue in both
    # the enqueue and dequeue operations. 

  def dequeue(self):
    # save item to return
    # delete first node
    # return saved item

    item = self.first.item
    self.first = self.first.nxt
    return item
  
  def is_empty(self):
    return self.first.nxt == None

def main():
  ll_queue = QueueOfStringsLinkedList() 
  ll_queue.enqueue('a')
  ll_queue.enqueue('b')
  ll_queue.enqueue('c')
  ll_queue.dequeue()
  ll_queue.dequeue()
  assert ll_queue.dequeue() == 'c'
main()


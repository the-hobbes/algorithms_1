#!/usr/bin/python

from random import randrange


class Shuffle:
  '''
    Shuffle algorithm:
    - take in a collection that needs shuffling.
    - walk through the collection, and generate a random integer x between 0 and
      i, where i is the index of the current iteration.
    - exchange collection[i] with collection[x]
    - repeat until i >= len(collection)
  '''


  def __init__(self, collection):
    return self.shuffle(collection)    

  def shuffle(self, collection):
    N = len(collection)
    self.shuffled_collection = [None] * N

    for i in range(0, N):
      rand = randrange(0, i + 1)
      self.shuffled_collection[i], self.shuffled_collection[rand] = ( 
        collection[rand], collection[i])

  def __str__(self):
    return str(self.shuffled_collection)

def main():
  collection = [1, 2, 3, 4, 5, 6, 7]
  shuffled = Shuffle(collection)
  print shuffled

main()

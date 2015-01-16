#!/usr/bin/python
'''
  Mergesort implemented in python.
  Continually splits a list in half. 
  - If the list is empty or has one item, it is sorted by definition (the base
  case).
  - If the list has more than one item, we split the list and recursively
  invoke a merge sort on both halves.
  - Once the two halves are sorted, the fundamental operation (called a merge)
  is performed. 
  - Merging is the proces of taking two smaller sorted lists and combining them
  to form a single, sorted, new list. 
'''
import math

class Mergesort():


  def sort(self, comparable):
    '''
      Recursively sort an array.
    '''
    print('Splitting ', comparable)

    # base case
    if len(comparable) < 2:
      return comparable
    
    mid = len(comparable) // 2
    left_half = comparable[:mid]
    right_half = comparable[mid:]

    self.sort(left_half)
    self.sort(right_half)
  
    # at this point, we assume the sublists are sorted, and can be merged
    i, j, k = 0, 0, 0
    
    while i < len(left_half) and j < len(right_half):
      # while we have items in both arrays, compare the two and pick the smaller
      if left_half[i] < right_half[j]: # the item in the left list is smaller
        comparable[k] = left_half[i]
        i += 1 # increment i, as we've used it to put an item into the result
      else: # the item on the right is smaller, or they are the same
        comparable[k] = right_half[j]
        j += 1 # increment j, as we've used it to put an item into the result
      k = k + 1 # increment k, as we must fill the next slot it the result

    while i < len(left_half):
      # if there are any items left in the left half, put them into the result
      comparable[k] = left_half[i]
      i += 1
      k += 1
  
    while j < len(right_half):
      # if there are any items left in the right half, put them into the result
      comparable[k] = right_half[j]
      j += 1
      k += 1
    
    print('Merging ', comparable)
 
    return comparable

def main():
  comparable = [2, 4, 5, 1, 0, 435, 5, 7, 9]
  ms = Mergesort()
  print('The sorted list is: ', ms.sort(comparable))


main()


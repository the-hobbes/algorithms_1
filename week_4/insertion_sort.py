#!/usr/bin/python

class InsertionSort():
    '''
       O(n) when the data set is already substantially sorted. O(n^2) when the
       data is in the worst case (completely non-sorted).

       Algorithm:
        On each iteration, move a[i] into the appropriate position on its left.
        Everything to the left of i is sorted, and everything to the right we 
        have not seen yet. 
        When i is less than wthe element to its left, exchange it with that 
        element. Continue until the elements to the left of the pointer are in
        sorted order. This means that everything to the left of i is in order.
        Repeate this until there are no more cards left to sort.
    '''  

    def __init__(self):
      pass

    def sort(self, comparable):
      for i in range(len(comparable)):
        for j in range(i, 0, -1): # start, stop, decrement
          if comparable[j] < comparable[j - 1]:
            comparable[j], comparable[j-1] = comparable[j-1], comparable[j]
          else:
            break 
      return comparable

def main():
  sort_me = [7, 10, 5, 3, 8, 4, 2, 9, 6]
  i_s = InsertionSort()
  print i_s.sort(sort_me)


main()

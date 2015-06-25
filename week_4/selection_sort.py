#!/usr/bin/python

class SelectionSort():
  '''
    O(n^2) time complexity. Generally performs worse than insertion sort
    (except in the worst case for insertion sort, when there is no order to the
    list).

    Algorithm:
    The input list is divided into two parts: An (initially empty) sublist of
    sorted items, and a sublist of items remaining to be sorted.
    The smallest element in the unsorted list is found, and then exchanged with
    the leftmost element in that same unsorted list.
    The sublist boundaries are then moved one element to the right (usually 
    done with a pointer, in this implementation the variable called 'minimum').
  '''
  def __init__(self):
    pass

  def sort(self, comparable):
    for i in range(0, len(comparable)):
      minimum = i
      for j in range(i + 1, len(comparable)):
        if comparable[j] < comparable[minimum]:
          minimum = j
      comparable[i], comparable[minimum] = comparable[minimum], comparable[i]

    return comparable 


def main():
  ss = SelectionSort()
  sort_me = [7, 10, 5, 3, 8, 4, 2, 9, 6]
  print ss.sort(sort_me)


main()
  

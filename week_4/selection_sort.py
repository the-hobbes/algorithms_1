#!/usr/bin/python

class SelectionSort():

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
  

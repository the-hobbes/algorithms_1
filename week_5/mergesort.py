#!/usr/bin/python
'''
  Mergesort implemented in python.
  See notes for an explanation of the algorithm.
'''
import math

class Mergesort():
  

  def sort(self, comparable):
    '''
      Recursively sort an array.
    '''
    if len(comparable) < 2:
      return comparable  
    result = [0] * len(comparable)
    mid = int(math.floor(len(comparable) / 2))
    low_array = self.sort(comparable[:mid])
    high_array = self.sort(comparable[mid:])

    # actually do the sort
    i = 0
    j = 0
    for k in range(len(comparable)):
      print 'i is: ' + str(i)
      print 'j is: ' + str(j)
      print 'length of low_array is: ' + str(len(low_array))
      print 'length of high_array is: ' + str(len(high_array))
  
      if i > len(low_array):
        result[k] = high_array[j]
        j += 1
      elif j > len(high_array):
        result[k] = low_array[i]
        i += 1
      elif low_array[i] < high_array[j]:
        result[k] = low_array[i]
        i += 1
      else:
        result[k] = high_array[j]
        j += 1

    return result
        

def main():
  comparable = [2, 4, 5, 1, 0, 435, 5, 7, 9]
  ms = Mergesort()
  print ms.sort(comparable)
  

main()

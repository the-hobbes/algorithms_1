#!/usr/bin/python


class BottomUpMergesort():

  def sort(self, comparable):
    N = len(comparable)
    
    # for each element in the subarray
    # double the size of the subarray until we get to N
    for sz in range(1, N):
      for lo in range(N - sz):
        print "lo: " + str(lo) + " lo + sz-1: " + str(lo+sz-1) + " min: " + str(min(lo+sz+sz-1, N-1))  
        self.merge(comparable, lo, lo + sz - 1, min(lo+sz+sz-1, N-1))
        lo += (sz + sz)
      sz = sz + sz
    
    return comparable

  def merge(self, comparable, lo, mid, hi):
    # lo is the first part of the array to be sorted
    # mid is the midpoint between the two
    
    aux = list(comparable)
    print aux

    # start the i pointer at the left part of the left half
    # start the j pointer at the left part of the right half
    # start k at low
    # for every value of k, we are most often comparing whether aux[j] is less
    # then aux[i].
    
    i = lo
    j = mid + 1
    for k in range(hi):
      print aux
      if i > mid: 
        comparable[k] = aux[j]
        j += 1
      elif j > hi:
        comparable[k] = aux[i]
        i += 1
      elif aux[i] > aux[j]:
        comparable[k] = aux[j]
        j += 1
      else:
        comparable[k] = aux[i]
        i += 1
      
    return comparable


def main():
  # comparable = [3, 3, 5, 8, 2, 23, 5, 0, 8888]
  comparable = [1, 3, 2]
  bum = BottomUpMergesort()
  print bum.sort(comparable)
   

main()

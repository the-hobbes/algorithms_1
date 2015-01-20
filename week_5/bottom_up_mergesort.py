#!/usr/bin/python


class BottomUpMergesort():

  def sort(self, comparable):
    width = 1
    size = len(comparable)

    for run in range(1, size, width): # start, stop, step
      for item in range(size):
        print comparable[item], comparable[item + width]

      width = width * 2



  def merge(self, comparable, index_left, index_right, index_end, aux):
    pass

def main():
  # comparable = [3, 3, 5, 8, 2, 23, 5, 0, 8888]
  comparable = [1, 3, 2, 4]
  bum = BottomUpMergesort()
  print bum.sort(comparable)


main()

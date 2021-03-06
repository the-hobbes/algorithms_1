#!/usr/bin/python

class ShellSort():
  '''
    Good visual demonstration of the algorithm:
      https://www.youtube.com/watch?v=M9YCh-ZeC7Y

    Algorithm Description:
      - Choose a starting step size, using one of the known methods.
      - step forward through the array until you hit array[stepsize]
      - compare the value of array[stepsize] with array[startingpoint]
        - for example, if the step size was 6 and this was the first iteration
          of the array, you would compare array[6] and array[0]
      - if array[6] is smaller than array[0], swap them
      - if you can walk back the length of the step size from the newly swapped
        element to compare it to the element in its position - step size, do so.
        - if the element you are comparing it to is larger than it, then swap
          them 
        - repeat
      - otherwise, continue forward until you cannot walk forward a full step
        size
      - repeat the above for a smaller step size, decremented according to the
        method you choose fit. Do this until the step size is 1, after which
        the array will be sorted.
  '''
  def __init__(self, a):
    # argument: comparable a
    self.a = a
    self.gap = self.calculate_start()

  def sort(self):
    gap = self.gap
    a = self.a
    print 'original: ' + str(a)
    # loop over gaps
    while gap > 0:
      print 'gap:' + str(self.gap) + '\n'
      # insertion sort time, using the gap instead of -1
      for i in range(gap, len(a)): # for the array given, gap starts at 4
        val = a[i]
        j = i
        while j >= gap and a[j - gap] > val:
          print 'j:' + str(j)
          print 'a[j]: ' + str(a[j])
          a[j] = a[j - gap]
          j -= gap
          print 'currently: ' + str(a)
        a[j] = val
      gap //= 3

    return a

  def calculate_start(self):
    # calculate starting h using knuth's 3x + 1 method
    h = 1
    while h < len(self.a) // 3:
      h = (3 * h) + 1

    return h


def main():
  sort_me = [1, 3, 78, 3, 6, 8, 5, 9, 0]
  shell_sort = ShellSort(sort_me)
  print shell_sort.sort()

main()

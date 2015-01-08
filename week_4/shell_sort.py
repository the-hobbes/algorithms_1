#!/usr/bin/python

class ShellSort():
  '''
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

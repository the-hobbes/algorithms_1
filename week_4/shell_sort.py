#!/usr/bin/python

class ShellSort():
  '''
  ''' 
  def __init__(self, a):
    # argument: comparable a
    self.N = len(a)
    self.h = self.calculate_starting_h()

  def sort(self):
    while self.h >= 1:
      # h-sort the array
      for i in range(self.h, self.N):
        
      self.h = self.h / 3 # move to the next increment

  def calculate_starting_h(self):
    # calculate starting h using knuth's 3x + 1 method
    h = 1
    while h < int(self.N / 3):
      h = (3 * h) + 1
    
    return h


def main():
  sort_me = ['s', 'h', 'e', 'l', 'l', 's', 'o', 'r', 't']
  shell_sort = ShellSort(sort_me)
  shell_sort.sort()

main()

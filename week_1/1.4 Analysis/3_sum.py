''' Given N distinct integer, how many triples sum to exactly 0?

    For example, given the following input:
      30 -40 -20 -10 40 0 10 5
    The output would be:
      4
    Since:
      30 + -40 + 10 = 0
      30 + -20 + 10 = 0
      -40 + 40      = 0
      -10 + 10      = 0

    Running Time is N^3
'''
from datetime import datetime


class ThreeSum():

  def __init__(self, inpt):
    self.inpt = inpt

  def count(self):
    '''
        Loop through self.inpt and determine the number of triples sum to 0.
        Return that number. 
        Brute force, for small numbers. 
    '''
    inpt = self.inpt
    counter = 0
    N = len(inpt)
    
    # triple for loop, gets each triple once and checks the sum.
    for i in range(N):
      for j in range(i + 1, N):
        for k in range(j + 1, N):
          if inpt[i] + inpt[j] + inpt[k] == 0:
            counter += 1

    return counter


def main():
  inpt = [30, -40, -20, -10, 40, 0, 10, 5]
  
  # time it the operation
  time_start = datetime.now()
  output = ThreeSum(inpt) # the actual code we want to test
  time_end = datetime.now()
  time_elapsed = time_end - time_start
  # milliseconds_elapsed = int(time_elapsed.total_seconds() * 1000)
  print time_elapsed

  assert output.count() == 4

if __name__ == '__main__':
  main()
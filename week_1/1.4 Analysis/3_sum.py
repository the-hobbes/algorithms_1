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
'''
class ThreeSum():

  def __init__(self, inpt):
    self.inpt = inpt

  def count(self):
    '''
        Loop through self.inpt and determine the number of triples sum to 0.
        Return that number. 
    '''
    inpt = self.inpt
    counter = 0
    N = len(inpt)
    
    for i in range(N):
      for j in range(i + 1, N):
        for k in range(j + 1, N):
          if inpt[i] + inpt[j] + inpt[k] == 0:
            counter += 1

    print counter
    return counter


def main():
  inpt = [30, -40, -20, -10, 40, 0, 10, 5]
  output = ThreeSum(inpt)
  assert output.count() == 4

if __name__ == '__main__':
  main()
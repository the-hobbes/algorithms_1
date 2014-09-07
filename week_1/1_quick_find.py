class QuickFind():
  '''implement the QuickFind algorithm, to see if any two items are connected'''

  def __init__(self, n):
    '''set the id of each object to itself in an array'''
    self.id = [i for i in range(n)]

  def connected(self, p, q):
    '''determine if p and n are connected. This is the find in quickfind'''
    return self.id[p] == self.id[q]

  def union(self, p, q):
    '''connect two elements p and q.
        set all items with id[p] to have id[q]
        This will run in N^2 time, which is too slow (quadratic time).
    '''
    p_id = self.id[p]
    q_id = self.id[q]

    for idx in range(len(self.id)):
      if self.id[idx] == p_id:
        self.id[idx] = q_id


def main():
  NUMBER_OF_ELEMENTS = 10

  qf = QuickFind(NUMBER_OF_ELEMENTS)
  assert qf.id == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  
  qf.union(9, 1)
  assert qf.id == [0, 1, 2, 3, 4, 5, 6, 7, 8, 1]

  

main()
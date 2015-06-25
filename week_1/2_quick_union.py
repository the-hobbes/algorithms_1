'''
	Alternative to quick find where we try and improve the union operation from
	quadratic time.
	This is a lazy algorthim, so-called because we try to avoid doing work until
	we have to. 

	We will use the same data structure, but have a different interpretation for 
	it. It will represent a tree, where each connected component has a root.
	EG-> if the 10 elements in the id[] array for a quick union data structure
	are:
		0 9 6 5 4 2 6 1 0 5
	then the roots of three and seven are:
		6 and 6
	which indicates they are in the same connected component. If two items have
	the same root, they are therefore connected.
	
	union(3, 8) means that we take the tree with the root node of 3 and set it
	as a child of the tree with the root node of 8.

	The drawback of this is that the trees can get too deep, making the find
	operation very expensive. Not scalable.
'''

class QuickUnion():
	def __init__(self, n):
		'''Create the array and set the value of each element to be its own root
		'''
		self.id = [i for i in range(n)]

	def _root(self, i):
		'''method used to find the root of a given node i. 
		   -First, note that the root of the tree points to itself, i.e. 
			that if p is the root of the tree it belongs to, then id[p] = p.
			1) is id[i] == i? If so, i is the root of it's tree, so we're done 
			   so return i.
			2) If not, move one step up the tree. id[i] is the address of the 
			   parent node of i, so we set i to id[i] (so i now refers to the 
			   parent node) and then go back to step 1.
			For example, if the array looks like this: 
			[0, 1, 2, 8, 3, 5, 6, 7, 8, 9]
			And you call _root(3), 
			you check to see if id[3] == 3. id[3] is 8, so you set i = id[3]. i
			is now 8. You then check again, to see if id[8] == 8. Indeed it does
			and you've found the root of 3.
		'''
		while i != self.id[i]:
			i = self.id[i]
		return i

	def connected(self, p, q):
		'''determine if two elements are connected by using the _root method.'''
		return self._root(p) == self._root(q)

	def union(self, p, q):
		'''Connect two components by changing the root of p to point to the
		root of q.
		'''
		p_root = self._root(p)
		q_root = self._root(q)

		self.id[p_root] = q_root


def main():
  NUMBER_OF_ELEMENTS = 10
  qu = QuickUnion(NUMBER_OF_ELEMENTS)
  print " 0  1  2  3  4  5  6  7  8  9 "
  print qu.id
  qu.union(4, 3)
  print qu.id
  qu.union(3, 8)
  print qu.id
main()
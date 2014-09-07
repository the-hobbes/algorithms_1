'''
	You can use a weighted algorithm to make sure smaller trees become the 
	children of larger trees. This is done by keeping track of the sizes of
	trees and comparing them, and linking the root of the smaller tree to the 
	root of the larger tree in each union operation.

	You would use a weighted algorithm to keep the trees from getting too tall,
	and thus making the find operation too expensive.

	Analysis:
		The depth of any node x is at most lg N (log base 2 of N)
		- remember that log base2 of N is the exponent you have to raise 2 to in 
		order to get N. Log base4 of 64 = x (in other words, 4^x = 64), x = 3.

		The depth of a node x increases by 1 when the tree T1 containing x is
		merged into another tree T2. This is only done when T2 is > T1, so the
		size of the tree containing x at least doubles. 

		The size of the tree containing x can double at most logN times, because
		if you start with 1 and double logN times you get N, and there are only
		N nodes in the tree. 
'''
class QuickUnion():
	def __init__(self, n):
		'''Create the array and set the value of each element to be its own root
			We also need to maintain a separate list containing the size of 
			each tree.
		'''
		self.id = [i for i in range(n)]
		self.sz = [1 for i in range(n)] # each tree has an initial size of 1

	def _root(self, i):
		'''method used to find the root of a given node i.'''
		while i != self.id[i]:
			# self.id[i] = self.id[self.id[i]], see path_compression
			i = self.id[i]
		return i

	def connected(self, p, q):
		'''determine if two elements are connected by using the _root method.
			Takes time proportional to log2 of N.
		'''
		return self._root(p) == self._root(q)

	def union(self, p, q):
		'''Connect two components by changing the root of the smaller tree to
			point to the root of the larger.
			Also update tree sizes in the sz array.
			Takes time proportional to log2 of N.
		'''
		p_root = self._root(p)
		q_root = self._root(q)

		if p_root == q_root: return

		if self.sz[p_root] < self.sz[q_root]: # if the size of tree p is smaller
			self.id[p_root] = q_root # set tree p to be a child of tree q
			self.sz[q_root] += self.sz[p_root] # update the size of tree q with that of p
		else: # otherwise, tree q is smaller or they are equal
			self.id[q_root] = p_root
			self.sz[p_root] += self.sz[q_root]

def main():
  NUMBER_OF_ELEMENTS = 10
  qu = QuickUnion(NUMBER_OF_ELEMENTS) # 505
  qu.union(4, 3)
  qu.union(3, 8) # 8 becomes child of 4, since it is smaller than tree 3,4 (and 4 is root)
  print qu.id


main()
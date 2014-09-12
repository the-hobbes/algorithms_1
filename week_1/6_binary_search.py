'''
	Binary Search algorthim.
	Searching for a key in a sorted array.
	- compare the key against the middle entry of the array
	- if the key is smaller than the middle entry, go left
	- if the key is greater than the middle entry, go right
	- if the key is equal to the middle entry, you've found it. 
'''


class BinarySearch():

	def search (self, key, a):
		'''
			- key is the key we are searching for.
			- a is the array we are searching in.
			Invariant:
				if the key is in the array, then it is between lo and hi in 
				the array.
		'''

		lo = 0
		hi = len(a) - 1 
		# len(a) - 1, because when you are searching for a number > the value 
		# of the last element of a, mid becomes equal to that last element as
		# it is checked, and a[mid] will be out of the list (if the array has
		# three elements in it, and you want to check the last, then a[3] will
		# throw a list out of bounds exception, because you really want a[2]).

		while (lo <= hi):
			mid = lo + (hi -lo) / 2
			# print mid, a[lo:hi] 

			if key < a[mid]:
				hi = mid -1 
			elif key > a[mid]:
				lo = mid + 1
			else:
				return mid

		return -1 # points are equal and we haven't found it, return -1


def main():
	a = [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97]
	bs = BinarySearch()
	
	mid = bs.search(33, a)
	assert mid == 4

	mid = bs.search(-1, a)
	assert mid == -1

	mid = bs.search(100, a)
	assert mid == -1


if __name__ == '__main__':
	main()
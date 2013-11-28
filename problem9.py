""" Write a function permute to compute all possible permutations 
    of elements of a given list.
"""

import itertools

def permute(a):
	result = []
	x = itertools.permutations(a)
	for p in x:
		result.append(list(p))
	return result

print permute([1, 2, 3])


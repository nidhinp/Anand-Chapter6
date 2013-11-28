""" Write a function flatten_dict to flatten a nested dictionary by joining
    the keys with . character
"""

def flatten_dict(x, result = None):
	if result == None:
		result = {}
	a = {}
	for key, value in x.items():
		if isinstance(value, dict):
			for i, j in value.items():
				a[key+'.'+i] = j
			flatten_dict(a, result) 
		else:
			result.update({key: x[key]})
	return result
print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})

""" Write a function unflatten_dict to do reverse of flatten_dict.
    >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
    {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
"""

def unflatten_dict(x, result = None):
	if result == None:
		result = {}
	b = {}
	c = {}
	for key, value in x.items():
		if '.' in key:
			outer_key = key.split('.')[0]
			inner_key = key.split('.')[1]
			b[inner_key] = value
			c[outer_key] = b
			unflatten_dict(c, result)			
		else:
			result[key] = value
	return result
		

print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})

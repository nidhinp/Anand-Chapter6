def treemap(fun, arg_list):
	result = []
	for arg in arg_list:
		if isinstance(arg, list):
			result.append(treemap(fun, arg))
		else:
			result.append(fun(arg))
	return result

print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])

""" Implement a function product to multiply 2 numbers recursively
    using + and - operators only.
"""

def product(number1, number2):
	if number2 == 0:
		return 0
	else:
		return number1 + product(number1, number2 - 1)

print product(4, 3)
print product(5, 7)

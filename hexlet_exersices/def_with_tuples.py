def sort_pair((a, b)):
	
	if a <= b:
		return (a, b)
	else:
		return (b, a)

print(sort_pair((4, 16))
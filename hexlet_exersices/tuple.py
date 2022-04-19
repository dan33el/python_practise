def tuple_changer(t):
	(a, b) = t
	if a >= b:
		print((b, a))
	else:
		print((a, b))

tuple_changer((2, 4))
tuple_changer((123432, 23849))
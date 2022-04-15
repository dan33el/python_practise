from random import choice

def choice_from_range(string='string', first_ind=0, last_ind=-1):
	s = string[first_ind:last_ind]
	print(choice(s))

choice_from_range()
choice_from_range('string', 3, -1)
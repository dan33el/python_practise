def string_or_not(var):
	return 'yes' if isinstance(var, str) == True else 'no'

string_or_not(10)
string_or_not(0.1)
string_or_not('some text')
string_or_not(None)
string_or_not(True)
string_or_not(False)
def filter_string(string, symb):
	filtered_string = ''
	for char in string:
		if char == symb or char == symb.swapcase():
			char = ''
		else:
			char = char
		filtered_string = filtered_string + char
	
	return filtered_string.strip()	
	
print(filter_string('text ', 'E'))
print(len(filter_string('text ', 'E')))
	

	
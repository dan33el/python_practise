def encrypt(text):
	i = 0
	index = text[i]
	last_index = text[-1]
	twisted_word = ''
	while index <= last_index:
		text[i] = text[i+1]
		i += 1
		
	return twisted_word

print(encrypt('text that should be twisted. Every two symbols will be changed on there places'))	
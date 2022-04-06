'''def encrypt(text):
	twisted_text = ''
	i = 0
	last_letter = text[-1]

	while i != last_letter:
		if len(text) % 2 == 0:
			current_char = text[i]
			text[i] = text[i+1]
			twisted_text = twisted_text + current_char


	return twisted_text

encrypt('text that should be twisted. Every two symbols will be changed on there places') '''

def encrypt(t):
	twisted_text = ''
	i = 0
	if t[i] % 2 != 0:
		t[i] = t[i-1]
		
	return twisted_text


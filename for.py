def mirrored_text(text):
	result = ''
	for char in text:
		result = char + result + char

	print(result)

mirrored_text('some text that should be mirrored')
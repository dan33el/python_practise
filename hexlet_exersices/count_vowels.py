from is_vowel import is_vowel

def count_vowels(string):
	result = 0
	for char in string:
		if is_vowel(char) == True:
			result += 1
		else:
			result += 0
	return result

print(is_vowel('o'))
print(count_vowels('wood'))
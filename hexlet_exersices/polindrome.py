def is_polindrome(text):
	start = text[0:]
	finish = text[::-1]
	if start == finish:
		return True
	else:
		return False

print(is_polindrome("some text that aren't polindrome"))
print(is_polindrome("АССА"))
print(is_polindrome("ишак ищет у тещи каши"))
print(is_polindrome(""))

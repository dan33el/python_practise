''' def encrypt(t):
	twisted_text = ''
	i = 0
	if len(t) % 2 == 0:
		while t.index(t[i]) <= t.index(t[-2]):
			twisted_text = twisted_text + t[i]
			i += i+1
			t = t.replace(t[i],t[i+1])
	print(t)
	print(len(t))
'''

def encrypt(text):
    i = 0
    result = ""
    while i < len(text):
        # Используем тернарный оператор
        # Значение переменной nextChar зависит от условия if
        # Если условие выполняется, в переменную записывается пустая строка
        # Иначе в переменную записывается символ строки c индексом i + 1
        nextChar = "" if (i + 1 >= len(text)) else text[i + 1]
        result = result + nextChar + text[i]
        i += 2
    return print(result)

encrypt('some!')

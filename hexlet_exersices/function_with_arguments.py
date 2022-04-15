'''def exponentiate(n1, n2=1):
	m = n1 ** n2
	return m

print(exponentiate(4, 4))
print(exponentiate(45))
'''

def get_hidden_card(card_number = '4300167890902425', symbols_that_hide = 4):
	result = '*' * symbols_that_hide + ' ' + str(card_number[-5:-1])
	return result

print(get_hidden_card('1234567878900987', 1))

def normalize_url(address):

  http = address[:8]

  if http[:8] == 'https://':
      answer = address

  elif http[:7] == 'http://':
      answer = 'https://' + address[7:]

  else:
      answer = 'https://' + address

  return answer

print(normalize_url('https://some.link.com'))
print(normalize_url('another.link.su'))
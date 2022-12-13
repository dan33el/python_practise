def print_numbers(num):

  while num >= 1:
    print(num)
    num = num - 1
  print('finished!')



print_numbers(9)


def reverse_string(string):
  index = len(string) - 1
  reversed_string = ''

  while index >= 0:
      current_char = string[index]
      reversed_string = reversed_string + current_char
      # То же самое через интерполяцию
      # reversed_string = f'{reversed_string}{current_char}'
      index = index - 1

  return print(reversed_string)

reverse_string('some sentence')
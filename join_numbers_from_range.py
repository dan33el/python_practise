def join_numbers_from_range(first_num, last_num=5):
	index = first_num
	string_of_nums = ''
	while index <= last_num:
		string_of_nums = str(string_of_nums)  + str(index) + ', '
		index = index + 1

	return string_of_nums

print(join_numbers_from_range(-4, 10))
print(join_numbers_from_range(0.1, 3.0))

'''	i = start
  sum = 0  # Инициализация суммы
  while i <= finish:  # Двигаемся до конца диапазона
      sum = sum + i   # Считаем сумму для каждого числа
      i = i + 1       # Переходим к следующему числу в диапазоне
  # Возвращаем получившийся результат
  return sum '''
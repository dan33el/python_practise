def find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index

def find_second_index(value, items):
    cursor = iter(items)
    first_index = find_index(value, cursor)
    second_index = find_index(value, cursor)
    if second_index is not None:
        return first_index + second_index + 1
        
print(find_second_index('a', 'baabo'))

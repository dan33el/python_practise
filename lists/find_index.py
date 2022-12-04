def find_index(el, obj):
    for (index, element) in enumerate(obj):
        if el == element:
            print(index)
            break
    else:
        print('Nothing')

find_index(1, [1, 2 , 3])
find_index('l', 'hello')
find_index(1, [])
find_index('i', 'kind')
from math import sqrt

def get_square_roots(num):
    ar = []
    if num < 0:
        return ar
    elif num == 0:
        ar.append(int(sqrt(num)))
        return ar
    else:
        ar.append(ar.append(int(sqrt(num))))
        return ar

print(get_square_roots(100))
print(get_square_roots(-10))
print(get_square_roots(0))

def get_range(r):
    ar = []
    i = 0
    if r <= 0:
        return ar
    else:
        ar.append(0)
        while i < r-1:
            i += 1
            ar.append(i)
    return ar

print(get_range(-5))
print(get_range(0))
print(get_range(5))

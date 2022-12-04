def rotated_left(obj):
    return obj[1:]+obj[:1]

def rotated_right(obj):
    return obj[-1:]+obj[:-1]

print(rotated_left((1, 2, 3, 4, 5)))
print(rotated_right((1, 2, 3, 4, 5)))

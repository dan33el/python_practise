def rotate(lis):
    if lis == []:
        return lis 
    else:
        lis.insert(0, lis.pop())
        return lis
        
print(rotate([]))
print(rotate(list([1, 2, 3, 4, 5])))
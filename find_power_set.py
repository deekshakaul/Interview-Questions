def subsets(my_set):
    result = [[]]
    for x in my_set:
        result = result + [y + [x] for y in result]
    return result
    
a=[1,2,3]
b=subsets(a)
print(b)

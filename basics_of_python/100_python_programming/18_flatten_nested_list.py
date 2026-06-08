
def flatten(arr):
    result = [] 
    for sublist in arr:
        if isinstance(sublist,list):
            result.extend(flatten(sublist))
        else:
            result.append(sublist)
    return result            

arr = [[1, 2], [3, 4], [4, [7, 5]], [5, 6]]
print(flatten(arr))
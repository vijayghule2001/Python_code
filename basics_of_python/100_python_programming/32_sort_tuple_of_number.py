my_tuple = (2,3,4,5,4,6)

lst= list(my_tuple)

for i in range(len(lst)):
    for j in range(i,len(my_tuple)):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

newTuple = tuple(lst)

print(newTuple)
           
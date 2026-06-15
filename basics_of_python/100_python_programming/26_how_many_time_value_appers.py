# my_tuple = (3,4,2,5,6,3,4,2,1)
# count= {}

# for num in my_tuple:
#    if num not in count:
#        count[num] = 1
#    else:
#        val = count[num] + 1
#        count[num] = val   
# print(count)    


my_tuple = (3, 4, 2, 5, 6, 3, 4, 2, 1)
count = {}
for num in my_tuple:
    count[num] = count.get(num, 0) + 1
    
print(count)

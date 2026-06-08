arr = [1,2,8,7,4,3,6,5,4,5,1,2]
obj = {}

# for i in range(0, len(arr)):
#    if arr[i] not in obj.keys():
#        obj[arr[i]] = 1
    
#    else:
#        count  = obj[arr[i]]
#        count = count+1
#        obj[arr[i]] = count   

# print(obj)       


for num in arr:
    obj[num] = obj.get(num,0)+1

print("count of dup: ", obj)        

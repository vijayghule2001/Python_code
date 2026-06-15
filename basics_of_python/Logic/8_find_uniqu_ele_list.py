arr = [1,2,3,4,7,3,2,1]
count = {}

for item in arr:
    count[item] =  count.get(item,0) +1

print("frequency :", count)

for key,val in count.items():
    if val == 1:
        print(key)    



list = [1,2,4,2,3,5,6,1,2]
frequency = {}

for i in range(0 , len(list)):
    count = 1
    for j in range(i+1, len(list)):
        if list[i] == list[j]:
            count =  count +1
    
    if list[i] not in frequency.keys():
        frequency[list[i]] = count

print("Frequency: ", frequency)        
arr  = [2,3,4,5,61,2,3,5,6,7]
given = 5

output = {}

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        sum =  arr[i] + arr[j]
        if sum == given:
            print(f"pair is : {arr[i]} +  {arr[j]} = {given} ")


# arr = [2,3,4,5,61,2,3,5,6,7]
# given = 5

# pairs = set()

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == given:

#             pair = tuple(sorted((arr[i], arr[j])))

#             if pair not in pairs:
#                 pairs.add(pair)
#                 print(pair)            
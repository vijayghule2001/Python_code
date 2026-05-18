arr = [2, 4, 3, 5, 7]
target = 7

for i  in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        sum =  arr[i] + arr[j]
        if target ==  sum:
            print(f"pair: {arr[i]} + {arr[j]} = {sum}")
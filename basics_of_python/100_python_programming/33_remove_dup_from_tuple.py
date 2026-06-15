mytuple = (2,3,4,55,3,2,4)

result = []

for item in mytuple:
    if item not in result:
        result.append(item)

newTuple = tuple(result)

print(newTuple)
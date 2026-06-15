tuple1 = (1, 2, 3, 4, 5,5)
tuple2 = (4, 5, 6, 7, 8,4)
common = []
for item in tuple1:
    if item in tuple2:
        common.append(item)

print("common ele: ", common)        
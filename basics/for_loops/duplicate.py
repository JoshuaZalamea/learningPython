list = [8, 4, 4, 5, 6, 7, 8, 9, 10]
list.sort()
prev = None
for item in list:
    if prev == item:
        print("Duplicate of", prev, "found")
    prev = item
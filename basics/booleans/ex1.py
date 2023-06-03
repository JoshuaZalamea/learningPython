list = ["life", "the universe", "everything", "jack", "jill", "life", "jill"]

copy = list[:]
copy.sort()
prev = copy[0]
del copy[0]

count = 0

while count < len(copy) and copy[count] != prev:
    prev = copy[count]
    count = count + 1

if count < len(copy):
    print("First match:", prev)
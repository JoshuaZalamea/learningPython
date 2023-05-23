a = 23
b = -23


def absoluteValue(n):
    if n < 0:
        n = -n
    return n

if absoluteValue(a) == absoluteValue(b):
    print("The absolute values of", a, "and", b, "are equal")
else:
    print("The absolute values of", a, "and", b, "are different")
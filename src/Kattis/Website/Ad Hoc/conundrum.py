d = 0
for i, c in enumerate(input()):
    if i % 3 == 0 and c != "P":
        d += 1
    elif i % 3 == 1 and c != "E":
        d += 1
    elif i % 3 == 2 and c != "R":
        d += 1
print(d)

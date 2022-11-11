s = []
last = " "
for c in input():
    if c != last:
        s.append(c)
        last = c
print("".join(s))

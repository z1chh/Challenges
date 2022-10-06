w = 0
l = 0
u = 0
o = 0
for c in input():
    if c == "_":
        w += 1
    elif c >= "a" and c <= "z":
        l += 1
    elif c >= "A" and c <= "Z":
        u += 1
    else:
        o += 1
t = w + l + u + o
print(w / t)
print(l / t)
print(u / t)
print(o / t)

n = int(input())
ct = 0
lw = 1
br = 0
while n >= br:
    br += lw * lw
    if n >= br:
        ct += 1
        lw += 2
print(ct)

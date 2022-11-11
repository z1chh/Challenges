longest = -1
l = []
while True:
    try:
        i = input()
        s = len(i)
        l.append(i)
        if s > longest:
            longest = s
    except:
        break
tr = 0
l = l[0:len(l) - 1]
for line in l:
    s = len(line)
    if s < longest:
        tr += (longest - s) * (longest - s)
print(tr)

tt = 15
d = {}
d[1] = 5
d[2] = 4
d[3] = 6

print(d)

mc = 3
cc = 0
fs = -1
while tt > 0:
    while cc < mc and tt > 0:
        for i in d.keys():
            if d[i] > 0:
                if cc == 0:
                    fs = i
                tr = min(d[i], mc - cc)
                d[i] -= tr
                cc += tr
                tt -= tr
    print("after batch", d)
    cc = 0
print(d)

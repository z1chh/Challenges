ct = 1
while True:
    try:
        l = list(map(int, input().split()))
        l = l[1:]
        max = max(l)
        min = min(l)
        print("Case {c}: {min} {max} {range}".format(
            c=ct, min=min, max=max, range=max - min))
        ct += 1
    except:
        break

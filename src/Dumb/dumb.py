s = "allo"
for c in s:
    print(c)
    
if False and 1 / 0:
    print("True")
    
print(s[3])

print(int(5 / 2))

print(max([1, 2, 3, 4, 5, 6]))

def test():
    while True:
        try:
            print(int(input()))
        except:
            break

test()

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


import sys

ct = 1
for i in sys.stdin:
        l = list(map(int, i.split()))
        l = l[1:]
        max = max(l)
        min = min(l)
        print("Case {c}: {min} {max} {range}".format(
            c=ct, min=min, max=max, range=max - min))
        ct += 1
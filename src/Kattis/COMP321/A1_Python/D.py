input()
l = list(map(lambda x: int(x), input().split()))
neg = 0
for n in l:
    if n < 0:
        neg += 1
print(neg)
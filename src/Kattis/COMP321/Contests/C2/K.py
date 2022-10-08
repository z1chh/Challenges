words, jobs = map(int, input().split())
vd = {}
for _ in range(words):
    word, price = input().split()
    vd[word] = int(price)
for _ in range(jobs):
    tot = 0
    while (s := input().split()) != ["."]:
        for w in s:
            if w in vd:
                tot += vd[w]
    print(tot)

input()
battings = map(int, input().split())
total = 0
bats = 0
for bat in battings:
    if bat != -1:
        total += bat
        bats += 1
print(total / bats)

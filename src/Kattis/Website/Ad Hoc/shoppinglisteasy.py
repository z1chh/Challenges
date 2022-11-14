lists, _ = map(int, input().split())
items = {}
for _ in range(lists):
    for item in input().split():
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
popular = []
for item in items:
    if items[item] == lists:
        popular.append(item)
print(len(popular))
for item in sorted(popular):
    print(item)

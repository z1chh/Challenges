num_potions, time = map(int, input().split())
potions = [int(input()) for _ in range(num_potions)]
potions.sort(reverse=True)
for i in range(num_potions):
    potions[i] -= (num_potions - i - 1) * time
for t in potions:
    if t < 1:
        print("NO")
        exit()
print("YES")

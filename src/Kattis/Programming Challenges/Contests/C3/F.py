_, T = map(int, input().split())
tasks = list(map(int, input().split()))
t = 0
completed = 0
for task in tasks:
    if t + task <= T:
        completed += 1
        t += task
    else:
        break
print(completed)

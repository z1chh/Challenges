def won(l):
    for i in l:
        if i != -1:
            return False
    return True


nb = int(input())
l = list(map(int, input().split()))
s = 0
while not won(l):
    # Get highest balloon
    m = l[0]
    index = 0
    for i in range(nb):
        if l[i] > m:
            m = l[i]
            index = i

    # Get height to shoot highest balloon
    if index > 0:
        m += index

    # Shoot
    s += 1
    #print("Shooting at height", m)
    for i in range(index, nb):
        if l[i] == m:
            l[i] = -1
            m -= 1
        if m <= 0:
            break

# Output number of arrows shot
print(s)

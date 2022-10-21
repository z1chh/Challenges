l = list(map(int, input().split()))

map1 = [set()] * (l[0] + 1)

connected = [False for _ in range(l[0]+1)]
connected[0] = True

for i in range(l[1]):
    inp = input().split()
    print(inp)
    a, b = map(int, inp)
    map1[a].add(b)
    map1[b].add(a)


def check_house(house_number):
    connected[house_number] = True
    for number in map1[house_number]:
        if connected[number] == False:
            check_house(number)


check_house(1)

every_house_connected = True

for i in range(1, l[0]+1):
    if connected[i] == False:
        every_house_connected = False
        print(i)

if every_house_connected:
    print("Connected")

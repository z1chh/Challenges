l = list(map(int, input().split()))
r = []
r.append(1 - l[0])
r.append(1 - l[1])
r.append(2 - l[2])
r.append(2 - l[3])
r.append(2 - l[4])
r.append(8 - l[5])
r = list(map(str, r))
print(" ".join(r))

x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x1 = x.pop()
if x1 in x:
    x.remove(x1)
    x1 = x[0]
y1 = y.pop()
if y1 in y:
    y.remove(y1)
    y1 = y[0]
print(x1, y1)

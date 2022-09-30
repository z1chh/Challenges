s = "allo"
for c in s:
    print(c)
    
if False and 1 / 0:
    print("True")
    
print(s[3])

print(int(5 / 2))

print(max([1, 2, 3, 4, 5, 6]))

def test():
    while True:
        try:
            print(int(input()))
        except:
            break

print(15 * 15 + 9 + 49)
print(13 * 13 + 49)

l = [1, 2, 3, 4]
l = l[0:len(l) - 1]
print(l)
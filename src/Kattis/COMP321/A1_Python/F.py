n = int(input())
o = input()
d = input()
if (n & 1):
    s = True
    for i in range(len(o)):
        if o[i] == d[i]:
            s = False
            break
    print("Deletion succeeded" if s else "Deletion failed")
else:
    print("Deletion succeeded" if o == d else "Deletion failed")

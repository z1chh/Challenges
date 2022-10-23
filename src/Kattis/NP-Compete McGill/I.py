s = input()
p = input()
if s == p:
    print("Yes")
elif s.swapcase() == p:
    print("Yes")
elif s[0].isdigit() and s[1:] == p:
    print("Yes")
elif s[-1].isdigit() and s[:-1] == p:
    print("Yes")
else:
    print("No")

left = True
right = True
tl = 0
tr = 0
bl = 0
br = 0
for _ in range(int(input())):
    s = input()
    if s[3] == "b":
        if s[0] == "+" or s[0] == "-":
            left = False
        else:
            right = False
    elif s[0] == "+":
        tl += 1
    elif s[0] == "-":
        bl += 1
    elif s[1] == "+":
        tr += 1
    else:
        br += 1
if left and (tl == 8 or bl == 8):
    left = False
if right and (tr == 8 or br == 8):
    right = False
if left:
    print(0)
elif right:
    print(1)
else:
    print(2)

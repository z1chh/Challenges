nb = int(input())
l = list(map(int, input().split()))
l.sort()
nl = ""
fe = False
first = l[0]
last = l[0]
row = False
for i in range(1, nb):
    # Get current bus
    bus = l[i]

    # Check if we have many buses in a row
    if (row):
        # Check if it still continues
        if bus == last + 1:
            last = bus
        else:
            row = False
            fe = True
            if first + 1 == last:
                nl += " {first} {last}".format(first=first, last=last)
            else:
                nl += " {first}-{last}".format(first=first, last=last)
            last = bus
    else:  # Not in a row
        # Check if we have new successsiono ihfiyufgbiraugjr
        if bus == last + 1:
            row = True
            first = last
            last = bus
        else:
            if not fe:
                nl += " {first}".format(first=last)
                fe = True
            else:
                nl += " {b}".format(b=last)
                fe = True
            last = bus

if row:
    if first + 1 == last:
        nl += " {first} {last}".format(first=first, last=last)
    else:
        nl += " {first}-{last}".format(first=first, last=last)
else:
    nl += " {l}".format(l=last)
print(nl[1:])

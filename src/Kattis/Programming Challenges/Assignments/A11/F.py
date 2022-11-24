c = 1
while True:
    try:
        x, y, r = map(float, input().split())
    except:
        break
    ax, ay = x, y
    out = False
    for _ in range(int(r)):
        if (ax**2 + ay**2)**0.5 >= 2:
            out = True
            break
        ax, ay = ax**2 - ay**2 + x, 2*ax*ay + y
    print(f"Case {c}: OUT" if out else f"Case {c}: IN")
    c += 1

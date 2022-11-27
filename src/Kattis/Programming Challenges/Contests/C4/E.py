def turn(i, s):
    if s == "Left":
        i -= 1
    elif s == "Right":
        i += 1
    if i < 0:
        i += 4
    if i > 3:
        i -= 4
    return i


def proc(x, y, ins):
    cx, cy = 0, 0
    d = 0
    for i in ins:
        if i == "Forward":
            if d == 0:
                cy += 1
            elif d == 1:
                cx += 1
            elif d == 2:
                cy -= 1
            else:
                cx -= 1
        else:
            d = turn(d, i)
    if cx == x and cy == y:
        return True
    return False

def main():
    x, y = map(int, input().split())
    n = int(input())
    instructions = [input() for _ in range(n)]
    for idx, ins in enumerate(instructions):
        m1, m2 = '', ''
        if ins == "Forward":
            m1, m2 = "Left", "Right"
        elif ins == "Left":
            m1, m2 = "Right", "Forward"
        else:
            m1, m2 = "Forward", "Left"
        ni = instructions.copy()
        ni[idx] = m1
        if proc(x, y, ni):
            print(idx + 1, m1)
            return
        else:
            ni[idx] = m2
            if proc(x, y, ni):
                print(idx + 1, m2)
                return


if __name__ == "__main__":
    main()

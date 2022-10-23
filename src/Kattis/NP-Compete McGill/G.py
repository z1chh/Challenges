def proofs():
    lines = int(input())
    ass = set()
    for i in range(1, lines + 1):
        arrow = False
        line = input().split()
        for word in line:
            if arrow:
                ass.add(word)
            else:
                if word == "->":
                    arrow = True
                else:
                    if word not in ass:
                        print(i)
                        return
    print("correct")
    return
proofs()

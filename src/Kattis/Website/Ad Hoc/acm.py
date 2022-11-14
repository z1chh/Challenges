score = 0
solved = 0
probs = {}
while True:
    line = input()
    if line == "-1":
        break
    t, p, r = line.split()
    if r == "right":
        solved += 1
        score += int(t)
        if p in probs:
            score += probs[p] * 20
    else:
        if p in probs:
            probs[p] += 1
        else:
            probs[p] = 1
print(solved, score)

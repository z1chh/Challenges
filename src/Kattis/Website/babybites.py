size = int(input())
st = input().split()
fishy = False
for i in range(size):
    word = st[i]
    if word == "mumble":
        continue
    else:
        word = int(word)
        if word != i + 1:
            fishy = True
            break

print("something is fishy" if fishy else "makes sense")

import math


def decrypt(msg, source_language):
    to_return = 0
    i = len(msg) - 1
    ct = 0
    while i >= 0:
        c = msg[i]
        index = -1
        for ind in range(len(source_language)):
            if c == source_language[ind]:
                index = ind
                break
        to_return += index * math.pow(len(source_language), ct)
        ct += 1
        i -= 1
    return int(to_return)


def encrypt(num, target_language):
    base = len(target_language)
    s = ""
    q = int(num / base)
    r = int(num % base)
    while q > 0:
        s += target_language[r]
        num = q
        q = int((num) / base)
        r = int(num % base)
    s += target_language[r]
    return s[::-1]

for i in range(1, int(input()) + 1):
    alien_number, source_language, target_language = input().split()
    num = decrypt(alien_number, source_language)
    s = encrypt(num, target_language)

    # Output message
    print("Case #{c}: {msg}".format(c=i, msg=s))

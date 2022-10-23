n = int(input())
toreturn = []
result = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        result.append(i - 1)
        result.append(n//i - 1)
for num in sorted(result):
    if str(num) not in toreturn:
        toreturn.append(str(num))
print(' '.join(toreturn))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
number = int(input())
divisors = 0
divisor = 2
while number > 1:
    while number % divisor == 0:
        divisors += 1
        number /= divisor
    divisor += 1
print(divisors)

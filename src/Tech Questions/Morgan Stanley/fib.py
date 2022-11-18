#include <iostream>
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def main():
    print(fib(5))
    print(fib(10))

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    fibNumbers = list()
    fibNumbers.append(0)
    fibNumbers.append(1)
    for _ in range(n - 2):
        fibNumbers.append(fibNumbers[-1] + fibNumbers[-2])
    return fibNumbers[-1]


if __name__ == '__main__':
    main()

# [0, 1, 1, 2, 3, 5]
#        1  2  3  4

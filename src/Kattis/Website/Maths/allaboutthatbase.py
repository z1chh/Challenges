import math


# Hardcode sue me
d = {'1': 1, '0': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10, 'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15, 'f': 16, 'g': 17, 'h': 18,
     'i': 19, 'j': 20, 'k': 21, 'l': 22, 'm': 23, 'n': 24, 'o': 25, 'p': 26, 'q': 27, 'r': 28, 's': 29, 't': 30, 'u': 31, 'v': 32, 'w': 33, 'x': 34, 'y': 35, 'z': 36}

value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17,
         'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35}

ops = {"+", "-", "*", "/", "="}

map_back = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i',
            19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z', 36: '0'}

# For each test case
for _ in range(int(input())):
    # Get input
    equation = input().split()

    # Get lowest base possible
    min_base = 1
    for i in range(0, 5, 2):
        for c in equation[i]:
            if d[c] > min_base:
                min_base = d[c]

    # Check from min_base to base 36
    possible_bases = []
    for base in range(min_base, 37):
        num1 = 0
        num2 = 0
        op = equation[1]
        num3 = 0

        # Get num1
        for idx, c in enumerate(equation[0][::-1]):
            num1 += math.pow(base, idx) * value[c]

        # Get num2
        for idx, c in enumerate(equation[2][::-1]):
            num2 += math.pow(base, idx) * value[c]

        # Get num3
        for idx, c in enumerate(equation[4][::-1]):
            num3 += math.pow(base, idx) * value[c]

        # Check if equation valid
        if op == "+":
            if num1 + num2 == num3:
                possible_bases.append(base)
        elif op == "-":
            if num1 - num2 == num3:
                possible_bases.append(base)
        elif op == "*":
            if num1 * num2 == num3:
                possible_bases.append(base)
        elif op == "/":
            if num1 / num2 == num3:
                possible_bases.append(base)
        else:
            raise ValueError(f"Error: inlalid operator {op}")

    # Check if any possible base
    if not possible_bases:
        print("invalid")
    else:
        print(''.join(map(lambda x: map_back[x], possible_bases)))

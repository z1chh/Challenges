#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaximumMEX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMaximumMEX(arr):
    arr.sort()
    n = 0
    for idx, v in enumerate(arr):
        if n <= v:
            arr[idx] = n
            n += 1
    return arr[-1] + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getMaximumMEX(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

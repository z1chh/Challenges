import math
import os


#
# Complete the 'getOneBits' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def getOneBits(n):
    binary = list()
    count = 0
    
    while n > 0:
        binary.append(o := n & 1)        # add right most bit
        count += o
        n = n >> 1                       # div by 2 (shift right)
    binary.reverse()
    one_bits = [count]
    
    for index, bit in enumerate(binary):
        if bit:
            one_bits.append(index + 1)
    return one_bits
if __name__ == '__main__':
    print(getOneBits(10))

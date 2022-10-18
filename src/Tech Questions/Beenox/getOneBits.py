import math
import os


#
# Complete the 'getOneBits' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def getOneBits(n):
    binary = []
    count = 0

    # Divide the number by two and store the remainder in binary
    while n > 0:
        binary.append(o := n & 1)
        count += o
        n = n >> 1
    
    # Reverse binary to get the binary representation of the number
    binary.reverse()
    
    # Add the number of one bits to the array, and their positions in the number
    one_bits = [count]
    for index, bit in enumerate(binary):
        if bit:
            one_bits.append(index + 1)
    
    # Return the number of one bits and their positions in the binary representation
    return one_bits


if __name__ == '__main__':
    print(getOneBits(10))

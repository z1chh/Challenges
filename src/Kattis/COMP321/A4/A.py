import numpy as np


# Main function
def radio_commercials():
    # Get input
    num_breaks, break_price = list(map(int, input().split()))
    students_per_break = list(map(int, input().split()))
    
    # Create new DP array
    sequences = np.zeros((num_breaks, num_breaks), int)
    
    # Find best sequences
    best_profit = -1
    
    # Initialize first row
    for i in range(num_breaks):
        tmp = students_per_break[i] - break_price
        sequences[0][i] = tmp
        if tmp > best_profit:
            best_profit = tmp
            
    # Compute for sequences of breaks
    for i in range(num_breaks):
        for j in range(i, num_breaks):
            tmp = sequences[i - 1][j - 1] + sequences[0][j]
            sequences[i][j] = tmp
            if tmp > best_profit:
                best_profit = tmp
                
    # Output profit
    print(best_profit)


# DELETE
def test():
    return np.zeros((3, 3), int)


# Main
if __name__ == "__main__":
    radio_commercials()
    # print(test())

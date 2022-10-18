"""
Function that updates the buildings left after a knock (the creature that knocks is determined by left_side (bool))
"""


def update(height, left_creature, right_creature, num_knocks, left_side):
    # Remove first element of creature
    if left_side:
        left_creature.pop(0)
    else:
        right_creature.pop(0)

    # Remove buildings from height
    for _ in range(num_knocks):
        height.pop(0)

    # Update other creature
    if left_side:
        for _ in range(num_knocks):
            # Check if sublist is empty
            if right_creature[-1] == []:
                right_creature.pop()

            # Remove last element from last sublist
            right_creature[-1].pop()
    else:
        for _ in range(num_knocks):
            # Check if sublist is empty
            if left_creature[-1] == []:
                left_creature.pop()

            # Remove last element from last sublist
            left_creature[-1].pop()


"""
Helper Function
Takes height, left_creature, right_creature as input, and checks which creature should knock buildings first (greedy)

Greedy Approach -> The creature that can knock the most buildings knocks first
                -> In case of a tie, we compute each knock to explore both possibilities (exhaustive search type of way)
"""


def helper(height, left_creature, right_creature, num_knocks):
    # Return minimum number of blows -> Greedy Algorithm
    while height:
        # Increment number of knocks
        num_knocks += 1

        # As long as there are buildings left, neither left_creature nor right_creature should be empty
        next_left_knock = left_creature[0]
        next_right_knock = right_creature[0]
        left_knock_len = len(next_left_knock)
        right_knock_len = len(next_right_knock)

        # Check which creature should knock buildings
        if left_knock_len > right_knock_len:
            update(height, left_creature, right_creature, left_knock_len, True)
        elif left_knock_len < right_knock_len:
            update(height, left_creature, right_creature,
                   right_knock_len, False)
        else:
            tmp1 = height.copy()
            tmp_l = left_creature.copy()
            tmp_r = right_creature.copy()
            update(tmp1, tmp_l, tmp_r, left_knock_len, True)
            update(height, left_creature, right_creature,
                   right_knock_len, False)
            return num_knocks + min(getMinimumBlows(tmp1), getMinimumBlows(height))
    return num_knocks


"""
This function first computes the buildings that would be destroyed by each knock from each creatures, and then calls the helper that computes the number of moves
"""


def getMinimumBlows(height):
    # Get list of buildings destroyed for each knock from left-side creature
    left_creature = []
    tmp = height.copy()
    while tmp:
        last_building = tmp.pop(0)
        knock = [last_building]
        while tmp:
            if last_building < tmp[0]:
                last_building = tmp.pop(0)
                knock.append(last_building)
            else:
                break
        left_creature.append(knock)

    # Get list of buildings destroyed for each knock from right-side creature
    right_creature = []
    tmp = height.copy()
    while tmp:
        last_building = tmp.pop()
        knock = [last_building]
        while tmp:
            if last_building < tmp[-1]:
                last_building = tmp.pop()
                knock.append(last_building)
            else:
                break
        right_creature.append(knock)

    # For visualization
    # print(left_creature)
    # print(right_creature)

    return helper(height, left_creature, right_creature, 0)


if __name__ == '__main__':
    print(getMinimumBlows([1, 2, 3, 4, 3, 2, 3, 2, 1]))
    print(getMinimumBlows([1, 2, 3, 4, 8, 7, 6, 5]))
    print(getMinimumBlows([2, 1, 2]))
    print(getMinimumBlows([1, 2, 1, 2, 10, 9]))
    print(getMinimumBlows([22, 75, 26, 45, 72, 81, 47, 29, 97, 2, 75, 25, 82, 84, 17, 56, 32, 2, 28, 37, 57, 39, 18,
          11, 79, 6, 40, 68, 68, 16, 40, 63, 93, 49, 91, 10, 55, 68, 31, 80, 57, 18, 34, 28, 76, 55, 21, 80, 22, 45]))

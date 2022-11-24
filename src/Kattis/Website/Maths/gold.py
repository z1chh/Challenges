# Global variables
width, height = map(int, input().split())
validTiles = {'G', '.'}


# Helper functions
def display(grid):
    for line in grid:
        print(' '.join(line))


def toString(grid):
    s = ''
    for line in grid:
        s += ''.join(line)
    return s


def toMatrix(grid):
    m = [grid[i * width: i * width + width] for i in range(height)]
    return m


def play(grid, queue, visited, coins, backtrack):
    # Get current position
    h, w = -1, -1
    for i in range(height):
        for j in range(width):
            if grid[i * width + j] == 'P':
                h, w = i, j
                break

    # Make sure that position is found
    if h == -1 and w == -1:
        raise ValueError("Error: player not found")

    # First check if stuck because of traps
    if h > 0 and grid[(h - 1) * width + w] == 'T':
        return coins[grid]
    elif h < width and grid[(h + 1) * width + w] == 'T':
        return coins[grid]
    elif w > 0 and grid[h * width + (w - 1)] == 'T':
        return coins[grid]
    elif w < width and grid[h * width + (w + 1)] == 'T':
        return coins[grid]

    # Check top, bottom, left, right
    found = False

    # Check top
    if h > 0 and grid[(h - 1) * width + w] in validTiles:
        newGrid = [c for c in grid]
        newGrid[(h - 1) * width + w] = 'P'
        newGrid[h * width + w] = '.'
        newGrid = ''.join(newGrid)
        if newGrid not in visited:
            found = True
            queue.append(newGrid)
            visited.add(newGrid)
            if grid[(h - 1) * width + w] == 'G':
                coins[newGrid] = coins[grid] + 1
            else:
                coins[newGrid] = coins[grid]
            if newGrid not in backtrack:
                backtrack[newGrid] = set()
            backtrack[newGrid].add(grid)
            if coins[grid] < coins[newGrid]:
                coins[grid] = coins[newGrid]

    # Check bottom
    if h < width and grid[(h + 1) * width + w] in validTiles:
        newGrid = [c for c in grid]
        newGrid[(h + 1) * width + w] = 'P'
        newGrid[h * width + w] = '.'
        newGrid = ''.join(newGrid)
        if newGrid not in visited:
            found = True
            queue.append(newGrid)
            visited.add(newGrid)
            if grid[(h + 1) * width + w] == 'G':
                coins[newGrid] = coins[grid] + 1
            else:
                coins[newGrid] = coins[grid]
            if newGrid not in backtrack:
                backtrack[newGrid] = set()
            backtrack[newGrid].add(grid)
            if coins[grid] < coins[newGrid]:
                coins[grid] = coins[newGrid]

    # Check left
    if w > 0 and grid[h * width + (w - 1)] in validTiles:
        newGrid = [c for c in grid]
        newGrid[h * width + (w - 1)] = 'P'
        newGrid[h * width + w] = '.'
        newGrid = ''.join(newGrid)
        if newGrid not in visited:
            found = True
            queue.append(newGrid)
            visited.add(newGrid)
            if grid[h * width + (w - 1)] == 'G':
                coins[newGrid] = coins[grid] + 1
            else:
                coins[newGrid] = coins[grid]
            if newGrid not in backtrack:
                backtrack[newGrid] = set()
            backtrack[newGrid].add(grid)
            if coins[grid] < coins[newGrid]:
                coins[grid] = coins[newGrid]

    # Check right
    if w < width and grid[h * width + (w + 1)] in validTiles:
        newGrid = [c for c in grid]
        newGrid[h * width + (w + 1)] = 'P'
        newGrid[h * width + w] = '.'
        newGrid = ''.join(newGrid)
        if newGrid not in visited:
            found = True
            queue.append(newGrid)
            visited.add(newGrid)
            if grid[h * width + (w + 1)] == 'G':
                coins[newGrid] = coins[grid] + 1
            else:
                coins[newGrid] = coins[grid]
            if newGrid not in backtrack:
                backtrack[newGrid] = set()
            backtrack[newGrid].add(grid)
            if coins[grid] < coins[newGrid]:
                coins[grid] = coins[newGrid]

    # Check if move was found
    if found:
        return -1
    else:
        for game in backtrack[grid]:
            queue.append(game)
            backtrack[grid] = set()
        return coins[grid]


# Main function
def main():
    # Initialize grid -> width and height read from input at line 2
    grid = ''
    for _ in range(height):
        grid += input()
    queue = [grid]
    visited = set()
    backtrack = {}
    backtrack[grid] = set()
    coins = {}
    coins[grid] = 0
    maxCoins = set()

    while queue:
        newGrid = queue.pop()
        outcome = play(newGrid, queue, visited, coins, backtrack)
        if outcome != -1:
            maxCoins.add(outcome)

    print(max(maxCoins))


# Run main
if __name__ == "__main__":
    main()

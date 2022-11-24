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


def toMatrix(grid, width, height):
    m = [grid[i * width: i * width + width] for i in range(height)]
    return m


def play(grid, queue, visited):
    # Get current position
    h, w = -1, -1
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 'P':
                h, w = i, j
                break

    # Make sure that position is found
    if h == -1 and w == -1:
        raise ValueError("Error: player not found")

    # Check top
    if h > 0 and grid[h - 1][w] in validTiles:
        newGrid = [line.copy() for line in grid]
        newGrid[h - 1][w] = 'P'
        newGrid[h][w] = '.'
        newGrid = toString(newGrid)
        queue.append(newGrid)
        visited.add(newGrid)

    # Check bottom
    if h < width and grid[h + 1][w] in validTiles:
        newGrid = [line.copy() for line in grid]
        newGrid[h + 1][w] = 'P'
        newGrid[h][w] = '.'
        newGrid = toString(newGrid)
        queue.append(newGrid)
        visited.add(newGrid)

    # Check left
    if w > 0 and grid[h][w - 1] in validTiles:
        newGrid = [line.copy() for line in grid]
        newGrid[h][w - 1] = 'P'
        newGrid[h][w] = '.'
        newGrid = toString(newGrid)
        queue.append(newGrid)
        visited.add(newGrid)

    # Check right
    if w < width and grid[h][w + 1] in validTiles:
        newGrid = [line.copy() for line in grid]
        newGrid[h][w + 1] = 'P'
        newGrid[h][w] = '.'
        newGrid = toString(newGrid)
        queue.append(newGrid)
        visited.add(newGrid)


# Main function
def main():
    grid = [[c for c in input()] for _ in range(height)]
    queue = [toString(grid)]
    visited = set()

    while queue:
        newGrid = queue.pop()
        visited.add(newGrid)


# Run main
if __name__ == "__main__":
    main()

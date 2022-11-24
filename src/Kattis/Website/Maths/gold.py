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


width, height = map(int, input().split())
grid = [[c for c in input()] for _ in range(height)]


display(grid)

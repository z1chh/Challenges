def gettingGold(grid, width, height, visited):
    # Set amount of gold to 0
    gold = 0

    # Find start position
    x, y = -1, -1
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "P":
                x, y = i, j
                break

    # Assert position found (should always be found)
    if x == -1 and y == -1:
        raise ValueError("Error: player not found")

    # Initialize queue and visited tiles
    queue = [(x, y)]
    visited[x][y] = True

    # Loop while there are still tiles to visit
    while queue:
        x, y = queue.pop(0)

        # Check if gold found
        if grid[x][y] == "G":
            gold += 1

        # Check if trap nearby
        if grid[x - 1][y] == "T" or grid[x + 1][y] == "T" or grid[x][y - 1] == "T" or grid[x][y + 1] == "T":
            continue

        # Check top
        if (grid[x - 1][y] == "." or grid[x - 1][y] == "G") and not visited[x - 1][y]:
            queue.append((x - 1, y))
            visited[x - 1][y] = True

        # Check bottom
        if (grid[x + 1][y] == "." or grid[x + 1][y] == "G") and not visited[x + 1][y]:
            queue.append((x + 1, y))
            visited[x + 1][y] = True

        # Check left
        if (grid[x][y - 1] == "." or grid[x][y - 1] == "G") and not visited[x][y - 1]:
            queue.append((x, y - 1))
            visited[x][y - 1] = True

        # Check right
        if (grid[x][y + 1] == "." or grid[x][y + 1] == "G") and not visited[x][y + 1]:
            queue.append((x, y + 1))
            visited[x][y + 1] = True

    # Return amount of gold found
    return gold


def main():
    # Get width and height
    width, height = map(int, input().split())

    # Initialize game map
    grid = [[c for c in input()] for _ in range(height)]

    # Initialize visited tiles
    visited = [[False for _ in range(width)] for _ in range(height)]

    # Solve
    print(gettingGold(grid, width, height, visited))


if __name__ == "__main__":
    main()

from collections import deque


# Get input
n, h, l = map(int, input().split())

# Create new graph
adjacent_nodes = []
for _ in range(n):
    adjacent_nodes.append([])
unvisited_nodes = set()
for i in range(n):
    unvisited_nodes.add(i)

# Create queue for nodes to visit during BFS
queue = deque()

# Populate graph
for s in map(int, input().split()):
    unvisited_nodes.remove(s)
    queue.append((0, s))
for _ in range(l):
    u, v = map(int, input().split())
    adjacent_nodes[v].append(u)
    adjacent_nodes[u].append(v)

# Compute BFS and output result
c, i = -1, -1
while queue:
    cost, v = queue.popleft()
    if cost > c or (cost == c and v < i):
        c, i = cost, v
    for u in adjacent_nodes[v]:
        if u in unvisited_nodes:
            unvisited_nodes.remove(u)
            queue.append((cost + 1, u))
if not unvisited_nodes:
    print(i)
else:
    print(min(unvisited_nodes))

# Get input
qs, bc = map(int, input().split())
q = {}

# Sort customers by maximum time of arrival
for i in range(qs):
    c, t = map(int, input().split())
    q.setdefault(t, []).append(c)

# Greedy algorithm from the end
m = 0
pc = []
for t in range(bc - 1, -1, -1):
    # Get all the customers that can get in at time t
    if t in q.keys():
        for c in q[t]:
            # Add them to list of potential customers
            pc.append(c)
    # Get the best customer at the current time
    if pc:
        m += max(pc)
        pc.remove(max(pc))
print(m)

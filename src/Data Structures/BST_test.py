from BST import BST
a = BST()
assert not a and len(a) == 0
try:
    y = a.get('x')
except KeyError as e:
    assert str(e) == "'x'"
else:
    raise Exception("KeyError not generated!")
s = 'cadbe'
for i, c in enumerate(s):
    a.put(c, i * 100)
assert a.depth() == 3
assert a and len(a) == len(s)
for i, c in enumerate(s):
    assert c in a and a.get(c) == i * 100
a.put('k', 0)
assert 'k' in a and a.get('k') == 0
assert len(a) == len(s) + 1
try:
    y = a.get('z')
except KeyError as e:
    assert str(e) == "'z'"
else:
    raise Exception("KeyError not generated!")

# ADD TESTS FOR YOUR NEW FUNCTIONALITY AFTER THIS LINE.
a = BST()
a.put('z', 1)
a.put('a', 0)
a.put('b', 10)
a.put('c', 0)

assert a.get('a') == 0, \
    "get error"
assert a.minKey() == 'a', \
    "min error"
assert a.maxKey() == 'z', \
    "max error"
assert a.__repr__() == "{'a':0,'b':10,'c':0,'z':1}", \
    "repr error"
print("All tests passed.")

# This code implements the performance testing you should comment on.
# For each value of n, it creates M different trees by randomizing the order
# of the integers from 0..n-2, then it computes the minimum, maximum, and mean
# depth of the M different trees.
#
from random import shuffle
M = 100 # number of trees to create per value of N
n = 16  # starting number of nodes
print("N   MIN MAX  MEAN")
while n < 512:
    stats = []
    data = list(range(n-1)) # generate a list of N-1 ints from 0 to N-2.
    for i in range(M):      # create M different trees
        bst = BST()             # create empty BST
        shuffle(data)           # randomize the data
        for x in data:          # build the tree
            bst.put(x)
        stats.append(bst.depth())
    print('{:3d} {:3d} {:3d} {:5.2f}'.format(n-1, min(stats), max(stats), sum(stats)/M))
    n *= 2

"""
1. For any given value of N, the worst case behavior is always almost two times worse than the best, if not reaching 2x.
2. It seems that the depths scale in relation to the N by its logarithm.
3. The average performance is always closer to the minimum depth, so normally, the performance are closer to the best
case behavior.
"""

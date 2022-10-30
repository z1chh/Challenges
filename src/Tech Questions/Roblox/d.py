def alloPolo(memory, x):
    start = -1
    size = 0
    for idx, mem in enumerate(memory):
        if size == 0:
            if mem == 0:
                size = 1
                start = idx
                if size == x:
                    return start
        else:
            if mem == 0:
                size += 1
                if size == x:
                    return start
            else:
                size = 0
    return -1


def solution(memory, queries):
    counter = 1
    ops = []
    d = {}
    for code, val in queries:
        if code == 0:
            start = alloPolo(memory, val)
            ops.append(start)
            if start != -1:
                for i in range(start, start + val):
                    memory[i] = 1
                d[counter] = (start, val)
                counter += 1
        else:
            if val in d:
                start, size = d[val]
                ops.append(size)
                for i in range(start, start + size):
                    memory[i] = 0
                d.pop(val)
            else:
                ops.append(-1)
    return ops

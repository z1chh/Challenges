def helper(rectangle, box):
    x1, y1 = rectangle
    x2, y2 = box
    if x2 <= x1 and y2 <= y1:
        return True
    if x2 <= y1 and y2 <= x1:
        return True
    return False


def solution(operations):
    to_return = []
    rectangles = set()
    for inp in operations:
        op, x, y = inp
        if op == 0:
            rectangles.add((x, y))
        else:
            fits = True
            for rec in rectangles:
                fits = helper(rec, (x, y))
                if not fits:
                    break
            to_return.append(fits)
    return to_return

# NOTE: I GET TLE

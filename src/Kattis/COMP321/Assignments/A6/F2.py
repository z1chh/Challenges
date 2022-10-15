class State:
    def __init__(self, last_pos, cur_pos) -> None:
        self._last_pos = last_pos
        self._cur_pos = cur_pos

    def move(self, new_pos) -> bool:
        if self._cur_pos > new_pos:
            if abs(self._cur_pos - self._last_pos) == self._cur_pos - new_pos:
                self._last_pos = self._cur_pos
                self._cur_pos = new_pos
            else:
                raise ValueError("Error: invalid move")
        elif self._cur_pos < new_pos:
            if abs(self._cur_pos - self._last_pos) == 2 * new_pos - self._cur_pos:
                self._last_pos = self._cur_pos
                self._cur_pos = new_pos
            else:
                raise ValueError("Error: invalid move")
        else:
            raise ValueError("Error: invalid move")


def nikola(state, squares, dest):
    # Check if destination is reached
    if state[1] == dest:
        return 0
    # BRO IDK WHAT TO DO AFTER THIS
    # I NEED SOME MEMORY TYPA SHII TO KEEP TRACK OF WHAT I ALREADY CHECKED


dest = int(input())
squares = [int(input()) for _ in range(dest)]
print(nikola(State(0, 1), squares, dest))

from curses import newpad
from gettext import npgettext


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


def nikola(state, squares):
    pass


squares = [int(input()) for _ in range(int(input()))]
print(nikola(State(0, 1), squares))
# Do something idk what
# Starts at square 1
# Must move to square 2 as first move

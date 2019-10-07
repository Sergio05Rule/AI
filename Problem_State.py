import sys

class State:
    def __init__(self, t):
        self.pos = t
        self.x = t[0]
        self.y = t[1]

    def print_state(self):
        print(self.pos)
        print(self.x)
        print(self.y)


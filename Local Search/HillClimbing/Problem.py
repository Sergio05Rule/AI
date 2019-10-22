import State
from HillClimbing import Node


class Problem:

    def __init__(self, initial_state):

        self.initial_state = initial_state


    def neighborhood(self, node):

        neighborhood = []
        for col in range(0,8):
            for spot in range(1,9):
                if node.chess.chess[col] != spot:
                    neighbor = Node(node.chess.change_position(col, spot))
                    neighborhood.append(neighbor)
        return neighborhood

    def print_nei(self, node):

        for nei in self.neighborhood(node):
            nei.chess.print_chess()
            print(nei.utility)

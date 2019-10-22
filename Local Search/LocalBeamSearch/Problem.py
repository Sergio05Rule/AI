from State import State
from LocalBeamSearch import Node


class Problem:

    def __init__(self, individuals):

        self.population = []
        self.random_population(individuals)

    def random_population(self, individuals):

        for x in range(individuals):

            new_state = State()
            new_node = Node(new_state)
            self.population.append(new_node)

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

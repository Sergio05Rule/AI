from State import State
from Genetic import Node


class Problem:

    def __init__(self, individuals):

        self.population = []
        self.random_population(individuals)


    def random_population(self, individuals):

        for x in range(individuals):

            new_state = State()
            new_node = Node(new_state)
            self.population.append(new_node)

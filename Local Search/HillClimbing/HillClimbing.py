from random import randint
from State import State

class Node:

    def __init__(self, state):

        self.chess = state
        self.utility = state.utility_function()



class Hill_Climbing():

    def __init__(self, problem):

        self.problem = problem
        self.node = Node(problem.initial_state)

    def restart(self):

        while 1:
            solution = self.fit()
            if solution.utility == 0:
                return solution
            new_state = State()
            new_start = Node(new_state)
            self.node = new_start
            print('RESTARTING')


    def fit(self):

        while(1):

            next_step = self.next_step()
            if next_step == 0:
                return self.node
            else:
                self.node = next_step[0]



    def next_step(self):

        # COSTRUISCI I VICINI DELLO STATO
        neighborhood = self.problem.neighborhood(self.node)

        # SELEZIONA UNO CON UTILITY PIÙ BASSA
        candidates = self.candidates(neighborhood)

        if candidates[1] < self.node.utility:
            print('Found better chess with utility', candidates[1])

            # ----- SCELGO RANDOMICAMENTE UNA DELLE SUCCESSIVE MIGLIORI SCACCHIERE -----
            random_min = randint(0, len(candidates[0]) - 1)
            random_node = candidates[0][random_min]
            next_node = neighborhood[random_node]

            return (next_node,candidates[1])
        else:
            return 0

    def candidates(self, neighborhood):
        utility_values = []

        for neighbour in neighborhood:
            utility_values.append(neighbour.utility)

        min_utility = min(utility_values)

        candidates = []
        for index, neighbour in enumerate(neighborhood):
            if neighbour.utility == min_utility:
                candidates.append(index)
        return (candidates, min_utility)






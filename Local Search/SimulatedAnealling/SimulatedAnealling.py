from random import randint
from State import State
from math import e


class Node:

    def __init__(self, state):

        self.chess = state
        self.utility = state.utility_function()



class Simulated_Anealling():

    def __init__(self, problem):

        self.problem = problem
        self.node = Node(problem.initial_state)
        self.iterations = 1
        self.alfa = 1
        self.k = 1


    def fit(self):

        while (1):
            print('Iteration: ',self.iterations)
            next_step = self.next_step()
            # ----- STOPPING CONDITION -----
            if next_step == 0:
                print('STOPPING CONDITION: MAX ITERATIONS = 1000')
                return 0
            # ----- SOLUTION FOUND -----
            if next_step.utility == 0:
                return next_step
            print('NEW CHESS WITH UTILITY: ',next_step.utility)
            next_step.chess.print_chess()
            self.node = next_step
            self.iterations += 1




    def next_step(self):

        # COSTRUISCI I VICINI DELLO STATO
        neighborhood = self.problem.neighborhood(self.node)

        while (1):
            if self.iterations > 1000:
                return 0

            # SELEZIONA UNO RANDOMICAMENTE TRA I VICINI
            random_selection = randint(0, len(neighborhood)-1)

            next_step = neighborhood[random_selection]

            probability = randint(0,100) / 100

            if self.stochastic_step(next_step) > probability:
                return next_step


    def stochastic_step(self, node):

        error = self.node.utility - node.utility
        exponential = error * self.k * self.iterations
        probability = self.alfa * e ** exponential

        if error > 0:
            return 1
        else:
            return probability









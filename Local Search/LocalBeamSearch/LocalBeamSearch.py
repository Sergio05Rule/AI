from random import randint
from State import State
from math import e

class Node:

    def __init__(self, state):

        self.chess = state
        self.utility = state.utility_function()

class Local_Beam_Search():

    def __init__(self, problem):

        self.problem = problem
        self.population = problem.population.copy()

        self.iterations = 1
        self.alfa = 1
        self.k = 0.5

    def fit(self):

        while(1):

            next_step = self.next_step()
            if next_step != 0:
                return next_step

    def next_step(self):

        neighborhood = list()
        for individual in self.population:
            # COSTRUISCI I VICINI DEGLI STATI
            neighborhood = neighborhood + self.problem.neighborhood(individual)

        next_population = self.candidates(neighborhood)

        for individual in next_population:
            if individual.utility == 0:
                return individual
        self.population = next_population
        self.iterations += 1
        return 0

    def candidates(self, neighborhood):

        candidates = list()
        while len(candidates) != len(self.population):
            random_neighbour = randint(0, len(neighborhood) - 1)
            pick = neighborhood[random_neighbour]
            if self.stochastic_selection(neighborhood, pick):
                candidates.append(pick)
        return candidates

    def stochastic_selection(self, neighborhood, pick):

        utility_values = list()
        for neighbour in neighborhood:
            utility_values.append(neighbour.utility)

        min_utility = min(utility_values)
        pick_utility = pick.utility
        error = min_utility - pick_utility
        probability  = self.alfa * e**(error*self.k*self.iterations)

        random_probability = randint(0,99) / 100

        if random_probability < probability:
            return 1
        else:
            return 0



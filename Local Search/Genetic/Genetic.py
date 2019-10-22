from random import randint
from State import State
from math import e


class Node:

    def __init__(self, state):

        self.chess = state
        self.fitness = state.fitness_function()

class Genetic_algorithm():

    def __init__(self, problem):

        self.problem = problem
        self.population = problem.population.copy()


    def fit(self):

        while(1):
            for individual in self.population:
                #print('individual: ',individual.chess.chess, 'with fitness = ', individual.fitness)
                if individual.fitness == 28:
                    return individual

            individuals = self.choose_individuals()
            #for individual in individuals:

                # print('CHOSEN ',len(individuals),' individuals: ', individual.chess.chess, 'with fitness:',individual.fitness)

            individuals = self.crossover(individuals)
            self.population = self.mutation(individuals)



    def choose_individuals(self):

        total_fitness = 0
        individuals = list()
        for ind in self.population:
            total_fitness += ind.fitness

        for iteration in range(len(self.population)):

            random_individual = randint(1,total_fitness)

            for ind in self.population:

                random_individual -= ind.fitness
                if random_individual <= 0:
                    individuals.append(Node(State(ind.chess.chess)))
                    break
        return individuals

    def crossover(self, individuals):

        couple = list()
        new_individuals = list()

        for ind in individuals:
            couple.append(ind)
            if len(couple) == 2:
                random_cut = randint(0,7)
                son1 = couple[0].chess.chess.copy()
                son2 = couple[1].chess.chess.copy()

                if random_cut != 0:
                    for index in range(8):
                        if index >= random_cut:
                            support = son1[index]
                            son1[index] = son2[index]
                            son2[index] = support
                    #print('With cut in ',random_cut)
                    #print('From\n',couple[0].chess.chess,'\n',couple[1].chess.chess)
                    #print('TO\n', son1, '\n', son2)

                new_individuals.append(Node(State(son1)))
                new_individuals.append(Node(State(son2)))
                couple.clear()
        return new_individuals


    def mutation(self, individuals):

        new_individuals = list()
        for ind in individuals:
            random_index = randint(0,8)
            if random_index == 8:
                new_individuals.append(ind)
            else:
                random_value = randint(1,8)
                new_chess = ind.chess.chess.copy()
                new_chess[random_index] = random_value
                new_individuals.append(Node(State(new_chess)))
        return new_individuals















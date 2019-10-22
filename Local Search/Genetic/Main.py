from Problem import Problem
from Genetic import *
from State import State


if __name__ == '__main__':

    problem = Problem(4)

    model = Genetic_algorithm(problem)
    solution = model.fit()

    print('----- SOLUTION -----')
    print('Fitness = ', solution.fitness)
    solution.chess.print_chess()

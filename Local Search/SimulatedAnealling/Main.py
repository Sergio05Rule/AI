from Problem import Problem
from SimulatedAnealling import *
from State import State


if __name__ == '__main__':

    initial_state = State()           # stato iniziale randomico
    problem = Problem(initial_state)

    model = Simulated_Anealling(problem)
    print('----- START -----')
    model.node.chess.print_chess()
    print('UTILITY = ',model.node.utility)

    solution = model.fit()
    if solution == 0:
        print('No solution found')
    else:
        print('SOLUTION')
        solution.chess.print_chess()
        print('UTILITY = ', solution.utility)

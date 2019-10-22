from Problem import Problem
from HillClimbing import *
import State


if __name__ == '__main__':

    initial_state = State.State()           # stato iniziale randomico
    problem = Problem(initial_state)

    model = Hill_Climbing(problem)
    print(model.node.chess.utility_function())
    print('Initial state')
    model.node.chess.print_chess()
    solution = model.restart()
    print('\nSOLUTION with utility: ',solution.utility)
    solution.chess.print_chess()

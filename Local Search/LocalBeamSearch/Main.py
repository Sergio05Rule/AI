from Problem import Problem
from LocalBeamSearch import *
import State


if __name__ == '__main__':

    initial_state = State.State()           # stato iniziale randomico
    problem = Problem(4)

    model = Local_Beam_Search(problem)

    solution = model.fit()

    print('----- SOLUTION -----')
    print('Fitness = ', solution.utility)
    solution.chess.print_chess()
import Problem_State as PS
import sys

# GRAPH PROBLEM


class Problem:
    def __init__(self, initial_state):

        self.initial_state = initial_state
        self.goal_state = [[1,2,3],[4,5,6],[7,8,0]]
        self.state_space = []


    def action(self, state):
        # restitutisce la lista delle azioni possibili
        action_list = []

        if (state.holeR > 0):
            action_list.append('Move TOP')
        if (state.holeR < 2):
            action_list.append('Move DOWN')
        if (state.holeC > 0):
            action_list.append('Move LEFT')
        if (state.holeC < 2):
            action_list.append('Move RIGHT')

        return action_list

    def result(self, state, action):
        # dato uno stato ed una azione restituisce il nuovo stato dopo aver eseguito l'azione
        if (action in self.action(state)):

            mat = PS.init_matrix(3,3)
            mat = PS.copy_matrix(state.matrix,3,3)
            new_state = PS.State(mat)

            if action == 'Move TOP':
                new_state.matrix[new_state.holeR][new_state.holeC] = state.matrix[new_state.holeR - 1][new_state.holeC]
                new_state.matrix[new_state.holeR - 1][new_state.holeC] = 0
                #PS.print_matrix(new_state.matrix,3,3)
                new_state.holeR = new_state.holeR - 1

            if action == 'Move DOWN':
                new_state.matrix[new_state.holeR][new_state.holeC] = new_state.matrix[new_state.holeR + 1][new_state.holeC]
                new_state.matrix[new_state.holeR + 1][new_state.holeC] = 0
                #PS.print_matrix(new_state.matrix,3,3)
                new_state.holeR = new_state.holeR + 1

            if (action == 'Move LEFT'):
                new_state.matrix[new_state.holeR][new_state.holeC] = new_state.matrix[new_state.holeR][new_state.holeC - 1]
                new_state.matrix[new_state.holeR][new_state.holeC - 1] = 0
                #PS.print_matrix(new_state.matrix,3,3)
                new_state.holeC = new_state.holeC - 1

            if (action == 'Move RIGHT'):
                new_state.matrix[new_state.holeR][new_state.holeC] = new_state.matrix[new_state.holeR][new_state.holeC + 1]
                new_state.matrix[new_state.holeR][new_state.holeC + 1] = 0
                new_state.holeC = new_state.holeC + 1

            return new_state

        else:
            print('Action not permitted for this state: ', action)
            sys.exit()


    def goal_test(self, state):
        # verifica se lo stato passato è il goal state
        if state.matrix[0][0] == 1 and state.matrix[0][1] == 2 and state.matrix[0][2] == 3 and state.matrix[1][0] == 4 and state.matrix[1][1] == 5 and state.matrix[1][2] == 6 and state.matrix[2][0] == 7 and state.matrix[2][1] == 8 and state.matrix[2][2] == 0:
            return 1
        else:
            return 0

    def path_cost(self, node, action):

        return node.path_cost + 1

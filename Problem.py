import Problem_State as PS
import sys

class Problem:
    def __init__(self, initial_state , goal_state, labyrinth):

        self.initial_state = initial_state
        self.goal_state = goal_state
        self.labyrinth = labyrinth
        self.state_space = []

    def action(self, state):
        # restitutisce la lista delle azioni possibili
        action_list = []

        if (self.labyrinth.check_top(state.x, state.y)): #is == 1
            #print('from', state.pos, '->TOP')
            action_list.append('Move TOP')

        if (self.labyrinth.check_down(state.x, state.y)): #is == 1
            #print('from', state.pos, '->DOWN')
            action_list.append('Move DOWN')

        if (self.labyrinth.check_left(state.x, state.y)): #is == 1
            #print('from', state.pos, '->LEFT')
            action_list.append('Move LEFT')

        if (self.labyrinth.check_right(state.x, state.y)): #is == 1
            #print('from', state.pos, '->RIGHT')
            action_list.append('Move RIGHT')

        return action_list

    def result(self, state, action):
        # dato uno stato ed una azione restituisce il nuovo stato dopo aver eseguito l'azione
        if (action in self.action(state)):

            new_state = PS.State((0,0))

            if action == 'Move TOP':
                new_state.x = state.x - 1
                new_state.y = state.y
                new_state.pos = (new_state.x, new_state.y)

            if action == 'Move DOWN':
                new_state.x = state.x + 1
                new_state.y = state.y
                new_state.pos = (new_state.x, new_state.y)

            if (action == 'Move LEFT'):
                new_state.x = state.x
                new_state.y = state.y - 1
                new_state.pos = (new_state.x, new_state.y)

            if (action == 'Move RIGHT'):
                new_state.x = state.x
                new_state.y = state.y + 1
                new_state.pos = (new_state.x, new_state.y)

            return new_state

        else:
            print('Action not permitted for this state: ', action)
            sys.exit()


    def goal_test(self, state):
        # verifica se lo stato passato è il goal state
        if state.pos == self.goal_state.pos:
            return 1
        else:
            return 0

    def path_cost(self, node, action):

        return node.path_cost + 1

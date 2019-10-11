import Problem_State as PS
import sys
import BF_Fringe as BF
import DF_Fringe as DF
import AS_Fringe as AS

class Problem:
    def __init__(self, N, M, K, V, initial_state, goal_state, fringe_type, limit=None): #TODO limit remove
        self.N = N
        self.M = M
        self.K = K
        self.V = V
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.closed = []
        self.created_nodes = 0 #TODO
        self.fringe_type = fringe_type
        self.limit = limit

        print('NEL PROBLEM HO LA LISTA DI MURI', V)

        if (fringe_type == 'BF'):
            self.fringe = BF.Fringe_list()
        if (fringe_type == 'DF'):
            self.fringe = DF.Fringe_list()
        if (fringe_type == 'AS'):
            self.fringe = AS.Fringe_list()

    def action(self, state): # restitutisce la lista delle azioni possibili

        action_list = []

        if (PS.check_obstacles(self.V, state, 'TOP', self.N, self.M)):  # is == 1
            action_list.append('Move TOP')

        if (PS.check_obstacles(self.V, state, 'DOWN', self.N, self.M) ):  # is == 1
            action_list.append('Move DOWN')

        if (PS.check_obstacles(self.V, state, 'LEFT', self.N, self.M) ):  # is == 1
            action_list.append('Move LEFT')

        if (PS.check_obstacles(self.V, state, 'RIGHT', self.N, self.M) ):  # is == 1
            action_list.append('Move RIGHT')

        return action_list

    def result(self, state, action):
        # dato uno stato ed una azione restituisce il nuovo stato dopo aver eseguito l'azione
        if (action in self.action(state)):

            new_state = PS.State((0, 0))

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


    def heuristic_func(self, state):

        return self.check_position_heu(state)

    def check_position_heu(self, state):

        return 0

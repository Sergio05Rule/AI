import Problem_State as PS
import sys
import BF_Fringe as BF
import DF_Fringe as DF
import UC_Fringe as UC
import GR_Fringe as GR
import AS_Fringe as AS

# GRAPH PROBLEM
class Problem:
    def __init__(self, graph, initial_state, goal_state, fringe_type):
        self.graph = graph
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.closed = []
        self.created_nodes = 0

        if (fringe_type == 'BF'):
            self.fringe = BF.Fringe_list()
        if (fringe_type == 'DF'):
            self.fringe = DF.Fringe_list()
        if (fringe_type == 'UC'):
            self.fringe = UC.Fringe_list()
        if (fringe_type == 'GR'):
            self.fringe = GR.Fringe_list()
        if (fringe_type == 'AS'):
            self.fringe = AS.Fringe_list()


    def action(self, state):
        # restitutisce la lista delle azioni possibili
        # restitutisce la lista delle azioni possibili
        action_list = []
        support = self.graph.get_vertex(state.id).get_connections()  # get children di Node
        for element in support:
            action_list.append(element.id)
        return action_list

    def result(self, state, action):
        # dato uno stato ed una azione restituisce il nuovo stato dopo aver eseguito l'azione
        if (action in self.action(state)):
            return PS.State(action)
        else:
            print('Action not permitted for this state')
            sys.exit()


    def goal_test(self, state):
        # verifica se lo stato passato è il goal state
        if state.id == self.goal_state.id:
            return 1
        else:
            return 0

    def path_cost(self, node, action):
        return node.path_cost + self.graph.get_vertex(node.state.id).get_weight(self.graph.get_vertex(action))

    def heuristic_func(self, state):

        return self.check_position_heu(state)

    def check_position_heu(self, state):

        return 0

    def manhattan_distance(self, state):

        return 0
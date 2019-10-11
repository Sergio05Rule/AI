import Problem_State as PS
import BF_Fringe as BF
import DF_Fringe as DF
import UC_Fringe as UC
import GR_Fringe as GR
import AS_Fringe as AS

# GRAPH PROBLEM


class Problem:
    def __init__(self, fringe_type):

        self.initial_state = PS.State([[1, 0, 0], [2, 0, 0], [3, 0, 0]])
        self.goal_state = PS.State([[0, 0, 1], [0, 0, 2], [0, 0, 3]])
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

        self.closed = []


    def action(self, state):
        # restitutisce la lista delle azioni possibili
        action_list = []

        tower = state.tower

        tops = PS.bricks_on_top(tower)

        for col in range(len(tower[0])):    # per ogni colonna

            if tops[col][0] != 0:           # controllo se c'è un brick da poter spostare

                for other_col in range(len(tower[0])):

                    if other_col != col:     # controllo le altre colonne

                        if tops[other_col][0] > tops[col][0] or tops[other_col][0] == 0:

                            action_list.append((col, other_col))

        return action_list

    def result(self, state, action):
        # dato uno stato ed una azione restituisce il nuovo stato dopo aver eseguito l'azione

        new_tower = PS.copy_matrix(state.tower, 3,3)
        new_state = PS.State(new_tower)

        column1 = action[0]
        column2 = action[1]


        tops = PS.bricks_on_top(state.tower)

        brick = tops[column1][0]
        pos1 = tops[column1][1]
        pos2 = tops[column2][1]


        if (tops[column2][0] == 0):
            pos2 = (3,column2)

        new_state.tower[pos2[0] - 1][pos2[1]] = brick
        new_state.tower[pos1[0]][pos1[1]] = 0

        return new_state


    def goal_test(self, state):
        # verifica se lo stato passato è il goal state
        if PS.compare_matrix(state.tower, self.goal_state.tower):
            return 1
        else:
            return 0

    def path_cost(self, node, action):

        return node.path_cost + 1

    def heuristic_func(self, state):

        return self.check_position_heu(state)

    def check_position_heu(self, state):

        return 0

    def manhattan_distance(self, state):
        distance = 0
        a = state.matrix
        b = self.goal_state
        for row in range(3):
            for col in range(3):
                element = b[row][col]
                for r in range(3):
                    for c in range(3):
                        if element == a[r][c]:
                            distance = distance + abs((r-row)) + abs((c-col))
        return distance


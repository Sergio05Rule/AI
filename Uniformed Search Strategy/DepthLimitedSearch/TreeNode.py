import DLS_Fringe as FL
import Problem_State as PS

#Library for Node Class

class Node:
    def __init__(self):
        self.state = None
        self.parent = None
        self.children = []
        self.depth = None
        self.path_cost = None
        self.action = None

    def root(self, root_state):
        self.state = root_state
        self.depth = 0
        self.path_cost = 0

    def create(self, state, parent, depth, path_cost, action):
        self.state = state
        self.parent = parent
        self.depth = depth + 1
        self.path_cost = path_cost
        self.action = action


def StateCompare (stateA, list):

    for node in list:
        if PS.compare_matrix(stateA.matrix, node.matrix):
            return 0
    return 1

def Expand(problem, node): # restitusice una serie di nodi da inserire nella FL

    actions = problem.action(node.state) # lista di azioni possibili
    tempFL = [] # lista temporanea dei nodi da aggiungere alla fringe
    flag = 0

    for action in actions:
        temp = problem.result(node.state, action)

        if StateCompare(temp, problem.state_space):
            tempN = Node()   # variabile temporanea di tipo nodo per inserire i nuovi nodi creati
            tempN.create(temp, node, node.depth, problem.path_cost(node,action), action) # assegna specifici valori alle variabili del nodo
            tempFL.append(tempN) # aggiunge il nodo alla lista dei nodi da inserire nella FL
            flag = 1 # è avvenuta una effettiva espansione quindi faccio print
    if flag:
        problem.state_space.append(node.state)

    return tempFL


def Tree_Search(problem, l):  # l is the depth limit for the Depth Limited Search Algorithm
    Fringe = FL.Fringe_list(l)
    root = Node()    # dichiarazione root_node
    root.root(problem.initial_state)      # inizializzazione root node
    Fringe.add(root)    # update fl w/ root_node

    while 1:
        if len(Fringe.list) == 0:
            return 1
        else:
            selected_node = Fringe.pop()

            if StateCompare(selected_node.state, problem.state_space):
                #print(' --- Checking\tnode\t', '---')
                if problem.goal_test(selected_node.state):
                    return selected_node

                new_fringe_nodes = Expand(problem, selected_node)

                for node in new_fringe_nodes:
                    Fringe.add(node)


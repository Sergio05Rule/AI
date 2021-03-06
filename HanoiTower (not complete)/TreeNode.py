import Problem_State as PS
import timeit

#Library for Node Class

class Node:
    def __init__(self):
        self.state = None
        self.parent = None      # il nodo parent è fondamentale per poter ricostruire il path fino al root
        self.depth = None       # indica la profondità del nodo
        self.path_cost = None   # è il path cost dal root al nodo attuale
        self.action = None      # indica l'azione che è fatto evolvere l'enviroment nello stato contenuto in questo nodo. Serve a poter ripercorrere le azioni che portano dal root al nodo attuale.
        self.heuristic = None

    def root(self, problem): # assegna ai parametri lo stato root_state e dei valori fissati per un nodo root
        self.state = problem.initial_state
        self.depth = 0
        self.path_cost = 0
        self.heuristic = None

    def create(self, problem, state, parent, depth, path_cost, action): # assegna i valori passati gli attributi di un nodo
        self.state = state
        self.parent = parent
        self.depth = depth + 1
        self.path_cost = path_cost
        self.action = action
        self.heuristic = None



def Expand(problem, node): # restitusice una serie di nodi da inserire nella FL

    actions = problem.action(node.state) # lista di azioni possibili
    tempFL = [] # lista temporanea dei nodi da aggiungere alla fringe list


    for action in actions:
        temp = problem.result(node.state, action)

        # ---------------- NUOVO NODO CREATO ----------------
        tempN = Node()   # variabile temporanea di tipo nodo per inserire i nuovi nodi creati
        problem.created_nodes += 1
        tempN.create(problem, temp, node, node.depth, problem.path_cost(node,action), action) # assegna specifici valori alle variabili del nodo
        tempFL.append(tempN) # aggiunge il nodo alla lista dei nodi da inserire nella FL

    return tempFL

def Tree

def Tree_Search(problem):  # l is the depth limit for the Depth Limited Search Algorithm

    Fringe = problem.fringe

    # ---------------- NUOVO NODO CREATO ----------------
    root = Node()    # dichiarazione root_node
    problem.created_nodes += 1
    root.root(problem)      # inizializzazione root node

    # ---------------- AGGIUNTA ROOT ALLA FRINGE ----------------
    Fringe.add(root)    # update fl w/ root_node
    print('aggiunto nodo root alla fringe ', root.state.tower)

    while 1:
        # ---------------- CONTROLLO ASSENZA SOLUZIONE ----------------
        if len(Fringe.list) == 0:
            return 1            #il Tree Search è terminato e non è andato a buon fine
        else:
            selected_node = Fringe.pop()            # seleziona il prossimo nodo della fringe list
            print('analizzo nodo: ', selected_node.state.tower)

            print('---------------- GOAL TEST CHECKING ----------------')
            # ---------------- GOAL TEST CHECKING ----------------
            if problem.goal_test(selected_node.state):
                return selected_node            # il Tree Search è terminato ed è andato a buon fine, viene restituito il nodo soluzione

            # espando se il nodo non soddisfa il goal test

            print('---------------- EXPAND ----------------')
            # ---------------- EXPAND ----------------
            new_fringe_nodes = Expand(problem, selected_node)           # effettua l'expand del nodo selezionato

            for x in new_fringe_nodes:

                print(x.state.tower)

            # ---------------- NUOVI NODI NELLA FRINGE ----------------
            for node in new_fringe_nodes:
                Fringe.add(node)            # aggiunge, uno alla volta, tutti i nodi restituiti dall'expand dell'ultimo nodo


def Graph_Search(problem):  # l is the depth limit for the Depth Limited Search Algorithm

    Fringe = problem.fringe

    # ---------------- NUOVO NODO CREATO ----------------
    root = Node()    # dichiarazione root_node
    problem.created_nodes += 1
    root.root(problem)      # inizializzazione root node

    # ---------------- AGGIUNTA ROOT ALLA FRINGE ----------------
    Fringe.add(root, problem)    # update fl w/ root_node

    while 1:
        # ---------------- CONTROLLO ASSENZA SOLUZIONE ----------------
        if len(Fringe.list) == 0:
            return 1            #il Tree Search è terminato e non è andato a buon fine
        else:
            selected_node = Fringe.pop()            # seleziona il prossimo nodo della fringe list

            # ---------------- GOAL TEST CHECKING ----------------
            if problem.goal_test(selected_node.state):
                return selected_node            # il Tree Search è terminato ed è andato a buon fine, viene restituito il nodo soluzione

            # espando se il nodo non soddisfa il goal test

            # ---------------- CONTROLLO NON SIA UN SOTTOALBERO GIÀ ATTRAVERSATO ----------------
            if PS.NotinClosed(problem, selected_node):

                # ---------------- EXPAND ----------------
                new_fringe_nodes = Expand(problem, selected_node)           # effettua l'expand del nodo selezionato

                # ---------------- AGGIUNGO AI NODI VISITATI ----------------
                problem.closed.append(selected_node.state)

            # ---------------- NUOVI NODI NELLA FRINGE ----------------
            for node in new_fringe_nodes:
                Fringe.add(node, problem)            # aggiunge, uno alla volta, tutti i nodi restituiti dall'expand dell'ultimo nodo


def Print_Path(node, time_start, problem):
    list = []           # lista dove memorizzare il nome dei nodi da stampare a video
    temp = node         # node contiene informazioni utili sulla depth e path cost del GOAL node
    flag = 0            # flag per il controllo del ciclo: vale 1 se trovo il nodo root
    print('')

    # Check if the solution is Failed
    if node == 1:
        print("Failed to find a valid solution!")
        return 0

    print('--- Path Finder ---')
    print('DEPTH: ', node.depth)

    return 0
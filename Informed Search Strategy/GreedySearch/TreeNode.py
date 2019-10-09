import UC_Fringe as FL
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
        self.heuristic = problem.heuristic_func(self.state)

    def create(self, problem, state, parent, depth, path_cost, action): # assegna i valori passati gli attributi di un nodo
        self.state = state
        self.parent = parent
        self.depth = depth + 1
        self.path_cost = path_cost
        self.action = action
        self.heuristic = problem.heuristic_func(state)



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


def Tree_Search(problem):  # l is the depth limit for the Depth Limited Search Algorithm
    Fringe = FL.Fringe_list()

    # ---------------- NUOVO NODO CREATO ----------------
    root = Node()    # dichiarazione root_node
    problem.created_nodes += 1
    root.root(problem)      # inizializzazione root node

    # ---------------- AGGIUNTA ROOT ALLA FRINGE ----------------
    Fringe.add(root)    # update fl w/ root_node

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

            # ---------------- EXPAND ----------------
            new_fringe_nodes = Expand(problem, selected_node)           # effettua l'expand del nodo selezionato

            # ---------------- NUOVI NODI NELLA FRINGE ----------------
            for node in new_fringe_nodes:
                Fringe.add(node)            # aggiunge, uno alla volta, tutti i nodi restituiti dall'expand dell'ultimo nodo


def Print_Path(node, time_start, problem):
    list = []           # lista dove memorizzare il nome dei nodi da stampare a video
    temp = node         # node contiene informazioni utili sulla depth e path cost del GOAL node
    flag = 0            # flag per il controllo del ciclo: vale 1 se trovo il nodo root
    print('')

    # Check if the solution is Failed
    if node == 1:
        print("Failed to find a valid solution!")
        return 0

    while 1:
        list.insert(0,temp)         # salvo in una lista i nodi del percorso: li inserisco all'indice 0 in modo da ottenere un ordine dal nodo iniziale a quello finale
        if temp.parent == None:         # riconosco il nodo root dall'essere l'unico senza un padre
            flag = 1
        else:
            temp = temp.parent          # passo al nodo padre per la prossima iterazione
        if flag :
            print('--- Path Finder ---'
                '\nI found a valid solution!'
                  '\nTime occured = ' , (timeit.default_timer() - time_start),
                  '\nPath Cost ='   , node.path_cost,
                  '\nTree Depth ='  , node.depth,
                  '\nNumber of nodes created =', problem.created_nodes)

            for index, x in enumerate(list):
                if index != 0:
                    print('\t↓\n', x.action,'\n\t↓')
                PS.print_matrix(x.state.matrix,3,3)
            return 0
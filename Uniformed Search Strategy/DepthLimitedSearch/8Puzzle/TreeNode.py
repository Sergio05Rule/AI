import DLS_Fringe as FL
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

    def root(self, root_state): # assegna ai parametri lo stato root_state e dei valori fissati per un nodo root
        self.state = root_state
        self.depth = 0
        self.path_cost = 0

    def create(self, state, parent, depth, path_cost, action): # assegna i valori passati gli attributi di un nodo
        self.state = state
        self.parent = parent
        self.depth = depth + 1
        self.path_cost = path_cost
        self.action = action


def StateCompare (stateA, list):  # effettua un confronto tra un nodo e una lista di nodi: se due nodi hanno lo stesso stato ritorna 0, altrimenti 1

    for node in list:
        if PS.compare_matrix(stateA.matrix, node.matrix):
            return 0
    return 1


def Expand(problem, node): # restitusice una serie di nodi da inserire nella FL

    actions = problem.action(node.state) # lista di azioni possibili
    tempFL = [] # lista temporanea dei nodi da aggiungere alla fringe list
    flag = 0

    for action in actions:
        temp = problem.result(node.state, action)

        tempN = Node()   # variabile temporanea di tipo nodo per inserire i nuovi nodi creati
        tempN.create(temp, node, node.depth, problem.path_cost(node,action), action) # assegna specifici valori alle variabili del nodo
        tempFL.append(tempN) # aggiunge il nodo alla lista dei nodi da inserire nella FL
        flag = 1 # è avvenuta una effettiva espansione quindi aggiungo il nodo alla lista closed
    if flag:
        problem.state_space.append(node.state)

    return tempFL


def Tree_Search(problem, l):            # l is the depth limit for the Depth Limited Search Algorithm
    Fringe = FL.Fringe_list(l)
    root = Node()           # dichiarazione root_node
    root.root(problem.initial_state)            # inizializzazione root node
    if problem.goal_test(root.state):
        return root
    Fringe.add(root)            # update fl w/ root_node

    while 1:
        if len(Fringe.list) == 0:
            return 1            #il Tree Search è terminato e non è andato a buon fine
        else:
            selected_node = Fringe.pop()            # seleziona il prossimo nodo della fringe list
            print('DEPTH ', selected_node.depth)

            # se nodo non soddisfa il goal test
            new_fringe_nodes = Expand(problem, selected_node)           # effettua l'expand del nodo selezionato

            # Check sui nodi appena espansi o(b^d) più performante in caso di costo uniforme
            for node in new_fringe_nodes:
                if problem.goal_test(node.state):
                   return node          # il Tree Search è terminato ed è andato a buon fine, viene restituito il nodo soluzione
                Fringe.add(node)            # aggiunge, uno alla volta, tutti i nodi restituiti dall'expand dell'ultimo nodo


def Iterative_Tree_Search(problem):

    l = 0
    solution = 1            # valore di default per 'soluzione non trovata'

    while 1:
        if solution == 1:
            l += 1
            solution = Tree_Search(problem, l)
        else:
            return solution

def Print_Path(node, time_start):
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
                '\nTree Depth ='  , node.depth)

            for index, x in enumerate(list):
                if index != 0:
                    print('\t↓\n', x.action,'\n\t↓')
                PS.print_matrix(x.state.matrix,3,3)
            return 0
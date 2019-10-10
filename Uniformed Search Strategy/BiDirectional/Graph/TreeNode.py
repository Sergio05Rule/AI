import Problem_State as PS
import timeit
import BF_Fringe as BF
import DF_Fringe as DF
import UC_Fringe as UC
import sys
import Problem as P
#Library for Node Class

class Node:
    def __init__(self):
        self.state = None
        self.parent = None      # il nodo parent è fondamentale per poter ricostruire il path fino al root
        self.depth = None       # indica la profondità del nodo
        self.path_cost = None   # è il path cost dal root al nodo attuale
        self.action = None      # indica l'azione che è fatto evolvere l'enviroment nello stato contenuto in questo nodo. Serve a poter ripercorrere le azioni che portano dal root al nodo attuale.

    def root(self, problem): # assegna ai parametri lo stato root_state e dei valori fissati per un nodo root
        self.state = problem.initial_state
        self.depth = 0
        self.path_cost = 0

    def create(self, problem, state, parent, depth, path_cost, action): # assegna i valori passati gli attributi di un nodo
        self.state = state
        self.parent = parent
        self.depth = depth + 1
        self.path_cost = path_cost
        self.action = action



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


def Tree_Search(problem):   # ritorna : 0 se può continuare la ricerca, 1 se non c'è soluzione, il nodo soluzione se l'ha trovato

    Fringe = problem.fringe

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
        print('EXPANDING: ', selected_node.state.id)

        # ---------------- NUOVI NODI NELLA FRINGE ----------------
        for node in new_fringe_nodes:
            Fringe.add(node)            # aggiunge, uno alla volta, tutti i nodi restituiti dall'expand dell'ultimo nodo

        return 0


def Print_Path(node, time_start, problem1, problem2):
    list = []           # lista dove memorizzare il nome dei nodi da stampare a video
    temp = node         # node contiene informazioni utili sulla depth e path cost del GOAL node
    flag = 0            # flag per il controllo del ciclo: vale 1 se trovo il nodo root
    print('')

    # Check if the solution is Failed
    if node == 1:
        print("Failed to find a valid solution!")
        return 0

    elif node[1] == 1:
        print('solution found for the first tree')

    elif node[1] == 2:
        print('solution found for the second tree')
    else:
        print('solution found in the intersection of the trees: ', node[1].state.id)




def compare_fringes(fringe1, fringe2):  # nel metodo bidirezionale confronta le fringe in cerca di elemento comune, altrimenti ritorna 0
    list1 = fringe1.list
    list2 = fringe2.list

    for node1 in list1:
        for node2 in list2:
            if node1.state.id == node2.state.id:
                return (node1,node2)
    return 0

def BiDirectional_Search(graph, prob1, prob2, fringe_type1, fringe_type2):

    # ----- DICHIARO E ASSEGNO I DUE PROBLEMI SIMMETRICI -----
    problem1 = prob1
    problem2 = prob2

    #----- SETTO IL TIPO DI ALGORITMO DI RICERCA DAL NODO START -----
    if fringe_type1 == 'BF':
        problem1.fringe = BF.Fringe_list()
    elif fringe_type1 == 'DF':
        problem1.fringe = DF.Fringe_list()
    elif fringe_type1 =='UC':
        problem1.fringe = UC.Fringe_list()
    else:
        print('Incorrect fringe_1 type')                # TIPO DI ALGORITMO NON PRESENTE
        sys.exit()

    # ----- SETTO IL TIPO DI ALGORITMO DI RICERCA DAL NODO END -----
    if fringe_type2 == 'BF':
        problem2.fringe = BF.Fringe_list()
    elif fringe_type2 == 'DF':
        problem2.fringe = DF.Fringe_list()
    elif fringe_type2 =='UC':
        problem2.fringe = UC.Fringe_list()
    else:
        print('Incorrect fringe_2 type')                  # TIPO DI ALGORITMO NON PRESENTE
        sys.exit()


    # ----- DICHIARO E ASSEGNO I DUE NODI DI PARTENZA DEI DUE ALBERI -----
    root1 = Node()
    root2 = Node()

    problem1.created_nodes += 1
    problem2.created_nodes += 1

    root1.root(problem1)
    root2.root(problem2)

    # ----- AGGIUNGO I ROOT NODES ALLA FRINGE -----
    problem1.fringe.add(root1)
    problem2.fringe.add(root2)


    solution1 = Tree_Search(problem1)
    solution2 = Tree_Search(problem2)

    solution = compare_fringes(problem1.fringe, problem2.fringe)

    if solution != 0:           # soluzione intermedia trovata
        return solution

    while 1:

        if solution1 == 0:
            solution1 = Tree_Search(problem1)
        elif solution1 == 1:
            return 1
        else:
            return (solution1, 1)           # tupla che contiene il nodo soluzione e un flag identificativo dell'albero che ha trovato la soluzione

        solution = compare_fringes(problem1.fringe, problem2.fringe)

        if solution != 0:
            return solution

        if solution2 == 0:
            solution2 = Tree_Search(problem2)
        elif solution2 == 1:
            return 1
        else:
            return (solution2, 2)           # tupla che contiene il nodo soluzione e un flag identificativo dell'albero che ha trovato la soluzione

        solution = compare_fringes(problem1.fringe, problem2.fringe)

        if solution != 0:  # soluzione intermedia trovata
            return solution

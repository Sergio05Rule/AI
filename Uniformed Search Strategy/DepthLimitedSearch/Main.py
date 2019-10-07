import TreeNode as TN
import Problem as P
import Problem_State as PS


def Print_Path(node):
    list = []   # lista dove memorizzare il nome dei nodi da stampare a video
    temp = node # (node contiene informazioni utili sulla depth e path cost del GOAL node)
    flag = 0    # flag per il controllo del ciclo: vale 1 se trovo il nodo root
    print('')

    # Check if the solution is Failed
    if node == 1:
        print("Failed to find a valid solution!")
        return 0

    while 1:
        list.insert(0,temp)  # salvo in una lista i nodi del percorso: li inserisco all'indice 0 in modo da ottenere un ordine dal nodo iniziale a quello finale
        if temp.parent == None: # sono arrivato al nodo root
            flag = 1
        else:
            temp = temp.parent # passo al nodo padre per la prossima iterazione
        if flag :
            print('--- Path Finder ---')
            print('I found a valid solution! \nPath Cost =', node.path_cost,'\nTree Depth =', node.depth)
            #output = ''
            print('')
            for index, x in enumerate(list):
                if index != 0:
                    print('\t↓\n', x.action,'\n\t↓')
                PS.print_matrix(x.state.matrix,3,3)
            return 0

if __name__ == '__main__':

    # inizializzazione matrice
    r = [[5, 1, 2],
         [4, 6, 3],
         [0, 7, 8]]
    start = PS.State(r)
    depth_limit = 37
    problem = P.Problem(start)

    Print_Path(TN.Tree_Search(problem, depth_limit))  #run the search Alg








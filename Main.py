import TreeNode as TN
import Problem as P
import Problem_State as PS
import Matrix as M

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
            print('I found a valid soution! \nPath Cost =', node.path_cost,'\nTree Depth =', node.depth)
            #output = ''
            print('')
            for index, x in enumerate(list):
                if index != 0:
                    print('\t↓\n', x.action,'\n\t↓')
                print(x.state.pos)
                #PS.print_matrix(x.state.matrix,3,3)
            return 0

if __name__ == '__main__':

    # inizializzazione matrice
    aux = [[5, 0, 2, 0, 1],
        [1, 6, 2, 0, 1],
        [5, 0, 2, 0, 1],
        [5, 1, 2, 0, 1],
        [1, 0, 8, 1, 1]]

    lab = M.Matrix(aux)

    lab.print_matrix()

    problem = P.Problem(PS.State((4,0)), PS.State((0,4)), lab)

    #actions = problem.action(PS.State((2,2)))
    #print(actions)

    Print_Path(TN.Tree_Search(problem))  #run the search Alg

    #test commit git hub











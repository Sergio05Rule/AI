import Graph as G
import TreeNode as TN
import Problem as P
import Problem_State as PS
import UC_Fringe as FL


if __name__ == '__main__':

    g = G.Graph()                 #definizione grafo

    # inizializzazione grafo
    g.add_edge('a', 'b', 1)
    g.add_edge('a', 'c', 10)
    g.add_edge('a', 'e', 4)
    g.add_edge('b', 'c', 2)
    g.add_edge('c', 'd', 3)
    g.add_edge('c', 'e', 3)
    g.add_edge('d', 'e', 2)

    start = 'a'  # stato iniziale del grafo
    end = 'e'  # stato goal di arrivo

    PS.check_state(start,g)
    PS.check_state(end,g)


    problem = P.Problem(g, PS.State(start), PS.State(end))
    problem2 = P.Problem(g, PS.State(end), PS.State(start))

    fringe = FL.Fringe_list()
    fringe2 = FL.Fringe_list()

    # ---------------- NUOVO NODO CREATO ----------------
    root1 = TN.Node()    # dichiarazione root_node
    problem.created_nodes += 1
    root1.root(problem)      # inizializzazione root node

    # ---------------- AGGIUNTA ROOT ALLA FRINGE ----------------
    fringe.add(root1)    # update fl w/ root_node

    # ---------------- NUOVO NODO CREATO ----------------
    root2 = TN.Node()    # dichiarazione root_node
    problem.created_nodes += 1
    root2.root(problem2)      # inizializzazione root node

    # ---------------- AGGIUNTA ROOT ALLA FRINGE ----------------
    fringe2.add(root2)    # update fl w/ root_node

    flag = 0

    while 1:

        if flag == 1:

            if fringe[0] == 0:  # CONTINUE
                fringe = TN.Tree_Search(problem, fringe[1])
                solution = TN.compare_fringes(fringe[1], fringe2[1])
            elif fringe[0] == 1: # SOLUTION FOUND
                break
            elif fringe[0] == 2: # SOLUTION FOUND
                TN.Print_Path(fringe[1], 0, problem)
                break

            if solution != 0:
                TN.Print_Path(solution, 0, problem)
                break


            if fringe2[0] == 0:  # CONTINUE
                fringe2 = TN.Tree_Search(problem2, fringe2[1])
                solution = TN.compare_fringes(fringe2[1], fringe[1])
            elif fringe2[0] == 1: # SOLUTION FOUND
                break
            elif fringe2[0] == 2: # SOLUTION FOUND
                TN.Print_Path(fringe2[1], 0, problem2)
                break

            if solution != 0:
                TN.Print_Path(solution, 0, problem2)
                break

        if flag == 0:
            fringe = TN.Tree_Search(problem, fringe)
            fringe2 = TN.Tree_Search(problem2, fringe2)
            solution = TN.compare_fringes(fringe[1], fringe2[1])
            if solution != 0:
                TN.Print_Path(solution, 0, problem2)
                break
            flag =+ 1


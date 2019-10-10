import Graph as G
import TreeNode as TN
import Problem_State as PS
import timeit
import Problem as P


if __name__ == '__main__':

    g = G.Graph()                 #definizione grafo

    # inizializzazione grafo
    g.add_edge('a', 'c', 1)
    g.add_edge('b', 'c', 1)
    g.add_edge('c', 'g', 1)
    g.add_edge('h', 'b', 1)
    g.add_edge('h', 'f', 1)
    g.add_edge('h', 'e', 1)
    g.add_edge('i', 'c', 1)
    g.add_edge('a', 'b', 1)
    g.add_edge('i', 'g', 1)
    g.add_edge('f', 'a', 1)
    g.add_edge('b', 'd', 1)

    start = 'a'  # stato iniziale del grafo
    end = 'e'  # stato goal di arrivo

    PS.check_state(start,g)
    PS.check_state(end,g)

    start_time = timeit.default_timer()

    # ----- DICHIARO E ASSEGNO I DUE PROBLEMI SIMMETRICI -----
    problem1 = P.Problem(g, PS.State(start), PS.State(end))
    problem2 = P.Problem(g, PS.State(end), PS.State(start))

    solution = TN.BiDirectional_Search(g, problem1, problem2, 'BF', 'BF')

    TN.Print_Path(solution, start_time, problem1, problem2)

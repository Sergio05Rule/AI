import TreeNode as TN
import Problem as P
import Problem_State as PS
import time
import Graph as G

if __name__ == '__main__':

    g = G.Graph()  # definizione grafo

    # inizializzazione grafo
    g.add_edge('a', 'c', 1)
    g.add_edge('a', 'b', 1)
    g.add_edge('b', 'd', 1)
    g.add_edge('d', 'e', 1)
    g.add_edge('d', 'f', 1)
    g.add_edge('e', 'g', 1)
    g.add_edge('c', 'e', 1)

    start = 'a'  # stato iniziale del grafo
    end = 'g'  # stato goal di arrivo

    depth_limit = 3
    problem = P.Problem(g, PS.State(start), PS.State(end))

    TN.Print_Path(TN.Tree_Search(problem, depth_limit), time.process_time())  #run dell'algoritmo di searching





import TreeNode as TN
import Problem as P
import Problem_State as PS
import timeit
import Graph as G

if __name__ == '__main__':
    start_time = timeit.default_timer()

    g = G.Graph()  # definizione grafo

    # inizializzazione grafo
    g.add_edge('a', 'c', 1)
    g.add_edge('a', 'b', 1)
    g.add_edge('b', 'd', 1)
    g.add_edge('d', 'e', 1)
    g.add_edge('d', 'f', 1)
    g.add_edge('e', 'g', 1)
    g.add_edge('c', 'e', 10)

    start = 'a'  # stato iniziale del grafo
    end = 'g'  # stato goal di arrivo

    depth_limit = 3

    problem = P.Problem(g, PS.State(start), PS.State(end), 'BF')
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)

    problem = P.Problem(g, PS.State(start), PS.State(end), 'UC')
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)

    problem = P.Problem(g, PS.State(start), PS.State(end), 'DF')
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)

    problem = P.Problem(g, PS.State(start), PS.State(end), 'DLS', depth_limit)
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)

    print('\n\n')

    problem = P.Problem(g, PS.State(start), PS.State(end), 'IDS')
    solution = TN.Iterative_Tree_Search(problem)
    TN.Print_Path(solution, start_time, problem)

    problem = P.Problem(g, PS.State(start), PS.State(end), 'GR')
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)

    problem = P.Problem(g, PS.State(start), PS.State(end), 'AS')
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)


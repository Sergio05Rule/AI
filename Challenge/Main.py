import TreeNode as TN
import Problem as P
import Problem_State as PS
import timeit

if __name__ == '__main__':
    start_time = timeit.default_timer()

    N = 5 # LARGHEZZA
    M = 5 # ALTEZZA
    K = 3 # NUMERO WALL
    V = [] #LISTA di Wall
    V.append((1,1))
    V.append((2,1))
    V.append((3,3))
    I = (0,0)
    G = (4,4)

    problem = P.Problem(N, M, K, V, PS.State(I), PS.State(G), 'BF')
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)

    problem = P.Problem(N, M, K, V, PS.State(I), PS.State(G), 'DF')
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)

    problem = P.Problem(N, M, K, V, PS.State(I), PS.State(G), 'AS')
    solution = TN.Graph_Search(problem)
    TN.Print_Path(solution, start_time, problem)


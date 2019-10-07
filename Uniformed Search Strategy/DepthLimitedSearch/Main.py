import TreeNode as TN
import Problem as P
import Problem_State as PS
import timeit

if __name__ == '__main__':

    start_time = timeit.default_timer()
    # inizializzazione matrice
    r = [[5, 1, 2],
         [4, 6, 3],
         [0, 7, 8]]
    start = PS.State(r)
    depth_limit = 9
    problem = P.Problem(start)

    TN.Print_Path(TN.Tree_Search(problem, depth_limit), start_time)  #run dell'algoritmo di searching





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
    problem = P.Problem(start)

    TN.Print_Path(TN.Iterative_Tree_Search(problem), start_time)  #run dell'algoritmo di searching







import TreeNode as TN
import Problem as P
import Problem_State as PS


if __name__ == '__main__':

    # inizializzazione matrice
    r = [[5, 1, 2],
         [4, 6, 3],
         [0, 7, 8]]
    start = PS.State(r)
    depth_limit = 10
    problem = P.Problem(start)

    TN.Print_Path(TN.Tree_Search(problem, depth_limit))  #run dell'algoritmo di searching







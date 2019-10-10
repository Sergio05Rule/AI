import TreeNode as TN
import Problem as P
import Problem_State as PS
import timeit

if __name__ == '__main__':

    start_time = timeit.default_timer()

    problem = P.Problem()

    TN.Print_Path(TN.Graph_Search(problem), start_time, problem)  #run dell'algoritmo di searching








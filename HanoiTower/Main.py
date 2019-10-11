import TreeNode as TN
import Problem as P
import Problem_State as PS
import timeit

if __name__ == '__main__':

    start_time = timeit.default_timer()

    problem = P.Problem('BF')
    TN.Print_Path(TN.Graph_Search(problem), start_time, problem)  #run dell'algoritmo di searching

    problem = P.Problem('UC')
    TN.Print_Path(TN.Graph_Search(problem), start_time, problem)  #run dell'algoritmo di searching

    #problem = P.Problem('DF')
    #TN.Print_Path(TN.Graph_Search(problem), start_time, problem)  # run dell'algoritmo di searching

    problem = P.Problem('AS')
    TN.Print_Path(TN.Graph_Search(problem), start_time, problem)  #run dell'algoritmo di searching

    problem = P.Problem('GR')
    TN.Print_Path(TN.Graph_Search(problem), start_time, problem)  #run dell'algoritmo di searching







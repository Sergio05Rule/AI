import Graph as G
import TreeNode as TN
import Problem as P
import Problem_State as PS


def check_state(state,g): # Check if an element is in the graph
    bool = 0
    for vertex in g.get_vertices():
        if state == vertex:
            bool = 1

    if bool == 0:
        print('\nABORT EXECUTION:',state,' is not a graph element!')
        sys.exit()



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
    end = 'd'  # stato goal di arrivo

    check_state(start,g)
    check_state(end,g)


    problem = P.Problem(g, PS.State(start), PS.State(end))
    solution = TN.Tree_Search(problem)  #run the search Alg

    print(solution.state.id,solution.parent.state.id, solution.parent.parent.state.id, solution.parent.parent.parent)


from CSP import Constraint, CSP
from typing import Dict, List, Optional
import ARC_3 as a

class Math_constraint(Constraint[str, str]):
    def __init__(self, p1: str, p2:str):
        super().__init__([p1,p2])
        self.p1: str = p1
        self.p2: str = p2

    def satisfied(self, assignment: Dict[str, str]):
        #print('TEST\n',self.p1)
        #print(assignment)
        #print(assignment[self.p2]) #Tavolo 1
        #Se uno dei due non è assegnato allora return True
        if self.p1 not in assignment or self.p2 not in assignment:
            return True

        return assignment[self.p1] == assignment[self.p2]

if __name__ == "__main__":
    var1 = 'x1'
    var2 = 'x2'
    variables: List[str] = [var1, var2]

    domains: Dict[str, List[str]] = {}

    domains['x1'] = [i for i in range (100,200)]
    domains['x2'] = [1,2,3,4,5,6,7,8,199,200,300,400]

    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint( Math_constraint("x1",'x2'))

    #ARC CONSISTENCY
    #a.arc_3(csp)

    csp.tree_csp_solver()
    '''
    # Print Soluzione
    solution: Dict[str, str] = csp.backtracking_search()
    if solution is None:
        print("Nessuna soluzione trovata")
    else:
        print('\nSoluzione:')
        for x in solution:
            print ('Variabile:', x,'- valore del dominio:', solution[x])

    '''

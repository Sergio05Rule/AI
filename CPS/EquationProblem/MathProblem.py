from CSP import Constraint, CSP
from typing import Dict, List, Optional

class Math_constraint(Constraint[str, str]):
    def __init__(self, p1: str):
        super().__init__([p1])
        self.p1: str = p1

    def satisfied(self, assignment: Dict[str, str]):
        #print('TEST\n',self.p1)
        #print(assignment)
        #print(assignment[self.p2]) #Tavolo 1
        #Se uno dei due non è assegnato allora return True
        if 'x1' not in assignment or 'x2' not in assignment or 'x3' not in assignment:
            return True

        x1_val = 0
        x2_val = 0
        x3_val = 0

        for x in assignment:
            if x == 'x1':
                x1_val = assignment[x]
            if x == 'x2':
                x2_val = assignment[x]
            if x == 'x3':
                x3_val = assignment[x]

        if x1_val > 150 and x3_val < x1_val + x2_val:
            return True
        else:
            return False

if __name__ == "__main__":
    var1 = 'x1'
    var2 = 'x2'
    var3 = 'x3'
    variables: List[str] = [var1, var2, var3]

    domains: Dict[str, List[str]] = {}

    domains['x1'] = [i for i in range (100,200)]
    domains['x2'] = [3,4,5]
    domains['x3'] = [0,1,2,3,4,5,6,7,8]

    #for x in variables:
        #print (domains[x])

    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint( Math_constraint("x1"))
    csp.add_constraint( Math_constraint("x2"))  #PERCHè SONO NECESSARIE TUTTE E 3 LE VARIABILI?
    csp.add_constraint( Math_constraint("x3"))

    # Print Soluzione
    solution: Dict[str, str] = csp.backtracking_search()
    if solution is None:
        print("Nessuna soluzione trovata")
    else:
        print('\nSoluzione:')
        for x in solution:
            print ('Variabile:', x,'- valore del dominio:', solution[x])



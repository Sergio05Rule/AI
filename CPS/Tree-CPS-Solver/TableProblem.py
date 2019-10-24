from CSP import Constraint, CSP
from typing import Dict, List, Optional
import ARC_3 as a
class Table_constraint(Constraint[str, str]):
    def __init__(self, p1: str, p2: str, cnd):
        super().__init__([p1, p2])
        self.p1: str = p1
        self.p2: str = p2
        self.cnd = cnd

    def satisfied(self, assignment: Dict[str, str]):
        if self.p1 not in assignment or self.p2 not in assignment:
            return True

        count_t1=0
        count_t2=0
        count_t3=0
        #check max sei persone per tavolo
        for x in assignment:
            print(assignment[x])
            if assignment[x] == 'Tavolo 1':
                count_t1 += 1
            elif assignment[x] == 'Tavolo 2':
                count_t2 += 1
            elif assignment[x] == 'Tavolo 3':
                count_t3 += 1

        if count_t1>5 or count_t2>5 or count_t3 >5:
            return False

        # check the table assigned to p1 is not the same as the table assigned to p2
        if self.cnd == 0:
            return assignment[self.p1] != assignment[self.p2]
        if self.cnd == 1:
            return assignment[self.p1] == assignment[self.p2]

if __name__ == "__main__":
    variables: List[str] = ["Antonella", "Domenico", "Raffaella", "Tommaso","Vincenzo","Azzurra","Cristiano","Francesca","Luigi","Giovanni","Marcella","Daniela","Nunzio","Leonardo","Silvia"]

    domains: Dict[str, List[str]] = {}
    for variable in variables:
        domains[variable] = ["Tavolo 1", "Tavolo 2", "Tavolo 3"]

    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint( Table_constraint("Giovanni", "Marcella",0)) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint("Marcella", "Daniela",0)) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint("Luigi", "Leonardo",0)) #condition = 1 insieme, 0 altrimenti

    csp.add_constraint( Table_constraint("Antonella", "Domenico",1)) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint("Domenico", "Raffaella",1)) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint("Raffaella", "Tommaso",1)) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint("Tommaso", "Vincenzo",1)) #condition = 1 insieme, 0 altrimenti

    csp.add_constraint( Table_constraint("Azzurra", "Cristiano",1)) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint("Cristiano", "Francesca",1)) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint("Francesca", "Luigi",1)) #condition = 1 insieme, 0 altrimenti

    #ARC CONSISTENCY
    a.arc_3(csp)

    #csp.tree_csp_solver()

    solution: Dict[str, str] = csp.backtracking_search()
    if solution is None:
        print("Nessuna soluzione trovata")
    else:
        print('\nSoluzione:')
        print(solution)


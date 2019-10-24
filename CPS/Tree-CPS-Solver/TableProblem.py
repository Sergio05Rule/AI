from CSP import Constraint, CSP
from typing import Dict, List, Optional
import ARC_3 as a
class Table_constraint_together(Constraint[str, str]):
    def __init__(self, p1: str, p2: str):
        super().__init__([p1, p2])
        self.p1: str = p1
        self.p2: str = p2

    def satisfied(self, assignment: Dict[str, str], variable):
        if self.p1 not in assignment or self.p2 not in assignment:
            return True

        return assignment[self.p1][0] == assignment[self.p2][0]


class Table_constraint_split(Constraint[str, str]):
    def __init__(self, p1: str, p2: str):
        super().__init__([p1, p2])
        self.p1: str = p1
        self.p2: str = p2

    def satisfied(self, assignment: Dict[str, str], variable):
        if self.p1 not in assignment or self.p2 not in assignment:
            return True
        '''
        for x in assignment:
            for y in assignment:
                if x != y and assignment[x] == assignment[y]:
                    return False
        '''
        return assignment[self.p1][0] != assignment[self.p2][0]


class Table_constraint_alldiff(Constraint[str, str]):
    def __init__(self, p1: str):
        super().__init__([p1])
        self.p1: List[str] = p1

    def satisfied(self, assignment: Dict[str, str], variable):
        '''
        for var in variables:
            if var not in assignment:
                return True
        '''

        for x in assignment:
            if x != variable and assignment[x] == assignment[variable]:
                return False
        return True



if __name__ == "__main__":
    variables: List[str] = ["Antonella", "Domenico", "Raffaella", "Tommaso","Vincenzo","Azzurra","Cristiano","Francesca","Luigi","Giovanni","Marcella","Daniela","Nunzio","Silvia","Leonardo"]

    domains: Dict[str, List[str]] = {}
    for variable in variables:
        domains[variable] = [("Tavolo 1",1),("Tavolo 1",2),("Tavolo 1",3),("Tavolo 1",4),("Tavolo 1",5),("Tavolo 1",6),
                             ("Tavolo 2",1),("Tavolo 2",2),("Tavolo 2",3),("Tavolo 2",4),("Tavolo 2",5),("Tavolo 2",6),
                             ("Tavolo 3",1),("Tavolo 3",2),("Tavolo 3",3),("Tavolo 3",4),("Tavolo 3",5),("Tavolo 3",6)]

    csp: CSP[str, str] = CSP(variables, domains)
    #non insieme
    csp.add_constraint( Table_constraint_split("Giovanni", "Marcella")) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint_split("Marcella", "Daniela")) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint_split("Luigi", "Leonardo")) #condition = 1 insieme, 0 altrimenti

    #insieme
    csp.add_constraint( Table_constraint_together("Antonella", "Domenico")) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint_together("Domenico", "Raffaella")) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint_together("Raffaella", "Tommaso")) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint_together("Tommaso", "Vincenzo")) #condition = 1 insieme, 0 altrimenti

    csp.add_constraint( Table_constraint_together("Azzurra", "Cristiano")) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint_together("Cristiano", "Francesca")) #condition = 1 insieme, 0 altrimenti
    csp.add_constraint( Table_constraint_together("Francesca", "Luigi")) #condition = 1 insieme, 0 altrimenti

    #Constraint valido per tutti: tutti in posti diversi dei tavoli
    for person in variables:
        csp.add_constraint( Table_constraint_alldiff(person)) #condition = 1 insieme, 0 altrimenti


    #csp.tree_csp_solver()

    solution: Dict[str, str] = csp.backtracking_search()
    if solution is None:
        print("Nessuna soluzione trovata")
    else:
        print('\nSoluzione:')
        print(solution)

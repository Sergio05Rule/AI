import typing as t

V = t.TypeVar(str) #simulo variabile striga per le Xi
D = t.TypeVar(str) #simulo variabile stringa per gli elementi del dominio

class Constraint( t.Generic[V, D] ):
    def __init__(self, variables: t.List[V]):
        self.variables = variables

    #@abstractmethod
    def satisfied(self, assignment: t.Dict[V, D]):
        ...

class CSP( t.Generic[V, D] ):
    def __init__(self, variables: t.List[V], domains: t.Dict[V, t.List[D]]):
        self.variables: t.List[V] = variables  # variabili che devono essere vincolate
        self.domains: t.Dict[V, t.List[D]] = domains  # dominii delle variabili
        self.constraints: t.Dict[V, t.List[Constraint[V, D]]] = {} #vincoli sulle variabili
        for variable in self.variables:
            self.constraints[variable] = []

    def add_constraint(self, constraint: Constraint[V, D]):
        for variable in constraint.variables:
            if variable in self.variables:
                self.constraints[variable].append(constraint)

    # Check if the value assignment is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, variable: V, assignment: t.Dict[V, D]):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: t.Dict[V, D] = {}):
        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment

        x = []
        for v in self.variables:
            if v not in assignment:
                x.append(v)

        unassigned: t.List[V] = x

        #if __debug__ :
                #print ('DEBUG - Assignament var :',x)

        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            #se i vincoli sono consistenti proseguo nel backtracking ricorsivo
            if self.consistent(first, local_assignment):
                result: t.Dict[V, D] = self.backtracking_search(local_assignment)

                if result is not None: #se result = None termino backtracking_search
                    return result
        return None
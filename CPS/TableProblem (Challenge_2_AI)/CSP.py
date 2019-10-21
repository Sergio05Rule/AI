import typing as t
from abc import *

V = t.TypeVar(str) #simulo variabile striga per le Xi
D = t.TypeVar(str) #simulo variabile stringa per gli elementi del dominio

class Constraint( t.Generic[V, D] ):
    def __init__(self, variables: t.List[V]):
        self.variables = variables

    #@abstractmethod
    def satisfied(self, assignment: t.Dict[V, D]):
        print('ALBY')
        ...

class CSP( t.Generic[V, D] ):
    def __init__(self, variables: t.List[V], domains: t.Dict[V, t.List[D]]):
        self.variables: t.List[V] = variables  # variabili che devono essere vincolate
        self.domains: t.Dict[V, t.List[D]] = domains  # dominii
        self.constraints: t.Dict[V, t.List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []

    def add_constraint(self, constraint: Constraint[V, D]):
        for variable in constraint.variables:
            if variable in self.variables:
                self.constraints[variable].append(constraint)

    # Check if the value assignment is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, variable: V, assignment: t.Dict[V, D]):

        #print('siamo in consistent')
        '''
        print(variable)

        for x in variable:
            print(assignment[variable])
        '''


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
            # if we're still consistent, we recurse (continue)
            if self.consistent(first, local_assignment):
                result: t.Dict[V, D] = self.backtracking_search(local_assignment)

                # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
        return None
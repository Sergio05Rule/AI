import typing as t

V = t.TypeVar(str) #simulo variabile striga per le Xi
D = t.TypeVar(str) #simulo variabile stringa per gli elementi del dominio

class Constraint( t.Generic[V, D] ):
    def __init__(self, variables: t.List[V]):
        self.variables = variables

    #@abstractmethod
    def satisfied(self, assignment: t.Dict[V, D]):
        ...

# Eurisiche
def minimum_remaining_values(unassigned_vars, domains): #next Xi
    if __debug__:
        print('DEBUG - minimum_remaining_values')

    number_of_var = []
    for var in unassigned_vars:
        count = 0
        for value in domains[var]:
            count += 1
        if __debug__:
            print('\t',var, ' ha il seguente numero di valori del dominio:', count,'\n\tvalues: ', domains[var])
        number_of_var.append(count)

    if __debug__:
        print('\tLa prossima variabile da selezionare secondo questa euristica è: ',unassigned_vars[number_of_var.index(min(number_of_var))])

    return unassigned_vars[number_of_var.index(min(number_of_var))]

def degree_heuristic(unassigned_vars, constraints): #next Xi
    if __debug__:
        print('DEBUG - degree_heuristic')

    number_of_constraint = []
    for var in unassigned_vars:
        count = 0

        if __debug__:
            print('\t', var, ' ha i seguenti vincoli:')

        for constraint in constraints[var]:
            count += 1
            if __debug__:
                print('\t',constraint.variables)
        number_of_constraint.append(count)

        if __debug__:
            print('\t numero di vincoli per ',var,':' ,count,'\n')

    if __debug__:
        print('\tnumero max di vincoli', max(number_of_constraint))
        print('\tindex',number_of_constraint.index(max(number_of_constraint)))
        print('\t', unassigned_vars[number_of_constraint.index(max(number_of_constraint))] )

    return unassigned_vars[number_of_constraint.index(max(number_of_constraint))]

def last_costraining_value(var, constraints, domains, assignment): #selezione del prossimo elemento del dominio per la data Xi
    #Need 2 be COMPLETE #TODO
    if __debug__:
        print('DEBUG - last_costraining_value')
    print('\t',var)

    for constraint in constraints[var]:
        print('\t',constraint.variables)
    print('\tdomains ',domains)
    print('\tassignment ',assignment)

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

    #controlla se l'assignment soddisfa tutti i constraint per la data variabile
    def consistent(self, variable: V, assignment: t.Dict[V, D]):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: t.Dict[V, D] = {}):
        # Se vero tutte le variabili sono state assegnate a valori del Dominio
        if len(assignment) == len(self.variables):
            return assignment

        x = []
        for v in self.variables:
            if v not in assignment:
                x.append(v)

        unassigned: t.List[V] = x

        if __debug__ :
                print ('DEBUG - unassigned var :',x)

        # recupero la prossima variabile da valorizzare secondo una opportuna euristica

        '''Cambio Euristica'''
        #next_var: V = unassigned[0] #euristica fifo
        #next_var: V = minimum_remaining_values(unassigned, self.domains) #euristica minimum_remaining_values
        next_var: V = degree_heuristic(unassigned, self.constraints) #euristica degree_heuristic

        for value in self.domains[next_var]:
            local_assignment = assignment.copy()
            local_assignment[next_var] = value #prendo il primo valore disponibile

            if __debug__:
                print('DEBUG - assigament', assignment, 'assignment[next_var] ', local_assignment[next_var])
                print('DEBUG - next var: ',next_var, ' local assignment:', local_assignment)
            #se i vincoli sono consistenti proseguo nel backtracking ricorsivo
            if self.consistent(next_var, local_assignment):
                result: t.Dict[V, D] = self.backtracking_search(local_assignment)

                if result is not None: #se result = None termino backtracking_search
                    return result
        return None
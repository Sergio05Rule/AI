import typing as t
import ARC_3 as a
import operator #per riordinare dizionario

V = t.TypeVar(str) #simulo variabile striga per le Xi
D = t.TypeVar(str) #simulo variabile stringa per gli elementi del dominio

class Constraint( t.Generic[V, D] ):
    def __init__(self, variables: t.List[V]):
        self.variables = variables

    #abstractmethod
    def satisfied(self, assignment: t.Dict[V, D]):
        ...

# Eurisiche
def minimum_remaining_values(unassigned_vars, domains): #next Xi

    number_of_var = []
    for var in unassigned_vars:
        count = 0
        for value in domains[var]:
            count += 1
        number_of_var.append(count)

    return unassigned_vars[number_of_var.index(min(number_of_var))]

def degree_heuristic(unassigned_vars, constraints): #next Xi

    number_of_constraints = []
    for var in unassigned_vars:
        count = 0

        for constraint in constraints[var]:
            for variable in constraint.variables:
                if variable in unassigned_vars and variable != var: #conto i constraint sulle var non assegnate
                    count += 1
        number_of_constraints.append(count)

    return unassigned_vars[number_of_constraints.index(max(number_of_constraints))]

def last_costraining_value(var, domains,constraints, unassigned): #selezione del prossimo elemento del dominio per la data Xi

    domain_count: t.Dict[D, D] = {}
    assignment: t.Dict[V, D] = {}

    for value in domains[var]: #Per ogni valore della next_var
        count = 0
        for constraint in constraints[var]:
            for neighbour in constraint.variables:
                if neighbour != var: #and neighbour in unassigned:
                    for n_value in domains[neighbour]:
                        assignment: t.Dict[V, D] = {}
                        assignment[var] = value
                        assignment[neighbour] = n_value
                        #verifica vincoli
                        for constraint in constraints[var]:
                            if not constraint.satisfied(assignment, var):
                                count += 1
                        domain_count[value] = count
    if len(assignment) != 0:
        sorted_domain_count= sorted(domain_count.items(), key=operator.itemgetter(1))
        result = []
        for x in sorted_domain_count:
            result.append(x[0])
        return result

    return domains

def foward_checking(csp, assignment, next_var, unassigned, new_domains):

    if not csp.consistent(next_var,assignment):

        return False
    else:
        return True

    '''
    removed_values = {}
    for var in csp.variables:
        removed_values[var] = []
    new_assignment = assignment.copy()
    for constraint in csp.constraints[next_var]: #tutti i constraint della next var
        for neighbour in constraint.variables:  #tutti i vicini dei constraint
            to_remove = []
            to_remove.clear()
            if neighbour != next_var and neighbour in unassigned:
                for value in new_domains[neighbour]:
                    new_assignment[neighbour] = value
                    #verifica vincoli
                    if not constraint.satisfied(new_assignment, next_var):
                        to_remove.append(value)
                if len(to_remove)==len(csp.domains[neighbour]):
                    return False
                removed_values[neighbour] = to_remove
     #vincolo all diff

    for var in csp.variables:
        if var != next_var:

            if assignment[next_var] not in removed_values[var]:
                removed_values[var].append(assignment[next_var])


    for v in csp.variables:
        if len(new_domains[v])==0:
            return False
    return removed_values
    '''

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
            else:
                print('Attenzione: ' ,variable,' non definita!')

    #controlla se l'assignment soddisfa tutti i constraint per la data variabile
    def consistent(self, variable: V, assignment: t.Dict[V, D]):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment,variable):
                return False
        return True

    def backtracking_search(self, assignment: t.Dict[V, D] = {}, local_domains = None):

        if local_domains == None:
            local_domains = self.domains.copy()

        # Se vero tutte le variabili sono state assegnate a valori del Dominio
        if len(assignment) == len(self.variables):
            return assignment

        x = []
        for v in self.variables:
            if v not in assignment:
                x.append(v)

        unassigned: t.List[V] = x

        # recupero la prossima variabile da valorizzare secondo una opportuna euristica

        '''Cambio Euristica'''
        next_var: V = unassigned[0] #euristica fifo
        #next_var: V = minimum_remaining_values(unassigned, self.domains) #euristica minimum_remaining_values
        #next_var: V = degree_heuristic(unassigned, self.constraints) #euristica degree_heuristic

        #self.domains[next_var] = last_costraining_value(next_var,self.domains, self.constraints,unassigned)

        removed = {}

        for value in local_domains[next_var]:

            new_domains = local_domains.copy()

            '''
            if removed == False:
                removed = {}
            for var in removed:
                for removed_value in removed[var]:
                    local_domains[var].append(removed_value)
            '''
            local_assignment = assignment.copy()
            local_assignment[next_var] = value #prendo il primo valore disponibile

            #se i vincoli sono consistenti proseguo nel backtracking ricorsivo
            #if self.consistent(next_var, local_assignment):

            if foward_checking(self, local_assignment, next_var, unassigned, local_domains):

                result: t.Dict[V, D] = self.backtracking_search(local_assignment, local_domains)

                if result is not None:  # se result = None termino backtracking_search
                    return result


            #removed = foward_checking(self, local_assignment, next_var, unassigned, local_domains)
            '''
            if removed != False:

                for var in removed:
                    for removed_value in removed[var]:
                        if removed_value in local_domains[var]:
                            local_domains[var].remove(removed_value)

                result: t.Dict[V, D] = self.backtracking_search(local_assignment, local_domains)


                if result is not None: #se result = None termino backtracking_search
                    return result
            '''
        return None


    def tree_csp_solver(self, assignment: t.Dict[V, D] = {}):

        n = len(self.variables) #numero di variabili del csp
        root = self.variables[0] #prima variabile del problema come root node

        #ORDINE TOPOLOGICO DELLE VARIABILE -> SI ASSUME ORDINE in self.variables

        for j in range(n, 2-1, -1): #per j che va da n a 2

            returned = make_arc_consistent(self, self.variables[j-1], self.variables[j-2])

        for var in self.variables:
            try:
                print('solution: var',var,'value:',self.domains[var][0])
            except:
                print('il dominio di una variabile è nullo, nessuna soluzione possibile')
                return

        input('\npress any key to end the tree_csp_resolver')


def make_arc_consistent(csp,xi,xj):
        flag1 = a.revise(csp,xi,xj)
        flag2 = a.revise(csp,xj,xi)
        return True
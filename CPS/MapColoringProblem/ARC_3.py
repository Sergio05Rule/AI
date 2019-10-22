def arc_3(CSP):
    if __debug__:
        print('DEBUG - ARC_3 Consistency')

    queue = load_queue(CSP) #a queue of arcs, initially all the arcs in csp

    #test revise
    actual_arc = queue.pop()
    xi = actual_arc[0]
    xj = actual_arc[1]

    while len(queue) != 0:
        actual_arc = queue.pop()
        xi = actual_arc[0]
        xj = actual_arc[1]
        if revise(CSP, xi, xj ) == True:
            if len(CSP.domains[xi]) == 0:
                return False

            for var in CSP.variables:
                for constraint in CSP.constraints[var]:
                    if constraint.variables[1] == xi:
                        queue.append(constraint.variables)
                        aux = constraint.variables[1], constraint.variables[0] #direzione inversa
                        queue.append(aux)
    if __debug__:
        print('DEBUG - FINE ARC_3 Consistency')

    input('\npress any key to continue')
    return True


def load_queue(CSP):

    queue = []

    for var in CSP.variables:
        for constraint in CSP.constraints[var]:
            aux = constraint.variables[1],constraint.variables[0]
            queue.append(constraint.variables)
            queue.append(aux) #direzione inversa

    return queue

def revise(CSP, xi, xj): #returns true iff we revise the domain of Xi
    revised = False
    flag = True

    test = [] #lista temporanea usata per eliminare valori dal dominio (dic[var][domain])
    #print('xi & xj',xi , xj)
    for index, x in enumerate(CSP.domains[xi]):
        for y in CSP.domains[xj]:
            #print('vicnolo', x, y)
            if x == y: #vincolo soddisfatto
                flag = False

        if flag != False:
            print('\tDEBUG - cancellazione dalla var:', xi, 'il valore del dominio:', CSP.domains[xi][index])
            print('\tDEBUG -', CSP.domains[xi][index])
            revised = True
        else:
            test.append(CSP.domains[xi][index])

    CSP.domains[xi] = test

    return revised





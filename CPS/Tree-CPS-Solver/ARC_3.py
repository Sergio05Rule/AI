def arc_3(CSP):
    if __debug__:
        print('DEBUG - ARC_3 Consistency')

    queue = load_queue(CSP) #a queue of arcs, initially all the arcs in csp

    print('Test queue')

    for element in queue:
        print(element)
    input('fine queue')
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
        for var in CSP.variables:
            print('Var:', var, 'Domain:',CSP.domains[var
            ])

    input('\npress any key to continue')
    return True


def load_queue(CSP):

    queue = []
    for var in CSP.variables:
        print('next')
        for constraint in CSP.constraints[var]:
            #aux = constraint.variables[1],constraint.variables[0]
            if constraint.variables not in queue:
                queue.append(constraint.variables)
                print('constraint.variables',constraint.variables)

                aux = constraint.variables[1],constraint.variables[0]
                queue.append(aux) #direzione inversa
    '''
    queue = []
    for var in CSP.variables:
        print('next')
        for constraint in CSP.constraints[var]:
            #aux = constraint.variables[1],constraint.variables[0]
                queue.append(constraint.variables)
                print('constraint.variables',constraint.variables)
            #queue.append(aux) #direzione inversa
    '''
    return queue

def revise(CSP, xi, xj): #returns true iff we revise the domain of Xi
    revised = False
    flag = True

    test = [] #lista temporanea usata per eliminare valori dal dominio (dic[var][domain])
    #print('xi & xj',xi , xj)
    for index, x in enumerate(CSP.domains[xi]):
        print('per ogni x nel dominio:',x)
        flag = True
        for y in CSP.domains[xj]:
            print('vicnolo', x, y)
            if revise_condition( x,y ,xi,xj ): #vincolo soddisfatto
                print('vincolo vero, flag = false')
                flag = False

        if flag != False:
            print('\tDEBUG - cancellazione dalla var:', xi, 'il valore del dominio:', CSP.domains[xi][index])
            print('\tDEBUG -', CSP.domains[xi][index])
            revised = True
        else:
            test.append(CSP.domains[xi][index])

    CSP.domains[xi] = test

    return revised

def revise_condition(a,b , xi,xj):
    if xi=='x1':
        if a > b:
            return True
        else:
            return False
    if xi=='x2':
        if a < b:
            return True
        else:
            return False
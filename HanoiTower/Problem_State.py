class State:
    def __init__(self, tower):
        self.tower = tower
        self.bricks = find_bricks(tower)



def find_bricks(tower):

    bricks = []

    for row in range(len(tower)):

        for col in range(len(tower[0])):

            if tower[row][col] == 1:
                bricks.insert(0,(row,col))
            elif tower[row][col] == 2:
                bricks.insert(1,(row,col))
            elif tower[row][col] == 3:
                bricks.insert(2,(row,col))

    return bricks


def bricks_on_top(tower):

    tops = []

    for col in range(len(tower[0])):

        brick = (0, (None,None))

        for row in range(len(tower)):

            if tower[2-row][col] > 0:
                brick = (tower[2-row][col], (2-row,col))

        tops.insert(col, brick)

    return tops


def print_matrix(matrix, rows, cols):
    [print(matrix[x]) for x in range(rows)]

def compare_matrix(a,b):

    for row in range(3):
        for col in range(3):
            if not (a[row][col] == b[row][col]):
                return 0
    return 1


def compare_states(state1, state2):

    return compare_matrix(state1.tower, state2.tower)


def NotinClosed(problem, node): #restituisce 1 se lo stato non è stato già visitato (al netto di controlli sulla depth) è quindi bisogna aggiungerlo

    NotVisited = 1
    for state in problem.closed:
        if compare_states(state, node.state):
            NotVisited = 0 #presente nei visited ma selected_node ha maggiore/uguale depth

    return NotVisited


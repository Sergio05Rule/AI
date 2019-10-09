

class State:
    def __init__(self, matrix):
        self.holeR = None
        self.holeC = None
        self.matrix = init_matrix(3,3)
        self.matrix = copy_matrix(matrix,3,3)
        if(not self.check_coerency()):
            print("Error: matrix in not well defined")

    def check_coerency(self):
        list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        for row in range(3):
            for col in range(3):
                for index, element in enumerate(list):
                    if self.matrix[row][col] == element:
                        if element == 0:
                            self.holeR = row
                            self.holeC = col
                        list.pop(index)

        if len(list) == 0:
            return 1
        else:
            return 0


def init_matrix(rows, cols):
    matrix = [[0 for x in range(cols)] for y in range(rows)]
    return matrix

def copy_matrix(inputM, rows, cols):

    outputM = init_matrix(rows, cols)
    for row in range(rows):
        for col in range(cols):
            outputM[row][col] = inputM[row][col]
    return outputM


def print_matrix(matrix, rows, cols):
    [print(matrix[x]) for x in range(rows)]


def compare_matrix(a,b):#restituisce 0 se le matrici sono diverse, 1 altrimenti

    for row in range(3):
        for col in range(3):
            if not (a[row][col] == b[row][col]):
                return 0
    return 1

def NotinClosed(problem, node): #restituisce 1 se lo stato non è stato già visitato (al netto di controlli sulla depth) è quindi bisogna aggiungerlo
    NotVisited = 1
    for tuple in problem.closed:
        if (compare_matrix(node.state.matrix , tuple[0].matrix) == 1 and node.depth >= tuple[1]):
            NotVisited = 0 #presente nei visited ma selected_node ha maggiore/uguale depth
    return NotVisited





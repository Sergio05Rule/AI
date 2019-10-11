import sys

class Matrix:
    def __init__(self, matrix):
        #self.holeR = None
        #self.holeC = None
        self.matrix = None
        self.init_matrix(len(matrix), len(matrix[0]))  # assumiamo una matrice rettangolare
        self.copy_matrix(matrix)

    def init_matrix(self, rows, cols):
        self.matrix = [[0 for x in range(cols)] for y in range(rows)]

    def copy_matrix(self, inputM):
        # outputM = self.init_matrix(len(inputM), len(inputM[0]))
        for row in range(len(inputM)):
            for col in range(len(inputM[0])):
                self.matrix[row][col] = inputM[row][col]

    def print_matrix(self):  # again supponiamo matrice rettangolare
        [print(self.matrix[x]) for x in range(len(self.matrix))]

    def compare_matrix(self, b):
        if len(self.matrix) != len(b) or len(self.matrix[0]) != len(b[0]):
            print("ERROR - In compare_matrix")
            sys.exit()
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                if not (self.matrix[row][col] == b[row][col]):
                    return 0
        return 1

    def check_top(self, x, y):
        if x==0:
            return 0
        else:
            try:
                if(self.matrix[x-1][y] != 0):
                    return 1
                else:
                    return 0
            except:
                return 0

    def check_down(self, x, y):
        if x==len(self.matrix)-1:
            return 0
        else:
            try:
                if(self.matrix[x+1][y] != 0):
                    return 1
                else:
                    return 0
            except:
                return 0

    def check_left(self, x, y):
        if y==0:
            return 0
        else:
            try:
                if(self.matrix[x][y-1] != 0):
                    return 1
                else:
                    return 0
            except:
                return 0

    def check_right(self, x, y):
        if y==len(self.matrix[0])-1:
            return 0
        else:
            try:
                if(self.matrix[x][y+1] != 0):
                    return 1
                else:
                    return 0
            except:
                return 0
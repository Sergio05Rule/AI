from random import randint


class State:

    def __init__(self, chess = None):

        if chess == None:
            self.chess = [0,0,0,0,0,0,0,0]
            self.random()
        else:
            self.chess = chess

    def random(self):

        for index in enumerate(self.chess):
            self.chess[index[0]] = randint(1,8)

    def how_many_on_rows(self, chess):

        cost = 0
        for col, queen1 in enumerate(chess[:7:]):
            for queen2 in chess[col+1::]:
                if queen1 == queen2:
                    cost += 1
        return cost

    def how_many_on_diagonal(self, chess):

        cost = 0
        for col, queen in enumerate(chess[:7:]):
            check_row = queen
            movement = min(8 - col, queen - 1) #il primo termine è il numero massimo di spostamenti verso destra, il secondo è il massimo di spostamenti verso l'alto
            for _, queen2 in enumerate(chess[col+1:col+1+movement:]):
                check_row -= 1
                if queen2 == check_row:
                    cost +=1

        for col, queen in enumerate(chess[:7:]):
            check_row = queen
            movement = min(8 - col, 8 - queen) #il primo termine è il numero massimo di spostamenti verso destra, il secondo è il massimo di spostamenti verso il basso
            for _, queen2 in enumerate(chess[col+1:col+1+movement:]):
                check_row += 1
                if queen2 == check_row:
                    cost +=1
        return cost

    def fitness_function(self, chess = None):
        if chess == None:
            chess = self.chess
        return 28 - self.how_many_on_diagonal(chess) - self.how_many_on_rows(chess)

    def change_position(self, col, new_pos):

        newchess = self.chess.copy()
        newchess[col] = new_pos
        new_state = State()
        new_state.chess = newchess
        return new_state


    def print(self):

        print('---- CHESS ----')
        for index, queen in enumerate(self.chess):
            print('In column ', index, 'queen in position: ', queen)

    def print_chess(self):

        print('  ', end='')
        for col in range(1,9):
            print(col, end=' ')
        print('')

        for row in range(1,9):
            print(row, end=' ')
            for col in range(8):
                if self.chess[col] == row:
                    print('Q', end=' ')
                else:
                    print('x', end=' ')
            print('')

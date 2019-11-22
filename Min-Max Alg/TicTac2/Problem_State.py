from copy import deepcopy

class State:
    def __init__(self, player , board = None):

        if board != None:
            self.board = board
        else:
            self.initialize_state()

        self.player_turn = player
        self.min = 'X'
        self.max = 'O'
        self.empty = '.'
        self.worst_max_case = -1
        self.worst_min_case = 1

    def initialize_state(self):
        self.board =   [['.','.','.'],
                        ['.','.','.'],
                        ['.','.','.']]

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == 'MIN':
                    print('{}|'.format(self.min), end=" ")
                elif self.board[i][j] == 'MAX':
                    print('{}|'.format(self.max), end=" ")
                elif self.board[i][j] == '.':
                    print('{}|'.format(self.empty), end=" ")
            print()
        print()

    def action(self):
        action_list = list()

        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '.' :
                    action_list.append( (i,j) )

        return (action_list)

    def result(self, action):

        px = action[0]
        py = action[1]

        if self.board[px][py] != '.':
            print('Azione non consentita. Casella (',px, py ,') occupata.')
            return self
        else:
            new_board = deepcopy(self.board)
            new_board[px][py] = self.player_turn
        return State(self.next_player(), new_board)

    def terminal_state(self):

        # Vertical win
        for i in range(0, 3):
            if (self.board[0][i] != '.' and
                    self.board[0][i] == self.board[1][i] and
                    self.board[1][i] == self.board[2][i]):
                return self.board[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.board[i] == ['MIN', 'MIN', 'MIN']):
                return 'MIN'
            elif (self.board[i] == ['MAX', 'MAX', 'MAX']):
                return 'MAX'

        # Main diagonal win
        if (self.board[0][0] != '.' and
                self.board[0][0] == self.board[1][1] and
                self.board[0][0] == self.board[2][2]):
            return self.board[0][0]

        # Second diagonal win
        if (self.board[0][2] != '.' and
                self.board[0][2] == self.board[1][1] and
                self.board[0][2] == self.board[2][0]):
            return self.board[0][2]

        # Is whole self.board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (self.board[i][j] == '.'):
                    return None

        return 'TIE'

    def next_player(self):

        if self.player_turn == 'MIN':
            return 'MAX'
        elif self.player_turn == 'MAX':
            return 'MIN'

    def heuristic(self):

        test = self.terminal_state()
        if test is None:
            return 0
        elif test is 'MAX':
            return 1
        elif test is 'MIN':
            return -1


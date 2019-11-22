from copy import deepcopy


class State:

    def __init__(self, player='MAX', input_board=None):

        if input_board is not None:
            self.board = input_board
        else:
            self.initialize_state()
        self.player_turn = player
        self.max_x = len(self.board)
        self.max_y = len(self.board[0])
        self.min = 'X'
        self.max = 'O'
        self.empty = '.'
        self.worst_max_case = -1000
        self.worst_min_case = 1000

    def initialize_state(self):

        self.board = \
            [['.', '.', '.', '.', '.', '.'],  # 0
             ['.', '.', '.', '.', '.', '.'],  # 1
             ['.', '.', '.', '.', '.', '.'],  # 2
             ['.', '.', '.', '.', '.', '.'],  # 3
             ['.', '.', '.', '.', '.', '.'],  # 4
             ['.', '.', '.', '.', '.', '.']]  # 5

    def draw_board(self):
        # print header
        print('\t', end='')
        for column in range(0, self.max_y):
            print(column, '\t\t', end='')
        print()

        for i in range(0, self.max_x):
            print(i, end='')
            for j in range(0, self.max_y):
                if self.board[i][j] == 'MIN':
                    print('\t{}\t|'.format(self.min), end=" ")
                elif self.board[i][j] == 'MAX':
                    print('\t{}\t|'.format(self.max), end=" ")
                elif self.board[i][j] == '.':
                    print('\t{}\t|'.format(self.empty), end=" ")
            print()
        print()

    def draw_board_reverse(self):
        # print header
        print('\t', end='')
        for column in range(0, self.max_y):
            print(column+1, '\t\t', end='')
        print()

        for i in range(self.max_x-1, -1, -1):
            print(i+1, end='')
            for j in range(self.max_y):
                if self.board[i][j] == 'MIN':
                    print('\t{}\t|'.format(self.min), end=" ")
                elif self.board[i][j] == 'MAX':
                    print('\t{}\t|'.format(self.max), end=" ")
                elif self.board[i][j] == '.':
                    print('\t{}\t|'.format(self.empty), end=" ")
            print()
        print()

    def action(self):

        # Le azioni possibili sono gli inserimenti nella colonna 0,1,2,3,4,5 se questa non è piena

        action_list = list()

        for j in range(0, self.max_y):
            if self.board[self.max_x-1][j] == '.':
                action_list.append(j)
        return action_list

    def result(self, action):
        new_board = deepcopy(self.board)

        # Azione non consentita
        if action not in self.action():
            print('Azione non consentita!')
            return State(self.player_turn, new_board)

        else:
            # trova la prima casella piena
            for i in range(len(self.board)):
                if new_board[i][action] == '.':
                    new_board[i][action] = self.player_turn
                    return State(self.next_player(), new_board)

        print('ATTENZIONE COMPORTAMENTO NON PREVISTO: nessuna azione fatta')
        return State(self.player_turn, new_board)

    def terminal_state(self):

        check = self.check_board()
        print('CONTOLLO ',check)

        if check[3] is True:
            return 'TIE'
        else:
            return check[2]

    def next_player(self):

        if self.player_turn == 'MAX':
            return 'MIN'
        elif self.player_turn == 'MIN':
            return 'MAX'

    def check_board(self):

        couples = 0
        triples = 0
        winner = None
        full = True

        #controlla ogni casella
        for j in range(self.max_y):
            for i in range(self.max_x):
                check_result = self.check_box(i, j)
                couples += check_result[0]
                triples += check_result[1]
                # se una casella è il punto di partenza di un riga, colonna o diagonale da 4 elementi, il vincitore viene salvato
                if check_result[2] > 0:
                    winner = self.board[i][j]
                # controllo che ci siano ancora caselle vuote
                if check_result[3] is False:
                    full = False

        return [couples, triples, winner, full]


    def check_box(self, x, y):
        box_value = self.board[x][y]
        couples = 0
        triples = 0
        quaternions = 0
        full = True

        max_jump_down = min(4, self.max_x - x)
        max_jump_up = min(4, x + 1)
        max_jump_right = min(4, self.max_y - y)

        if box_value == '.':
            full = False
        # vertical check
        for jump in range(max_jump_down):
            if box_value == self.board[x + jump][y]:
                if jump == 1 and box_value == 'MAX':
                    couples += 1
                elif jump == 2 and box_value == 'MAX':
                    triples += 1
                elif jump == 3:
                    if box_value == 'MAX':
                        quaternions += 1
            else:
                break

        # horizontal check
        for jump in range(max_jump_right):
            if box_value == self.board[x][y + jump]:
                if jump == 1:
                    couples += 1
                elif jump == 2:
                    triples += 1
                elif jump == 3:
                    quaternions += 1
            else:
                break

        # diagonal1 check
        for jump in range(min(max_jump_right, max_jump_down)):
            if box_value == self.board[x + jump][y + jump]:
                if jump == 1:
                    couples += 1
                elif jump == 2:
                    triples += 1
                elif jump == 3:
                    quaternions += 1
            else:
                break

        # diagonal2 check
        for jump in range(min(max_jump_right, max_jump_up)):
            if box_value == self.board[x - jump][y + jump]:
                if jump == 1:
                    couples += 1
                elif jump == 2:
                    triples += 1
                elif jump == 3:
                    quaternions += 1
            else:
                break


        return [couples, triples, quaternions, full]


    def heuristic(self):

        heuristic = self.check_board()[0] + self.check_board()[1]
        return heuristic

'''

board = \
    [['MIN', 'MAX', '.', '.', '.', '.'],  # 0
     ['MAX', '', '.', '.', '.', '.'],  # 1
     ['MIN', '.', '.', '.', '.', '.'],  # 2
     ['.', '.', '.', '.', '.', '.'],  # 3
     ['.', '.', '.', '.', '.', '.'],  # 4
     ['.', '.', '.', '.', '.', '.']]  # 5

a = State()
a.board = board
a.draw_board_reverse()
print(a.heuristic())

'''
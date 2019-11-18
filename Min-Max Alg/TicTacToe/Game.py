import Problem_State as PS
import time

# TicTacToe Game

class Game:
    def __init__(self, first_player_turn, min_max_depth = 0):
        self.initialize_game()
        self.player_turn = first_player_turn #variabile che tiene conto quale giocatore deve muovere
        self.cs = None
        self.min_max_depth = min_max_depth

    #inizializzo board di gioco
    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    # restitutisce, data il current_state tutte le mosse possibili (action_list)
    def action(self, state):
        action_list = list()

        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == '.' :
                    action_list.append( (i,j) )

        return action_list

    #controllando la board verifica se il gioco è finito vittorie/pareggi
    def terminal_state(self, state):

        # Vertical win
        for i in range(0, 3):
            if (state[0][i] != '.' and
                    state[0][i] == state[1][i] and
                    state[1][i] == state[2][i]):
                return state[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (state[i] == ['O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (state[0][0] != '.' and
                state[0][0] == state[1][1] and
                state[0][0] == state[2][2]):
            return state[0][0]

        # Second diagonal win
        if (state[0][2] != '.' and
                state[0][2] == state[1][1] and
                state[0][2] == state[2][0]):
            return state[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (state[i][j] == '.'):
                    return None

        # It's a tie!
        return '.'


    def max_value(self):
        # Possible values for max_v are:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        # We're initially setting it to -2 (-inf) as worse than the worst case:
        max_v = -2
        result = self.terminal_state(self.current_state)
        move = (0,0)
        move = list(move)

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == 'X':
            return (-1, move)
        elif result == 'O':
            return (1, move)
        elif result == '.':
            return (0, move)

        #result = None -> Game not end -> continue the game
        for action in self.action(self.current_state):
            self.current_state[action[0]][action[1]] = 'O'
            (new_max_v, move) = self.min_value()
            if new_max_v > max_v:
                max_v = new_max_v
                move[0] = action[0]
                move[1] = action[1]
            self.current_state[action[0]][action[1]] = '.'

        #print('siamo in max_value è ho selezionato', max_v, 'move', move)

        return (max_v,move)


    def min_value(self):
        # Possible values for max_v are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        min_v = +2
        result = self.terminal_state(self.current_state)
        move = (0,0)
        move = list(move)

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == 'X':
            return (-1, move)
        elif result == 'O':
            return (1, move)
        elif result == '.':
            return (0, move)


        #if result = None -> Game not end -> continue the game
        for action in self.action(self.current_state): #action with no attr
            self.current_state[action[0]][action[1]] = 'X'

            (new_min_v,move)  =  self.max_value()
            if new_min_v < min_v:
                min_v = new_min_v
                move[0] = action[0]
                move[1] = action[1]
            self.current_state[action[0]][action[1]] = '.'
        #print('siamo in min_value è ho selezionato', min_v, 'move', move)


        return (min_v, move )

    def min_max_decision(self):

        while True:
            self.draw_board()
            result = self.terminal_state(self.current_state)

            # Printing the appropriate message if the game has ended
            if result != None:
                if result == 'X':
                    print('The winner is X!')
                elif result == 'O':
                    print('The winner is O!')
                elif result == '.':
                    print("It's a tie!")

                return

            # If it's player's turn
            if self.player_turn == 'X':

                (m, move) = self.min_value()
                while True:

                    #start = time.time()
                    #end = time.time()
                    #print('Evaluation time: {}s'.format(round(end - start, 7)))
                    #print('Recommended move: X = {}, Y = {}'.format(move[0], move[1]))


                    '''Player vs CPU'''
                    #px = int(input('inserisci la riga (0, 1 o 2):'))
                    #py = int(input('inserisci la colonna (0, 1 o 2):'))

                    px = move[0]
                    py = move[1]
                    print('cpu2 move are' ,px,py)
                    if (px,py) in self.action(self.current_state):
                        #if self.action(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('AZIONE NON PERMESSA, RIPETERE')

            # If it's AI's turn
            else:
                (m, move) = self.max_value()
                print('la mossa pensata dalla CPU è: ',move)
                self.current_state[move[0]][move[1]] = 'O'
                self.player_turn = 'X'








    #definizione delle Heuristiche!
    def heuristic_func(self, state):

        return self.manhattan_distance(state)

    def check_position_heu(self, state):

        well_positioned = 0
        a = state.matrix
        b = self.goal_state

        for row in range(3):
            for col in range(3):
                if  (a[row][col] == b[row][col]):
                    well_positioned += 1
        return 9 - well_positioned
    '''
    def manhattan_distance(self, state):
        distance = 0
        a = state.matrix
        b = self.goal_state
        for row in range(3):
            for col in range(3):
                element = b[row][col]
                for r in range(3):
                    for c in range(3):
                        if element == a[r][c]:
                            distance = distance + abs((r-row)) + abs((c-col))
        return distance
    '''



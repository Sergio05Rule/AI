import time
import random
from Problem_State import State

# TicTacToe Game
class Game:
    def __init__(self, first_player_turn, min_max_depth = 0):
        self.current_state = State(first_player_turn)
        self.initialize_game()
        self.player_turn = first_player_turn #variabile che tiene conto quale giocatore deve muovere
        # todo si potrebbe integrare il player turn all'interno dello stato (da lasciare alla fine)
        # todo (solo priscio, no challenge) si potrebbero definire i giocatori come MIN e MAX e permettere all'utente di inserire due lettere a piacimento

        self.cs = None
        self.min_max_depth = min_max_depth
        self.depth = 0


    #inizializzo board di gioco
    def initialize_game(self):
        self.current_state.initialize_state()


    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state.board[i][j]), end=" ")
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

        # Verticale
        for i in range(0, 3):
            if (state[0][i] != '.' and
                    state[0][i] == state[1][i] and
                    state[1][i] == state[2][i]):
                return state[0][i]

        # Orizzontale
        for i in range(0, 3):
            if (state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (state[i] == ['O', 'O', 'O']):
                return 'O'

        # Diagonale 1
        if (state[0][0] != '.' and
                state[0][0] == state[1][1] and
                state[0][0] == state[2][2]):
            return state[0][0]

        # Diagonale 2
        if (state[0][2] != '.' and
                state[0][2] == state[1][1] and
                state[0][2] == state[2][0]):
            return state[0][2]

        # Tris-board piena
        for i in range(0, 3):
            for j in range(0, 3):
                if (state[i][j] == '.'):
                    return None

        # It's a tie!
        return '.'


    def max_value(self):

        max_v = -2
        result = self.current_state.terminal_state()


        possible_moves = list()

        if result == 'X':
            return (-1, None)
        elif result == 'O':
            return (1, None)
        elif result == '.':
            return (0, None)

        # debug print
        if self.depth == 0:
            print('Azioni possibili per MAX', self.current_state.action())

        temp_state = self.current_state.copy()

        #result = None -> Game not end -> continue the game
        for action in self.current_state.action():

            # todo: self.current_state = result(action)
            #self.current_state = self.current_state.result(action)
            self.current_state.board[action[0]][action[1]] = 'O'

            # dubug
            self.depth += 1

            (new_max_v, new_move) = self.min_value()

            # dubug
            self.depth -= 1

            # dubug
            if self.depth == 0:
                print('La mossa  ', action, 'ha valore', new_max_v)

            if new_max_v == max_v:
                possible_moves.append(action)

            elif new_max_v > max_v:

                max_v = new_max_v

                possible_moves.clear()
                possible_moves.append(action)

            # todo un metodo generale per annullare la mossa, al massimo si potrebbe memorizzare lo stato precedente e ripristinarlo
            self.current_state.board[action[0]][action[1]] = '.'


        # debug
        if self.depth == 0:
            print('Le migliori possibili mosse per MAX sono: ', possible_moves)

        actual_move = random.choice(possible_moves)

        return (max_v,actual_move)


    def min_value(self):
        # max_v :
        # -1 - loss
        # 0  - a tie
        # 1  - win


        min_v = +2 # inizializzata a +2, worse than the worst case
        result = self.current_state.terminal_state()

        possible_moves = list()

        # todo rendere i valori indipendenti dal problema (-1 dovrebbe essere il minimo possibile, +1 il massimo possibile, 0 in caso di pareggio)
        if result == 'X':
            return (-1, None)
        elif result == 'O':
            return (1, None)
        elif result == '.':
            return (0, None)

        # debug print
        if self.depth == 0:
            print('Azioni possibili per MIN', self.action(self.current_state.board))

        #if result = None -> Game not end -> continue the game
        for action in self.current_state.action():


            # todo: self.current_state = result(action, X)
            #self.current_state = self.current_state.result(action)
            self.current_state.board[action[0]][action[1]] = 'X'

            # dubug
            self.depth += 1

            (new_min_v,new_move)  =  self.max_value()

            # dubug
            self.depth -= 1

            if new_min_v == min_v:
                possible_moves.append(action)

            elif new_min_v < min_v:

                min_v = new_min_v

                possible_moves.clear()
                possible_moves.append(action)

            # annulla la mossa fatta per valutare quella successiva
            # todo un metodo generale per annullare la mossa, al massimo si potrebbe memorizzare lo stato precedente e ripristinarlo
            self.current_state.board[action[0]][action[1]] = '.'

        # debug print
        if self.depth == 0:
            print('Le migliori possibili mosse per MIN sono: ', possible_moves)

        actual_move = random.choice(possible_moves)

        return (min_v, actual_move)

    def min_max_decision(self, Human = False):

        while True:
            self.draw_board()
            result = self.current_state.terminal_state()

            if result != None:
                if result == 'X':
                    print('The winner is X!')
                elif result == 'O':
                    print('The winner is O!')
                elif result == '.':
                    print("It's a tie!")

                return 1    # Game ended sucessfully

            # If it's MIN turn
            if self.current_state.player_turn == 'X':

                input('Lancia MIN (premi invio per continuare)\n')

                while True:

                    move: tuple

                    if Human == True:
                        '''Player vs CPU'''
                        px = int(input('inserisci la riga (0, 1 o 2):'))
                        py = int(input('inserisci la colonna (0, 1 o 2):'))
                        move = (px,py)

                    if Human == False:
                        '''CPU vs CPU'''
                        start = time.time()
                        (m, move) = self.min_value()
                        end = time.time()
                        print('Tempo elaborazione mossa: {}s'.format(round(end - start, 7)))
                        print('La mossa pensata dalla cp1 è: ', move,' con m = ',m)

                    if move in self.action(self.current_state.board):

                        self.current_state = self.current_state.result(move)
                        break

                    else:
                        print('MOSSA NON PERMESSA, RIPETERE')

            # If it's MAX turn (always controlled by AI)
            else:

                input('Lancia MAX (premi invio per continuare)\n')
                start = time.time()
                (m, move) = self.max_value()
                end = time.time()
                print('Tempo elaborazione mossa: {}s'.format(round(end - start, 7)))
                print('La mossa pensata dalla cp1 è: ', move, ' con m = ', m)
                self.current_state = self.current_state.result(move)





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



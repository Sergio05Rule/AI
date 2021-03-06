import time
import random
#from Problem_State import State
from ForzaQuattro import State

# TicTacToe Game
class Game:
    def __init__(self, first_player_turn, max_depth = 1000):
        self.current_state = State(first_player_turn)
        self.current_state.initialize_state()
        self.player_turn = first_player_turn #variabile che tiene conto quale giocatore deve muovere
        self.max_depth = max_depth
        self.depth = 1


    def max_value(self, state):

        print('\n----------------------------')
        print('Max value function at depth ', self.depth)
        state.draw_board_reverse()
        print('max con euristica: ', state.heuristic())
        #input('avanti')

        max_v = self.current_state.worst_max_case  # inizializzata a -2, worse than the worst case

        # caso nodo foglia dell'albero, stato di termine gioco
        result = state.terminal_state()

        possible_moves = list()

        # todo sostituire 1 e -1 con euristica di soluzione MAX e soluzione MIN
        if result == 'MIN':
            return (-1000, None)
        elif result == 'MAX':
            return (1000, None)
        elif result == 'TIE':
            return (0, None)

        # Prova a fare un'altra mossa
        if self.depth < self.max_depth:
            print('Analisi alla depth: ', self.depth)

            for action in state.action():

                new_state = state.result(action)

                self.depth += 1

                (new_max_v, new_move) = self.min_value(new_state)

                self.depth -= 1

                print('Valore della foglia: ',new_max_v, 'attuale record ', max_v)

                # ho trovato una mossa che ha un'euristica pari a quella migliore trovata fin'ora
                if new_max_v == max_v:
                    possible_moves.append(action)
                    print('Scelto come nuovo max a pari valore', 'azione ', action, 'depth', self.depth)

                # ho trovato una mossa che ha un'euristica migliore
                elif new_max_v > max_v:

                    max_v = new_max_v
                    print('Scelto come nuovo max', 'azione ', action, 'depth', self.depth)

                    possible_moves.clear()
                    possible_moves.append(action)

            # debug print
            if self.depth == 1:
                print('Le migliori possibili mosse per MAX sono: ', possible_moves,' e max = ', max_v)

            print('Devo scegliere tra le mosse', possible_moves)
            actual_move = random.choice(possible_moves)

            return (max_v,actual_move)

        # Non procedere più con le mosse
        else:
            print('STOP PROFONDITA\' CON VALORE: ', state.heuristic(),'DEL GIOCATORE ', self.current_state.player_turn)
            return (state.heuristic(), None)


    def min_value(self, state):

        print('\n----------------------------')
        print('Min value function at depth ', self.depth)
        state.draw_board_reverse()
        print('min con euristica: ', state.heuristic())
        #input('avanti')

        min_v = self.current_state.worst_min_case  # inizializzata a +2, worse than the worst case

        # caso nodo foglia dell'albero, stato di termine gioco
        result = state.terminal_state()

        possible_moves = list()

        # todo sostituire 1 e -1 con euristica di soluzione MAX e soluzione MIN
        if result == 'MIN':
            return (-1000, None)
        elif result == 'MAX':
            return (1000, None)
        elif result == 'TIE':
            return (0, None)

        # Prova a fare un'altra mossa
        if self.depth < self.max_depth:
            print('Analisi alla depth: ', self.depth)

            for action in state.action():

                new_state = state.result(action)

                self.depth += 1

                (new_min_v,new_move) = self.max_value(new_state)

                self.depth -= 1

                print('Valore della foglia: ',new_min_v, 'attuale record ', min_v)

                # ho trovato una mossa che ha un'euristica pari a quella migliore trovata fin'ora
                if new_min_v == min_v:
                    print('Scelto come nuovo min a pari valore', 'azione ', action, 'depth', self.depth)
                    possible_moves.append(action)

                # ho trovato una mossa che ha un'euristica migliore
                elif new_min_v < min_v:
                    print('Scelto come nuovo min', 'azione ', action, 'depth', self.depth)
                    min_v = new_min_v

                    possible_moves.clear()
                    possible_moves.append(action)

            # debug print
            if self.depth == 1:
                print('Le migliori possibili mosse per MIN sono: ', possible_moves,' e min = ', min_v)

            #print('Mosse terminate, le mosse migliori sono: ', possible_moves)
            #input('Avanti')
            print('Devo scegliere tra le mosse', possible_moves)
            actual_move = random.choice(possible_moves)
            print('Mossa scelta, ', actual_move, 'alla profondità: ', self.depth)
            return (min_v, actual_move)

        # Non procedere più con le mosse
        else:
            print('STOP PROFONDITA\' CON VALORE: ', state.heuristic(),'DEL GIOCATORE ', self.current_state.player_turn)
            return (state.heuristic(), None)


    def min_max_decision(self, Human = False):

        while True:
            self.current_state.draw_board_reverse()
            result = self.current_state.terminal_state()

            if result != None:
                if result == 'MIN':
                    print('The winner is', self.current_state.min)
                elif result == 'MAX':
                    print('The winner is', self.current_state.max)
                elif result == 'TIE':
                    print("It's a tie!")

                return 1    # Game ended sucessfully

            # If it's MIN turn
            if self.current_state.player_turn == 'MIN':

                input('Lancia MIN (premi invio per continuare)\n')

                while True:

                    move: tuple

                    if Human is True:
                        '''Player vs CPU'''
                        px = int(input('inserisci la riga (0, 1 o 2):'))
                        py = int(input('inserisci la colonna (0, 1 o 2):'))
                        move = (px,py)

                    if Human is False:
                        '''CPU vs CPU'''
                        start = time.time()

                        (m, move) = self.min_value(self.current_state)
                        #(m, move) = self.min_value_alpha_beta(temp_state,-2,2)

                        end = time.time()
                        print('Tempo elaborazione mossa: {}s'.format(round(end - start, 7)))
                        print('La mossa pensata dalla cp1 è: ', move,' con m = ',m)

                    if move in self.current_state.action():

                        self.current_state = self.current_state.result(move)
                        break

                    else:
                        print('MOSSA NON PERMESSA, RIPETERE')

            # If it's MAX turn (always controlled by AI)
            else:

                input('Lancia MAX (premi invio per continuare)\n')
                start = time.time()

                (m, move) = self.max_value(self.current_state)
                #(m, move) = self.max_value_alpha_beta(temp_state,-2,2)


                end = time.time()
                print('Tempo elaborazione mossa: {}s'.format(round(end - start, 7)))
                print('La mossa pensata dalla cp1 è: ', move, ' con m = ', m)
                self.current_state = self.current_state.result(move)

    def min_value_alpha_beta(self, state, alpha, beta):  # self.min_value_alpha_beta(-2, 2)

        min_v = +2
        result = state.terminal_state()

        possible_moves = list()
        result_action = None

        if result == 'MIN':
            return (-1, None)
        elif result == 'MAX':
            return (1, None)
        elif result == '.':
            return (0, None)

            # debug print
        if self.depth == 0:
            print('Azioni possibili per MIN_ab', state.action())

        for action in state.action():

            new_state = state.result(action)

            # dubug
            self.depth += 1

            (new_min_v, new_move) = self.max_value_alpha_beta(new_state, alpha, beta)

            # dubug
            self.depth -= 1

            # dubug
            if self.depth == 0:
                print('La mossa  ', action, 'ha valore', new_min_v)

            if new_min_v < min_v:
                min_v = new_min_v
                result_action = action

            if min_v <= alpha:
                return (min_v, result_action)

            if min_v < beta:
                beta = min_v

        # debug print
        '''
        if self.depth == 0:
            print('Le migliori possibili mosse per MIN sono: ', possible_moves)
        '''

        return (min_v, result_action)

    def max_value_alpha_beta(self, state, alpha, beta):  # self.max_value_alpha_beta(-2, 2)

        max_v = -2
        result = state.terminal_state()

        possible_moves = list()
        result_action = None

        if result == 'MIN':
            return (-1, None)
        elif result == 'MAX':
            return (1, None)
        elif result == '.':
            return (0, None)

        # debug print
        if self.depth == 0:
            print('Azioni possibili per MAX_ab', state.action())

        for action in state.action():

            new_state = state.result(action)

            # dubug
            self.depth += 1

            (new_max_v, new_move) = self.min_value_alpha_beta(new_state, alpha, beta)

            # dubug
            self.depth -= 1

            # dubug
            if self.depth == 0:
                print('La mossa  ', action, 'ha valore', new_max_v)

            if new_max_v > max_v:
                max_v = new_max_v
                result_action = action

            state.board[action[0]][action[1]] = '.'

            if max_v >= beta:
                return (max_v, result_action)

            if max_v > alpha:
                alpha = max_v

        # debug print
        if self.depth == 0:
            print('Le migliori possibili mosse per MIN sono: ', result_action)

        return (max_v, result_action)



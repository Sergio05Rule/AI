import Game as G

if __name__ == '__main__':

    FirstMove = 'MAX'
    min_max_depth = 5

    g = G.Game(FirstMove, min_max_depth) #inizializzo gioco

    Human = False
    g.min_max_alfa_beta(Human)




class State:
    def __init__(self, t):
        self.pos = t
        self.x = t[0]
        self.y = t[1]

    def print_state(self):
        print(self.pos)
        print(self.x)
        print(self.y)

def NotinClosed(problem, node): #restituisce 1 se lo stato non è stato già visitato (al netto di controlli sulla depth) è quindi bisogna aggiungerlo
    NotVisited = 1

    for element in problem.closed:

        if node.state.pos == element.state.pos:
                NotVisited = 0

    return NotVisited

def check_obstacles(list ,state, direction, width, height):

    #print('STO ANALIZZANDO GLI OSTACOLI DI ', state.pos, 'IN DIREZIONE ', direction)

    flag = 1

    if direction == 'TOP':
        check_pos = (state.x-1, state.y)
       # print('CHECK POS TOP VALE:', check_pos)
        if check_pos[0] == -1:
            flag = 0
    if direction == 'DOWN':
        check_pos = (state.x+1, state.y)
       # print('CHECK POS DOWN VALE:', check_pos)
        if check_pos[0] == height:
            flag = 0
    if direction == 'RIGHT':
        check_pos = (state.x, state.y+1)
        #print('CHECK POS RIGHT VALE:', check_pos)
        if check_pos[1] == width:
            flag = 0
    if direction == 'LEFT':
        check_pos = (state.x, state.y-1)
        #print('CHECK POS LEFT VALE:', check_pos)
        if check_pos[1] == -1:
            flag = 0

   #print('----- ', len(list), '-----')

    for wall in list:
        #print(' IL MURO È ', wall)
        if check_pos[0] == wall[0] and check_pos[1] == wall[1]:
           # print('TROVATO MURO IN POSIZIONE: ', check_pos,' :', wall)
            flag = 0
    #print('----- IL FLAG VALE:', flag)
    return flag

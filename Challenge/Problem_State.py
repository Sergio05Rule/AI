
class State:
    def __init__(self, id):
        self.id = id


def NotinClosed(problem, node): #restituisce 1 se lo stato non è stato già visitato (al netto di controlli sulla depth) è quindi bisogna aggiungerlo
    NotVisited = 1

    for element in problem.closed:

        if problem.fringe_type == 'DLS' or problem.fringe_type == 'IDS':
            if node.state.id == element.state.id and node.depth >= element.depth:
                NotVisited = 0
        else:
            if node.state.id == element.state.id:
                NotVisited = 0

    return NotVisited
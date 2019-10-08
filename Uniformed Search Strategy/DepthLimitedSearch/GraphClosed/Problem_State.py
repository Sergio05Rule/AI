
class State:
    def __init__(self, id):
        self.id = id


def NotinClosed(problem, node): #restituisce 1 se lo stato non è stato già visitato (al netto di controlli sulla depth) è quindi bisogna aggiungerlo
    NotVisited = 1
    for tuple in problem.closed:
        if node.state.id == tuple[0].id and node.depth >= tuple[1]:
            NotVisited = 0 #presente nei visited ma selected_node ha maggiore/uguale depth
    return NotVisited
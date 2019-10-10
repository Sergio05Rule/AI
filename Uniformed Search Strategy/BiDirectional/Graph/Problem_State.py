

class State:
    def __init__(self, id):
        self.id = id


def check_state(state,g): # Check if an element is in the graph
    bool = 0
    for vertex in g.get_vertices():
        if state == vertex:
            bool = 1

    if bool == 0:
        print('\nABORT EXECUTION:',state,' is not a graph element!')
        sys.exit()
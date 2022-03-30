
from Solver import *
from Util import *


class BreadthFirstSearch(Solver):
    
    def solve(self, tent):
        x=0
        queue = Queue()
        solution = None
        state = tent.state
        trees = tent.trees
        start = Node(state, trees,tent,[])
        queue.push(start)

        while queue.empty() == False:
            x+=1

            top = queue.pop()
            state = top.state

            if tent.is_goal_state(state):
                print(x)
                solution = top
                break

            nodes = top.expand_node()

            for node in nodes:
                if tent.is_legal_state(node.state):
                    queue.push(node)    

        return solution

    
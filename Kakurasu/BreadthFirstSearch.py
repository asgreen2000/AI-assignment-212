
from Solver import *
from Util import *


class BreadthFirstSearch(Solver):
    
    def solve(self, binaro):
        
        queue = Queue()
        solution = None

        start = Node(binaro.grid, None, [])
        
        queue.push(start)

        while queue.empty() == False:
            
            front = queue.pop()
            state = front.state
            path = front.path
 
            
            if binaro.is_goal_state(state):
                solution = front
                break

            nodes = front.expand_node()

            for node in nodes:
                if binaro.is_legal_state(node.state):
                    queue.push(node)    

        return solution

    
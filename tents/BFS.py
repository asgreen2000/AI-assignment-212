
from Solver import *
from Util import *


class BreadthFirstSearch(Solver):
    
    def solve(self, tent):
        
        queue = Queue()
        solution = None
        state = tent.state
        trees = tent.trees
        start = Node(state, trees,tent,[])
        
        queue.push(start)

        while queue.empty() == False:
            
            top = queue.pop()
            state = top.state
            path = top.path
 
            
            if tent.is_goal_state(state):
                solution = top
                break

            nodes = top.expand_node()

            for node in nodes:
                if tent.is_legal_state(node.state):
                    queue.push(node)    

        return solution

    
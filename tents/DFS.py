
from Solver import *
from Util import *


class DepthFirstSearch(Solver):
    
    def solve(self, tent):
        stack = Stack()
        solution = None
        state = tent.state
        trees = tent.trees
        start = Node(state, trees,tent,[])
        visited = []

        stack.push(start)
        count = 0
        while stack.empty() == False:
            
            top = stack.pop()
            state = top.state
            path = top.path
            
            count += 1
            visited += [str(state)]
            if tent.is_goal_state(state):
                solution = top
                break

            nodes = top.expand_node()

            for node in nodes:
                if visited.count(str(node.state)) == 0:
                    stack.push(node)    
        
        return solution

    
from Tents import *
import math
import Util
# Visitor pattern is used for implementing these classes
# let_me_solve reprensents visit method

class SearchAlgo:
    # this method return solution's path
    def solve(self, tents):
        pass
    def let_me_solve(self, tents):
        return tents.accept(self)

class AStarSearch(SearchAlgo):
    
    def solve(self, tents):
        return "A*"



class DepthFirstSearch(SearchAlgo):
    
    def solve(self, tents):

        pass


class BreadthFirstSearch(SearchAlgo):

    def solve(self, tents):
        
        queue = Util.Queue()
        state = tents.state
        size = tents.size
        frontier = Node(tents.state)

        queue.push(frontier)

        while queue.empty() == False:
            
            frontier = queue.pop()
            state = frontier.state
        
            if tents.is_goal_state(state):
                return state
        
            nodes = frontier.expand_node(tents)

            for node in nodes:
                queue.push(node)
            

        return []
            
class Node:

    def __init__(self, state):
        self.state = Util.deep_copy(state)

    def tents_at(self,row_idx, col_idx):
        self.state[row_idx][col_idx] = Tents.TENT
    
    def nothing_at(self, row_idx, col_idx):
        self.state[row_idx][col_idx] = Tents.NOTHING

    def expand_node(self, tents):
        #find first empty cell
        size = tents.size
        for row_idx in range(size):
            for col_idx in range(size):
                if self.state[row_idx][col_idx] == Tents.EMPTY:

                    res = []
                    first_child = Node(self.state)
                    first_child.tents_at(row_idx, col_idx)
                    if str(self.state[1]) == "[1, 2, 3, 3, 3, 2]":
                        print(self.state)
                    if tents.is_legal_state(first_child.state):
                        
                        res += [first_child]
                    
                    second_child = Node(self.state)
                    second_child.nothing_at(row_idx, col_idx)
                    
                    if tents.is_legal_state(second_child.state):
                        res += [second_child]

                    return res
        
        return []
                    

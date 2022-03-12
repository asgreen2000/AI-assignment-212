from Hitori import *

class SearchAlgo:
    # this method return solution's path
    def solve(self, init_state, n):
        pass
    def let_me_solve(self, hitori):
        return hitori.accept(self)

class DepthFirstSearch(SearchAlgo):
    
    def solve(self, init_state, n):
        return "DFS"

class AStarSearch(SearchAlgo):
    
    def solve(self, init_state, n):
        return "A*"

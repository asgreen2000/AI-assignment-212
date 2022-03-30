from DFS import DepthFirstSearch
from BFS import BreadthFirstSearch
from AStarSearch import AStarSearch
import Constant
from Util import *


class Tents(Subscriber):

    def __init__(self, state, row_const, col_const, size):
        self.grid = create_square_list(Constant.UNSET, size)
        self.state = state
        self.row_const = row_const
        self.col_const = col_const
        self.size = size
        self.trees = self.generate_list_tree()
        self.solver = None

    def solve_by_dfs(self):
        self.solver = DepthFirstSearch()
        self.solution = self.solver.solve(self)
    
    def solve_by_bfs(self):
        self.solver = BreadthFirstSearch()
        self.solution = self.solver.solve(self)
        
    def solve_by_a_star(self):
        self.solver = AStarSearch()
        self.solution = self.solver.solve(self)

    def generate_list_tree(self):
        self.trees = []
        
        for row_idx in range(self.size):
            for col_idx in range(self.size):
                number = self.state[row_idx][col_idx]
                if number == Constant.TREE:
                    self.trees += [[row_idx, col_idx]]

        return self.trees

    def generate_steps(self):
        res = []

        if self.solution:
            res = self.solution.generate_steps()
        return res

    def update_grid(self, row, col):
        pass
    
    def can_have_tent_at(self, state, row_idx, col_idx):
        
        if row_idx < 0 or row_idx >= self.size or col_idx < 0 or col_idx >= self.size:
            return False

        count_row_tents = 0
        count_col_tents = 0
        for i in range(self.size):
            if state[row_idx][i] == Constant.TENT:
                count_row_tents += 1
            if state[i][col_idx] == Constant.TENT:
                count_col_tents += 1

        if count_col_tents > self.col_const[col_idx] or count_row_tents > self.row_const[row_idx]:
            return False

        # check tent in horizontal, vertical direction
        if row_idx > 0 and state[row_idx - 1][col_idx] == Constant.TENT:
            return False
        if col_idx > 0 and state[row_idx][col_idx - 1] == Constant.TENT:
            return False
        if row_idx < self.size - 1 and state[row_idx + 1][col_idx] == Constant.TENT:
            return False
        if col_idx < self.size - 1 and state[row_idx][col_idx + 1] == Constant.TENT:
            return False

        # check diagonally
        if row_idx > 0 and col_idx > 0 and state[row_idx - 1][col_idx - 1] == Constant.TENT:
            return False
        if row_idx > 0 and col_idx < self.size - 1 and state[row_idx - 1][col_idx + 1] == Constant.TENT:
            return False
        if row_idx < self.size - 1 and col_idx > 0 and state[row_idx + 1][col_idx - 1] == Constant.TENT:
            return False        
        if row_idx > 0 and row_idx < self.size - 1 and col_idx < self.size - 1 and state[row_idx + 1][col_idx + 1] == Constant.TENT:
            return False

        return True

    def is_legal_state(self, state):        
        for row_idx in range(self.size):
            for col_idx in range(self.size):
                if state[row_idx][col_idx] == Constant.TENT:
                    if self.can_have_tent_at(state, row_idx, col_idx) == False:
                        return False
        
        return True

    def have_beside(self, state, row_idx, col_idx,val):
        if row_idx > 0 and state[row_idx - 1][col_idx] == val:
            return True
        if row_idx < self.size - 1 and state[row_idx + 1][col_idx] == val:
            return True
        if col_idx > 0 and state[row_idx][col_idx - 1] == val:
            return True
        if col_idx < self.size - 1 and state[row_idx][col_idx + 1] == val:
            return True

        return False

    def is_goal_state(self, state):
        

        row=[]
        col=[]
        for tree in self.trees:
            if self.have_beside(state,tree[0],tree[1],2)==False:
                return False
        for i in self.row_const :
            row+=[i]
        for i in self.col_const :
            col+=[i]
        for x in range(len(state)):
            for y in state[x]:
                if y==2:
                    row[x]-=1
        for x in range(len(state)):
            for y in range(len(state)):
                if state[y][x]==2:
                    col[x]-=1
        for i in row:
            if i !=0:
                return False
       
        for i in col:
            if i !=0:
                return False


        return True
    
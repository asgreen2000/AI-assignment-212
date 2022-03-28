import Constant
from Util import *


class Solver:

    def solve(self, kakurasu):
        pass


class Node:

    def __init__(self, state,trees, tents, path):

        self.state = deep_copy(state)
        self.row_const = tents.row_const
        self.col_const =tents.col_const
        self.path = path
        self.trees = trees
        self.tents=tents
        self.size = len(self.row_const)
        if len(self.path) > 0:
            row = self.path[len(self.path) - 1][0]
            col = self.path[len(self.path) - 1][1]
            self.state[row][col] = Constant.TENT
        
    def tents_at(self,row_idx, col_idx):
        self.state[row_idx][col_idx] = Constant.TENT
        
    def nothing_at(self, row_idx, col_idx):
        self.state[row_idx][col_idx] = Constant.NOTHING

    def check_neighbor(self,row_idx,col_idx):
        val=0
        if self.state[row_idx][col_idx] == Constant.TENT:
            return False
        if row_idx > 0 and self.state[row_idx - 1][col_idx] == Constant.TREE  :
            val+=1
        if row_idx < self.size - 1 and self.state[row_idx + 1][col_idx] == Constant.TREE :
            val+=1
        if col_idx > 0 and self.state[row_idx][col_idx - 1] == Constant.TREE  :
            val+=1
        if col_idx < self.size - 1 and self.state[row_idx][col_idx + 1] == Constant.TREE :
            val+=1
        return val>0

    def expand_node(self):

            res = []
            size = len(self.state) if self.state else 0
            for row_idx in range(size):
                for col_idx in range(size):

                   
                    if self.state[row_idx][col_idx] == Constant.UNSET and Node.check_neighbor(self,row_idx,col_idx)==True:                        
                        first_child = type(self)(self.state, self.trees,self.tents,self.path + [[row_idx, col_idx]])

                        first_child.tents_at(row_idx, col_idx)  
                        res += [first_child]
            
            return res

    def generate_steps(self):

        state = create_square_list('_', self.size)
        res = []

        res += [str_square_list(state, "\n")]

        for pos in self.path:
            state[pos[0]][pos[1]] = 'X'
            
            res += [str_square_list(state, "\n")]
        
        return res


 
 
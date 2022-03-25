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
    

    def check_neighbor(self,row_idx,col_idx,val):
        size = len(self.state) 
        if  self.state[row_idx][col_idx] ==val:
            return False
        if row_idx>0 and row_idx<size-1 and col_idx>0 and col_idx<size-1:
            if  self.state[row_idx-1][col_idx] ==val or  self.state[row_idx+1][col_idx] ==val or  self.state[row_idx][col_idx-1]==val or self.state[row_idx][col_idx+1]==val :
                    return True
        elif row_idx==0 and col_idx>0 and col_idx<size-1:
            if   self.state[row_idx+1][col_idx] ==val or  self.state[row_idx][col_idx-1]==val or  self.state[row_idx][col_idx+1]==val :
                    return True
        elif row_idx==size-1 and col_idx>0 and col_idx<size-1:
            if   self.state[row_idx-1][col_idx] ==val or  self.state[row_idx][col_idx-1]==val or  self.state[row_idx][col_idx+1]==val :
                    return True
        elif row_idx>0 and row_idx<size-1 and col_idx==0:
            if   self.state[row_idx-1][col_idx] ==val or  self.state[row_idx+1][col_idx]==val or  self.state[row_idx][col_idx+1]==val :
                    return True
        elif row_idx>0 and row_idx<size-1 and col_idx==size-1:
            if   self.state[row_idx-1][col_idx] ==val or  self.state[row_idx+1][col_idx]==val or  self.state[row_idx][col_idx-1]==1 :
                    return True
        elif row_idx==0 and col_idx==0:
            if  self.state[row_idx+1][col_idx] ==val or  self.state[row_idx][col_idx+1]==val:
                    return True
        elif row_idx==0 and col_idx==size-1:
            if  self.state[row_idx+1][col_idx] ==val or  self.state[row_idx][col_idx-1]==val:
                    return True
        elif row_idx==size-1 and col_idx==0:
            if  self.state[row_idx-1][col_idx] ==val or  self.state[row_idx][col_idx+1]==val:
                    return True
        elif row_idx==size-1 and col_idx==size-1:
            if  self.state[row_idx-1][col_idx] ==val or  self.state[row_idx][col_idx-1]==val:
                    return True
        return False

    def check_can_tent(self,row_idx,col_idx,val):
        size = len(self.state) 
        if  self.state[row_idx][col_idx] ==val:
            return False
        if row_idx>0 and row_idx<size-1 and col_idx>0 and col_idx<size-1:
            if  self.state[row_idx-1][col_idx] ==val or  self.state[row_idx+1][col_idx] ==val or  self.state[row_idx][col_idx-1]==val or self.state[row_idx][col_idx+1]==val or self.state[row_idx+1][col_idx+1]==val or self.state[row_idx-1][col_idx-1]==val or self.state[row_idx-1][col_idx+1]==val or self.state[row_idx+1][col_idx-1]==val :
                    return False
        elif row_idx==0 and col_idx>0 and col_idx<size-1:
            if   self.state[row_idx+1][col_idx] ==val or  self.state[row_idx][col_idx-1]==val or  self.state[row_idx][col_idx+1]==val or self.state[row_idx+1][col_idx-1]==val or self.state[row_idx+1][col_idx+1]==val :
                    return False
        elif row_idx==size-1 and col_idx>0 and col_idx<size-1:
            if   self.state[row_idx-1][col_idx] ==val or  self.state[row_idx][col_idx-1]==val or  self.state[row_idx][col_idx+1]==val  or self.state[row_idx-1][col_idx+1]==val or self.state[row_idx-1][col_idx-1]==val:
                    return False
        elif row_idx>0 and row_idx<size-1 and col_idx==0:
            if   self.state[row_idx-1][col_idx] ==val or  self.state[row_idx+1][col_idx]==val or  self.state[row_idx][col_idx+1]==val  or self.state[row_idx-1][col_idx+1]==val or self.state[row_idx+1][col_idx+1]==val:
                    return False
        elif row_idx>0 and row_idx<size-1 and col_idx==size-1:
            if   self.state[row_idx-1][col_idx] ==val or  self.state[row_idx+1][col_idx]==val or  self.state[row_idx][col_idx-1]==1  or self.state[row_idx-1][col_idx-1]==val or self.state[row_idx+1][col_idx-1]==val:
                    return False
        elif row_idx==0 and col_idx==0:
            if  self.state[row_idx+1][col_idx] ==val or  self.state[row_idx][col_idx+1]==val  or self.state[row_idx+1][col_idx+1]==val:
                    return False
        elif row_idx==0 and col_idx==size-1:
            if  self.state[row_idx+1][col_idx] ==val or  self.state[row_idx][col_idx-1]==val or self.state[row_idx+1][col_idx-1]==val:
                    return False
        elif row_idx==size-1 and col_idx==0:
            if  self.state[row_idx-1][col_idx] ==val or  self.state[row_idx][col_idx+1]==val or self.state[row_idx-1][col_idx+1]==val:
                    return False
        elif row_idx==size-1 and col_idx==size-1:
            if  self.state[row_idx-1][col_idx] ==val or  self.state[row_idx][col_idx-1]==val or self.state[row_idx-1][col_idx-1]==val:
                    return False
        return True

    def expand_node(self):

            res = []
            size = len(self.state) if self.state else 0
            for row_idx in range(size):
                for col_idx in range(size):

                   
                    if self.state[row_idx][col_idx] == Constant.UNSET and Node.check_neighbor(self,row_idx,col_idx,1)==True:                        
                        first_child = type(self)(self.state, self.trees,self.tents,self.path + [[row_idx, col_idx]])

                        first_child.tents_at(row_idx, col_idx)  
                        res += [first_child]
            
            return res

    def generate_steps(self):

        state = create_square_list(Constant.UNSET, self.size)
        res = []

        res += [str_square_list(state, "\n")]

        for pos in self.path:
            state[pos[0]][pos[1]] = Constant.TENT
            
            res += [str_square_list(state, "\n")]
        
        return res


 
 
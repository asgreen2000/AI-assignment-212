import Constant
from Solver import *
from Util import *


class AStarSearch(Solver):
    
    class CustomNode(Node):

        def __init__(self, state,trees, tents, path):
            super().__init__( state,trees, tents, path)
            self.state = deep_copy(state)
            self.trees = trees
            self.tents=tents
            self.size = len(self.state)
            self.g_value = self.cal_g_value() # number of used tents
            self.h_value = self.cal_h_value() # number of tents need to be placed
            self.totcal_cost = self.g_value + self.h_value
            self.col_const=tents.col_const
            self.row_const=tents.row_const


        def get_total_cost(self):
            return self.g_value + self.h_value

        def cal_g_value(self):
            count = 0
            
            for row in self.state:
                for number in row:
                    if number == Constant.TENT:
                        count += 1

            return count
        
        # def cal_h_value(self):
        #     tents_map = []

        #     for i in range(self.size):
        #         tents_map += [[0] * self.size]

        #     count = 0
        
        #     for tree in self.trees:
        #         row_idx = tree[0]
        #         col_idx = tree[1]
        #         count += 1
        #         if row_idx > 0 and self.state[row_idx - 1][col_idx] == Constant.TENT and tents_map[row_idx - 1][col_idx] != 1:
        #             tents_map[row_idx - 1][col_idx] = 1
        #         elif row_idx < self.size - 1 and self.state[row_idx + 1][col_idx] == Constant.TENT and tents_map[row_idx + 1][col_idx] != 1:
        #             tents_map[row_idx + 1][col_idx] = 1
        #         elif col_idx > 0 and self.state[row_idx][col_idx - 1] == Constant.TENT and tents_map[row_idx][col_idx - 1] != 1:
        #             tents_map[row_idx][col_idx - 1] = 1
        #         elif col_idx < self.size - 1 and self.state[row_idx][col_idx + 1] == Constant.TENT and tents_map[row_idx][col_idx + 1] != 1:
        #             tents_map[row_idx][col_idx + 1] = 1
        #         else:
                   
        #             count -= 1
        #     return len(self.trees) - count

        # def cal_h_value(self):

        #     res=0
        #     for x in range(self.size):
        #         for y in range(self.size):
        #             if self.tents.can_have_tent_at(self.state,x,y)==True and self.state[x][y]!=1 and self.state[x][y]!=2 and self.tents.have_beside(self.state,x,y,1)==True:
        #                 res+=1

        #     return res

        def cal_h_value(self):

            col= self.col_const
            row=self.row_const
            res =0
            for x in range(self.size):
                tmp=0
                for y in range(self.size):
                    if self.tents.can_have_tent_at(self.state,x,y)==True and self.state[x][y]!=1 and self.state[x][y]!=2 and self.tents.have_beside(self.state,x,y,1)==True:
                        tmp+=1 
                if row[x]==tmp:
                    res+=1
            for x in range(self.size):
                tmp=0
                for y in range(self.size):
                    if self.tents.can_have_tent_at(self.state,y,x)==True and self.state[y][x]!=1 and self.state[y][x]!=2 and self.tents.have_beside(self.state,y,x,1)==True:
                        tmp+=1 
                if col[x]==tmp:
                    res+=1


            return self.size*2-res
            
    def compare(self, node_a, node_b):
        return node_a.totcal_cost <= node_b.totcal_cost

    def solve(self, tent):

        open_queue = PriorityQueue(self.compare)
        solution = None
        closed = []
        state = tent.state
        trees = tent.trees

        frontier = AStarSearch.CustomNode(state, trees,tent,[])
        open_queue.push(frontier)

        while open_queue.empty() == False:

            frontier = open_queue.pop()
            state = frontier.state
            closed += [str(state)]

            if tent.is_goal_state(state):
                solution = frontier
                break
            
            nodes = frontier.expand_node()
            
            for node in nodes:
                str_state = str(node.state)
                if tent.is_legal_state(node.state) and closed.count(str_state) == 0:
                    open_queue.push(node)      
      
        return solution

  
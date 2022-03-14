from Tents import *
import math
import Util
# Visitor pattern is used for implementing these classes
# let_me_solve reprensents visit method

class TrackNode:

    def __init__(self, forest, row_const, col_const, parent, tree_index):
        self.forest = Util.clone_two_dimen_list(forest)
        self.row_const = row_const + []
        self.col_const = col_const + []
        self.parent = parent
        self.tree_index = tree_index + 0

    def tents_at(self,row_idx, col_idx):
        self.forest[row_idx][col_idx] = Tents.TENT
        self.row_const[row_idx] -= 1
        self.col_const[col_idx] -= 1

class SearchAlgo:
    # this method return solution's path
    def solve(self, tents):
        pass
    def let_me_solve(self, tents):
        return tents.accept(self)

class DepthFirstSearch(SearchAlgo):
    
    def solve(self, tents):
        return []

class AStarSearch(SearchAlgo):
    
    def solve(self, tents):
        return "A*"


class BreadthFirstSearch(SearchAlgo):

    def solve(self, tents):

        forest = tents.forest
        row_const = tents.row_const
        col_const = tents.col_const
        size = tents.size
        trees = tents.generate_list_tree()

        queue = Util.Queue()

        front_node = TrackNode(forest, row_const, col_const, None, 0)

        queue.push(front_node)

        while queue.empty() == False:
            
            tree = queue.pop()
            tree_index = tree.tree_index
            
            forest = tree.forest
            if tree_index >= len(trees):
                return forest
            row_idx = trees[tree_index][0]
            col_idx = trees[tree_index][1]
            row_const = tree.row_const
            col_const = tree.col_const
            
            

            if Tents.can_have_tents_at(forest, row_const, col_const, row_idx - 1, col_idx, size):
                new_tent = TrackNode(forest, row_const, col_const, tree, tree_index + 1)
                new_tent.tents_at(row_idx - 1, col_idx)
                queue.push(new_tent)
                
            if Tents.can_have_tents_at(forest, row_const, col_const, row_idx + 1, col_idx, size):
                
                new_tent = TrackNode(forest, row_const, col_const, tree, tree_index + 1)
                new_tent.tents_at(row_idx + 1, col_idx)
                queue.push(new_tent)
                
            if Tents.can_have_tents_at(forest, row_const, col_const, row_idx, col_idx - 1, size):
               
                new_tent = TrackNode(forest, row_const, col_const, tree, tree_index + 1)
                new_tent.tents_at(row_idx, col_idx - 1)
                queue.push(new_tent)
                

            if Tents.can_have_tents_at(forest, row_const, col_const, row_idx, col_idx + 1, size):
                
                new_tent = TrackNode(forest, row_const, col_const, tree, tree_index + 1)
                new_tent.tents_at(row_idx, col_idx + 1)
                queue.push(new_tent)
                
        return []
            




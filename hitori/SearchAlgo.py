from Hitori import *
import math
import Util
# Visitor pattern is used for implementing these classes
# let_me_solve reprensents visit method


class TrackNode:
    
    def __init__(self, state ,count , path, rows_track, cols_track, row_idx):
        self.state = Util.clone_two_dimen_list(state)
        self.count = count + 0
        self.path = Util.clone_two_dimen_list(path)
        self.rows_track = rows_track + []
        self.cols_track = cols_track + []
        self.row_idx = row_idx + 0

class SearchAlgo:
    # this method return solution's path

    def solve(self, hitori):
        pass
    def let_me_solve(self, hitori):
        return hitori.accept(self)
    
    def get_track(self, state, n):
        """This method return a 2d list tracking cells
        breaking the game rules"""
        rows_track = []
        cols_rack = []
        for i in range(n):
            rows_track += [[0] * (n + 1)]
            cols_rack += [[0] * (n + 1)]
        count_invalid_cell = 0
        for i in range(n):
            for j in range(n):
                number = state[i][j]
                count_invalid_cell += 1 if rows_track[i][number] > 0 else 0
                count_invalid_cell += 1 if cols_rack[j][number] > 0 else 0
                rows_track[i][number] += 1
                cols_rack[j][number] += 1
        
        return rows_track, cols_rack, count_invalid_cell

class DepthFirstSearch(SearchAlgo):
    
    def solve(self, hitori):
        return []

class AStarSearch(SearchAlgo):
    
    def solve(self, hitori):
        return "A*"


class BreadthFirstSearch(SearchAlgo):

    def solve(self, hitori):
        init_state = hitori.get_init_state()
        n = hitori.get_game_size()

        cells_to_take_list = [i for i in range(1, math.ceil(n / 2) + 1)]

        rows_track, cols_track, count_invalid = self.get_track(init_state, n)

        queue = Util.Queue()

        front_node = TrackNode(init_state, count_invalid, [], rows_track, cols_track, -1)

        queue.push(front_node)

        while queue.empty() == False:
            
            front_node = queue.pop()

            state = front_node.state
            path = front_node.path
            count = front_node.count
            rows_track = front_node.rows_track
            cols_track = front_node.cols_track
            # calculate next row index
            row_idx = front_node.row_idx + 1

            if count == 0:
                return path
            if row_idx == n:
                continue

            
            new_node = TrackNode(state, count, path, rows_track, cols_track, row_idx)
            
            queue.push(new_node)

            for cells_to_take in cells_to_take_list:
                step = 2
                upper_bound = n - (1 + (cells_to_take - 1) * 2) + 1

                for i in range(0, upper_bound):

                    new_node = TrackNode(state, count, path, rows_track, cols_track, row_idx)
                    should_push = False
                    for col_idx in range(i, (cells_to_take - 1) * 2 + 1, step):

                        should_push = True
                        number = new_node.state[i][col_idx]

                        if i > 0 and new_node.state[i - 1][col_idx] == Hitori.BLACK_CELL:
                            should_push = False
                            break
                        
                        new_node.state[row_idx][col_idx] = Hitori.BLACK_CELL
                       
                        new_node.path += [[new_node.row_idx, col_idx]]
                        new_node.rows_track[new_node.row_idx][number] -= 1
                        new_node.cols_track[col_idx][number] -= 1
                        if new_node.rows_track[new_node.row_idx][number] > 0:
                            new_node.count -= 1
                            
                        if new_node.cols_track[col_idx][number] > 0:
                            new_node.count -= 1
                    
                    if should_push == True:
                        should_push = Hitori.valid_move_at_row(new_node.state, new_node.row_idx, n)

                    if should_push == True:
                        queue.push(new_node)
        return []







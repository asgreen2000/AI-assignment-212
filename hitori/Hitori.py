class Hitori:
    BLACK_CELL = 0
    
    def __init__(self, init_state, n):
        self.init_state = init_state
        self.n = n

    # receive solver and call solve mmethod
    def accept(self, solver):
        return solver.solve(self)
    def get_init_state(self):
        return self.init_state
    def get_game_size(self):
        return self.n
    
    @staticmethod
    def valid_move(state):
        """define rules of this game in this method"""
        pass

    @staticmethod
    def valid_move_at_row(state, index, n):
        if index < 0 or index >= n:
            raise IndexError("List index is out of range!")
        flag = True

        """Only check above"""
        if index > 0:
            flag = flag and Hitori.exist_single_in_row(state, index - 1, n)
        flag = flag and Hitori.exist_single_in_row(state, index, n)

        return flag

    @staticmethod
    def exist_single_in_row(state, rowIndex, n):
        
        flag = False
        for index in range(0, n):
            if state[rowIndex][index] != Hitori.BLACK_CELL:
                
                if index > 0:
                    flag = flag or state[rowIndex][index - 1] != Hitori.BLACK_CELL
                if index < n - 1:
                    flag = flag or state[rowIndex][index + 1] != Hitori.BLACK_CELL
                if rowIndex > 0:
                    flag = flag or state[rowIndex - 1][index] != Hitori.BLACK_CELL
                if rowIndex < n - 1:
                    flag = flag or state[rowIndex + 1][index] != Hitori.BLACK_CELL
        
        return flag

    @staticmethod

    def check_duplicate_in_row(state, rowIndex, n):
        
        if rowIndex < 0 or rowIndex >= n:
            raise IndexError("List index is out of range!")

        row_track = [0] * (n + 1)

        for number in state[rowIndex]:
            if row_track[number] > 0:
                return True
            row_track[number] += 1
        
        return False



    def can_win(self, state):
        pass

        

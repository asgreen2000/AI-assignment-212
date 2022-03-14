class Tents:
    EMPTY = 0
    TREE = 1
    TENT = 2
    def __init__(self, forest, row_const, col_const, size):
        self.forest = forest
        self.row_const = row_const
        self.col_const = col_const
        self.size = size
        self.trees = self.generate_list_tree()

    def accept(self, solver):
        return solver.solve(self)
    
    def generate_list_tree(self):
        self.trees = []

        for row_idx in range(self.size):
            for col_idx in range(self.size):
                number = self.forest[row_idx][col_idx]
                if number == Tents.TREE:
                    self.trees += [[row_idx, col_idx]]
        
        return self.trees

    @staticmethod
    def can_have_tents_at(forest, row_const, col_const ,row_idx, col_idx, size):
        
        
        if row_idx < 0 or row_idx >= size or col_idx < 0 or col_idx >= size:
            return False

        if forest[row_idx][col_idx] != Tents.EMPTY:
            return False
        

        # check constraint
        if row_const[row_idx] <= 0 or col_const[col_idx] <= 0:
            return False

        # check tent in horizontal, vertical direction
        if row_idx > 0 and forest[row_idx - 1][col_idx] == Tents.TENT:
            return False
        if col_idx > 0 and forest[row_idx][col_idx - 1] == Tents.TENT:
            return False
        if row_idx < size - 1 and forest[row_idx + 1][col_idx] == Tents.TENT:
            return False
        if col_idx < size - 1 and forest[row_idx][col_idx + 1] == Tents.TENT:
            return False

        # check diagonally
        if row_idx > 0 and col_idx > 0 and forest[row_idx - 1][col_idx - 1] == Tents.TENT:
            return False
        if row_idx > 0 and col_idx < size - 1 and forest[row_idx - 1][col_idx + 1] == Tents.TENT:
            return False
        
        if row_idx < size - 1 and col_idx > 0 and forest[row_idx + 1][col_idx - 1] == Tents.TENT:
            return False

        
        if row_idx > 0 and row_idx < size - 1 and col_idx < size - 1 and forest[row_idx + 1][col_idx + 1] == Tents.TENT:
            return False

        return True
    

        

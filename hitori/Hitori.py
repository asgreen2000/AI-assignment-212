from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Hitori:
    init_state: List[List[int]]
    n: int

    # receive solver and call solve mmethod
    def accept(self, solver):
        return solver.solve(self.init_state, self.n)

        

from Hitori import *
from SearchAlgo import *
import pathlib
# importing functools for reduce()
import functools

DIR_PATH = str(pathlib.Path(__file__).parent.resolve()) + '\\'


def readFile(fileName):
    scanner = open(fileName,"r")
    lines = scanner.read().splitlines()
    return lines

if __name__ == '__main__':

    """
    Input format:
    n: first line of input, represent size of grid
    Each of the next line describes a row in grid
    """

    fileName = "input.txt"
    input = readFile(DIR_PATH + fileName)
    n = str(input[0][0])
    grid = functools.reduce(lambda res, cur: res + [cur.split(' ')], input[1:], [])
    
    # Hitori game
    hitori = Hitori(grid, n) 
    dfs = DepthFirstSearch()
    a_star = AStarSearch()
    
    # let Hitori call solve method of dfs
    solution = dfs.let_me_solve(hitori)

    print(solution)

    

from re import fullmatch
from turtle import st
from Tents import *
import pathlib
import time
import os
import Util
import functools

DIR_PATH = str(pathlib.Path(__file__).parent.resolve())


class WriteSolution:

    @staticmethod
    def truncate_file(fileName):
        file = open(fileName,"r+")
        file.truncate(0)
        file.close()

    @staticmethod
    def write(data, fileName):
        WriteSolution.truncate_file(fileName)
        f = open(fileName, "w")
        f.write(data)
        f.close()

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
    for x in range(1,31):
        fileName = "input" + str(x) +".txt"
        input = readFile(os.path.join(DIR_PATH, 'input' ,fileName))
        n = int(input[0])

        grid = functools.reduce(lambda res, cur: res + [[int(i) for i in cur.split(' ')]], input[1:], [])
        
        forest = grid[0 : n]

        row_const = grid[n]
        col_const = grid[n + 1]
        
        tents = Tents(forest, row_const, col_const, n)
        start = time.time()
        tents.solve_by_a_star()
        end = time.time()
        steps = tents.generate_steps()
        result=""
        result+="Time: "
        result += str(end - start)
        print(x,end-start)
        result+="\n"
        result+=Util.print_steps(steps)
        out="output"+str(x)+".txt"
        WriteSolution.write(result, os.path.join(DIR_PATH, 'output_astar' ,out))



        # start = time.time()
        # tents.solve_by_dfs()
        # end = time.time()
        # steps = tents.generate_steps()
        # result=""
        # result+="Time: "
        # result += str(end - start)
        # result+="\n"
        # result+=Util.print_steps(steps)
        # out="output"+str(x)+".txt"
        # WriteSolution.write(result, os.path.join(DIR_PATH, 'output_dfs' ,out))


    
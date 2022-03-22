from Kakurasu import *
import pathlib
import time
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
    size = int(input[0][0])

    row_const = [int(number) for number in input[1].split(' ')]
    col_const = [int(number) for number in input[2].split(' ')]

    kakurasu = Kakurasu(row_const, col_const, size)

    kakurasu.solve_by_a_star()
    
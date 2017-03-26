import sys


def get_ijk(index):
    """
    :param index: the CNF variable (positive base 8 number)
    :return: i,j,k
    i: row number (0-8) of the sudoku
    j: column number (0-8) of the sudoku
    k: the number (1-9) of the cell (i,j)
    """
    index -= 1
    i = index / 81
    index -= (81 * i)
    j = index / 9
    index -= (9 * j)
    k = index + 1
    return i, j, k


def construct_grid(sat):
    """
    :param sat: a list of the variables in the sat solution
    :return: a filled 9x9 array with the sudoku solution
    """
    cursor = 0
    sol = [[0 for _ in range(9)] for _ in range(9)]
    while sat[cursor] != '0':
        index = int(sat[cursor])
        if index > 0:
            i, j, k = get_ijk(index)
            sol[i][j] = k
        cursor += 1
    return sol


def print_sol_basic(sol):
    """
    :param sol: a filled 9x9 array with the sudoku solution
    Prints the solution with columns separated by 2 spaces
    """
    print('\n'.join([''.join(['{:3}'.format(num) for num in row])
                     for row in sol]))


def main():
    std_in = sys.stdin.read().replace('\n', ' ').split()
    solvable = std_in.pop(0) == "SAT"
    if solvable:
        sol = construct_grid(std_in)
        print_sol_basic(sol)
    else:
        print("UNSOLVABLE SUDOKU")


if __name__ == "__main__":
    main()

import sys, getopt


def main():
    inputfile = get_input_file()
    ent = read(inputfile)
    done = construct_grid(ent)
    print_sol_basic(done)


def get_input_file():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:v', ["help", "input="])
    except getopt.GetoptError:
        print 'sat2sud -i <inputfile>'
        sys.exit(2)
    if not opts:
        print 'sat2sud -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'sat2sud -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--input"):
            return arg


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
    print('\n'.join([''.join(['{:3}'.format(num) for num in row]) for row in sol]))


def read(filename):
    try:
        with open(filename) as f:
            sol = f.read()
    except Exception as error:
        print(error)
        sys.exit(1)
    final = sol.split()
    return final[1:]


if __name__ == "__main__":
    main()

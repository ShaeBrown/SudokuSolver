import sys, getopt

def get_index(i, j, k):
    """
    :param i: row number (0-8) of the sudoku
    :param j: column number (0-8) of the sudoku
    :param k: the number (0-8) of the cell (i,j)
    :return: the index (positive base 8 number)
    """
    return (81 * i) + (9 * j) + k + 1


def filled_cells(clauses, sud):
    """
    Reads the sudoku grid input and appends a clause for each filled cell
    (i, j, k) -> true
    :param clauses: the list of clauses in CNF
    """
    index = 0
    for k in sud:
        if k == '\n':
            continue
        if k not in ['0', '.', '*', '?']:
            i = index / 9
            j = index % 9
            ijk = get_index(i, j, int(k) - 1)
            clauses.append(str(ijk))
        index += 1


def cells(clauses):
    """
    Appends clauses requiring that each cell contains at least one number
    :param clauses: the list of clauses in CNF
    """
    for i in range(0, 9):
        for j in range(0, 9):
            clause = []
            for k in range(0, 9):
                clause.append(str(get_index(i, j, k)))
            clauses.append(" ".join(clause))


def rows(clauses):
    """
    Appends clauses requiring that a number appears at most once in every row
    :param clauses:
    """
    for i in range(0, 9):
        for k in range(0, 9):
            for j in range(0, 8):
                for l in range(j + 1, 9):
                    clauses.append("-%d -%d" % (get_index(i, j, k), get_index(i, l, k)))


def columns(clauses):
    """
    Appends clauses requiring that a number appears at most once in every column
    :param clauses: the list of clauses in CNF
    """
    for j in range(0, 9):
        for k in range(0, 9):
            for i in range(0, 8):
                for l in range(i + 1, 9):
                    clauses.append("-%d -%d" % (get_index(i, j, k), get_index(l, j, k)))


def sub_grid(clauses):
    """
    Appends clauses requiring that a number appears at most once in every sub-grid
    :param clauses: the list of clauses in CNF
    """
    for k in range(0, 9):
        for a in range(0, 3):
            for b in range(0, 3):
                for u in range(0, 3):
                    for v in range(0, 2):
                        for w in range(v + 1, 3):
                            i = 3 * a + u
                            j1 = 3 * b + v
                            j2 = 3 * b + w
                            clauses.append("-%d -%d" % (get_index(i, j1, k), get_index(i, j2, k)))
    for k in range(0, 9):
        for a in range(0, 3):
            for b in range(0, 3):
                for u in range(0, 2):
                    for v in range(0, 3):
                        for w in range(u + 1, 3):
                            for t in range(0, 3):
                                i1 = 3 * a + u
                                i2 = 3 * a + w
                                j1 = 3 * b + v
                                j2 = 3 * b + t
                                clauses.append("-%d -%d" % (get_index(i1, j1, k), get_index(i2, j2, k)))


def get_input_file():
    filename = ""
    GSAT = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:v', ["help", "input=", "gsat"])
    except getopt.GetoptError as e:
        print(e)
        print 'sud2sat -i <inputfile>'
        sys.exit(2)
    if not opts:
        print 'sud2sat -i <inputfile>'
        sys.exit(2)
    print(opts)
    for opt, arg in opts:
        if opt == '-h':
            print 'sud2sat -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--input"):
            filename = arg
        elif opt == "--gsat":
            GSAT = True
    return filename, GSAT


def read(filename):
    try:
        with open(filename) as f:
            sud = f.read()
    except Exception as error:
        print(error)
        sys.exit(1)
    return list(sud)


def print_CNF(clauses):
    num_clauses = len(clauses)
    num_variables = get_index(8, 8, 8)
    print("p cnf %d %d" % (num_variables, num_clauses))
    for clause in clauses:
        print(clause + " 0")


def print_GSAT(clauses):
    for clause in clauses:
        print("(" + clause + ")")


def main():
    clauses = []
    inputfile, GSAT = get_input_file();
    sud = read(inputfile);
    filled_cells(clauses, sud)
    cells(clauses)
    rows(clauses)
    columns(clauses)
    sub_grid(clauses)
    if GSAT:
        print_GSAT(clauses)
    else:
        print_CNF(clauses)


if __name__ == "__main__":
    main()

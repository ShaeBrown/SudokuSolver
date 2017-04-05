# SudokuSolver

## sud2sat
Input to sud2sat must be provided by a file.\
`python sud2sat.py -i <inputfile>`\
To output the results to another file:\
`python sud2sat.py -i <inputfile> > <outputfile>`\
To output the results in GSAT format.\
`python sud2sat.py -i <inputfile> --gsat`

## sat2sud
Input to sud2sat must be provided by a file.\
`python sat2sud.py -i <inputfile>`\
To output the results to another file:\
`python sat2sud.py -i <inputfile> > <outputfile>`

## solve.sh
Create a folder named /test\
Edit num_files variable in solve.sh to the number of tests\
Have test files named 01.txt, 02.txt .. num_files.txt (max 99)\
Make sure solve.sh has executable privledges\
Run `./solve.sh`

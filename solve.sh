#!/bin/bash
#Test files named 01.txt, 02.txt .. num_files.txt in folder named test
#Produces a report in sol.txt
num_files=95
time_sum=0
TIME=0
mkdir cnf
mkdir cnfsol
for i in $(seq -f "%02g" 1 ${num_files})
do
   input="./test/${i}.txt"
   out="./cnf/cnf${i}.txt"
   python sud2sat.py -i ${input} > ${out}
done
for i in $(seq -f "%02g" 1 ${num_files})
do
   input="./cnf/cnf${i}.txt"
   out="./cnfsol/cnfsol${i}.txt"
   TIME=$(minisat -verb=2 ${input} ${out} | grep -o [0-9+]\.[0-9+]* | tail -1 | bc -l)
   time_sum=`echo "$time_sum + $TIME" | bc`
   printf "${i}\n" >> sol.txt
   printf "Time: ${TIME}s\n" >> sol.txt
   python sat2sud.py -i ${out} >> sol.txt
   printf "\n\n" >> sol.txt
done
echo "TOTAL TIME: ${time_sum}s" >> sol.txt
rm -r cnf
rm -r cnfsol

Haven't done any stats yet

Algorithms can go in _sorts but probably easier to create more files that create seperate csv's and just merge the csv's so running can be done in parts.

number of runs N and number of elements in the unsorted array ARRAY_SIZE are defined in parameters.txt and that are read in the _sorts

time is recorded in milliseconds 

For gathering the data:
install node.js, java runtime environment, g++ compiler, and python with pandas, numpy, scipy, statsmodels, and matplotlib
    to get python_data.csv run "python python_sorts.py"

    to get c_data.csv compile with "g++ -O3 sorts.cpp" and get either a.out on linux or a.exe on windows. Then run the executable with "./a.out" on linux and just "a.exe" on windows

    to get java_sorts.csv run "javac Main.java" and get Main.class, then run the java with "java Main.java" to get the csv

    to get javascript_data.csv run "node javascript_data.csv"

    then put all the csv files in a folder named data
Then run "python stats.py" to generate the png figures and print the Tukey test and summary statistics.
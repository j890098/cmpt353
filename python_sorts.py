import os
import os.path
import json
import numpy as np
import pandas as pd
import time
from python_implementations import all_implementations

path = "parameters.txt"

# Data to be written
class Params:
    def __init__(self, N, ARRAY_SIZE):
        if(isinstance(N, str)):
            N=int(N)
        if(isinstance(ARRAY_SIZE, str)):
            ARRAY_SIZE=int(ARRAY_SIZE)
        self.N = N
        self.ARRAY_SIZE = ARRAY_SIZE 
    def __str__(self):
        return f"Params(N={self.N},ARRAY_SIZE={self.ARRAY_SIZE})"
        


if(os.path.isfile(path) and os.path.getsize(path)>2):

    # Reading from txt file
    f = open(path, "r")
    data = f.read().split(' ')
    print("reading params")
    
    params = Params(data[0],data[1])
    f.close
    print(params)
else: 
    # no params file make a new one
    params = Params(200,500000)
    print("empty file, adding placeholder",params)
    
    # Writing to params.txt
    f = open(path, "w")
    f.write(str(params.N)+" "+str(params.ARRAY_SIZE))
    f.close()


results = pd.DataFrame()
for i in range(params.N):
    currentRun=[]
    randomArr = np.random.randint(2147483647, size=params.ARRAY_SIZE)
    for sort in all_implementations:
        st = time.time() * 1000
        res = sort(randomArr)
        en = time.time() * 1000
        currentRun.append(en-st)
    results=pd.concat([results,pd.DataFrame([currentRun],
                      columns=["python_builtin","numpyBuiltin","implementedQuicksort"])],
                      ignore_index=False, axis=0)
results.to_csv('python_data.csv', index=False)





    

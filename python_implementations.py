import numpy as np


def numpyBuiltin(arr):
    return np.sort(arr, kind='quicksort')
def pythonBuiltin(arr):
    return arr.sort()



all_implementations = [pythonBuiltin, numpyBuiltin]
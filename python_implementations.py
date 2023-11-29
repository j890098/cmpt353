import random
import numpy as np


def numpyBuiltin(arr):
    return np.sort(arr, kind='quicksort')
def pythonBuiltin(arr):
    return arr.sort()

def quicksort(arr):
    return quicksortAux(arr,0,arr.size-1)

def quicksortAux(arr,start,end):
    i = start
    j = end
    if(end>start):
        pivotIndex = random.randint(start, end)
        pivot = arr[pivotIndex]
        
        while (i<end or j>start):
            while (arr[i] < pivot and i+1 < end):
                i+=1
            while (arr[j] > pivot and j-1 > start):
                j-=1

            if (i <= j) :
                swap(arr, i, j)
                i+=1
                j-=1
            
            else :
                if (i < end):
                    quicksortAux(arr, i, end)
                if (j > start):
                    quicksortAux(arr, start, j)
                return arr
            
    
    return arr
    
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


all_implementations = [pythonBuiltin, numpyBuiltin, quicksort]
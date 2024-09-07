
#quicksort algorithm 

import numpy as np

inputfilename = 'quicksortAlgorithm\output.txt'
outpufilename = 'quicksortAlgorithm\sortedoutput.txt'

array = np.loadtxt(str(inputfilename), dtype = int)

def quicksort (array):
    if len (array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

sorted_array = quicksort(array)
np.savetxt(str(outpufilename), sorted_array, fmt='%d')

print(f'\n >> Array sorted - saved @ {outpufilename}')

#quicksort algorithm 

import numpy as np

filename = "quicksortAlgorithm\output.txt"
array = np.loadtxt('quicksortAlgorithm\output.txt', dtype=int)

def quicksort (array):
    if len (array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

sorted_array = quicksort(array)
np.savetxt('quicksortAlgorithm\sortedoutput.txt', array, fmt='%d')

print(f'Sorted array:{sorted_array}')
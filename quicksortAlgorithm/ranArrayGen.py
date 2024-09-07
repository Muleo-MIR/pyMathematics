
#list generator

import numpy as np

outputfilename = 'quicksortAlgorithm\output.txt'

lowerBound,upperBound,n = map(int,input('\n >> Input lower bound, upper bound and number of elements in list: ').split())

array = (np.random.randint(low = lowerBound,high = upperBound,size = n))
np.savetxt(str(outputfilename), array, fmt='%d')

print(f'\n >> Array generated - saved @ {outputfilename}')
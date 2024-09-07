
#list generator

import numpy as np
import os

filename = "quicksortAlgorithm\output.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)
f = open(filename, "w") 

lowerBound,upperBound,n = map(int,input('Input lower bound, upper bound and number of elements in list: ').split())

print(list(np.random.randint(low = lowerBound,high = upperBound,size = n)),file = f)
f.close()
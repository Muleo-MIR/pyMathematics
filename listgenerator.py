
#list generator

import numpy as np

lowerBound,upperBound,n = map(int,input('Input lower bound, upper bound and number of elements in list: ').split())

print(list(np.random.randint(low = lowerBound,high = upperBound,size = n)))
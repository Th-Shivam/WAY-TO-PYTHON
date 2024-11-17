import numpy as np  
from scipy import stats
x = [17,10,9,14,13,17,12,20,14]
mean = np.mean(x)
print(mean)
median = np.median(x)
print(median)
mode = stats.mode(x)
print(mode)

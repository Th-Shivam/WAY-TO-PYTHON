import matplotlib.pyplot as plt
import numpy as np

# Correct initialization of arrays
y = np.array([5, 15, 17, 45, 36, 7, 98, 56])

# Plotting the histogram with 20 bins
plt.hist(y, bins=20)

# Display the plot
plt.show()
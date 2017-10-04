def plot_data_normal_graph(data):
	mean = np.mean(data)
	variance = np.var(data)
	sigma = math.sqrt(variance)
	x = np.linspace(mean - (3 * variance), mean + (3 * variance), 100)
	return x, mean, sigma

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

data = np.array([
    [9,2,5,8],
    [6,1,3,2],
    [8,4,6,8],
    [7,1,2,6],
    [10,5,6,9],
    [6,2,4,7]
])

x, mean, sigma = plot_data_normal_graph(data)

plt.plot(x, mlab.normpdf(x, mean, sigma))
plt.show()
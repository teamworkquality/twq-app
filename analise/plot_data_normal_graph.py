import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

def plot_data_normal_graph(data):
	data = data.T
	mean = np.mean(data)
	variance = np.var(data)
	sigma = math.sqrt(variance)
	x = np.linspace(mean - (3 * variance), mean + (3 * variance), 100)
	return x, mean, sigma

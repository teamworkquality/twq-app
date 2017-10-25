import numpy as np
from scipy.stats import rankdata

def spearman(data):
	ranked_data = np.array([
		rankdata([((ai - np.max(a)) * -1) for ai in a])
		for a in data.T
	]).T
	return pearson(ranked_data)

def pearson(data):
	data = data.T
	return np.array([[correlation_xy(x,y) for y in data] for x in data])

def correlation_xy(x,y):
	mean_x = np.mean(x)
	std_x = (np.sum([(xi - mean_x) ** 2 for xi in x]) / (len(x) - 1)) ** (1/2)
	mean_y = np.mean(y)
	std_y = (np.sum([(yi - mean_y) ** 2 for yi in y]) / (len(y) - 1)) ** (1/2)

	return np.cov(x,y)[0][1] / (std_x * std_y)

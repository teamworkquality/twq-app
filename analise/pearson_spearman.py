def spearman(data):
	ranked_data = np.array([
		rankdata([((ai - np.max(a)) * -1) for ai in a])
		for a in data.T
	]).T
	return pearson(ranked_data)

def pearson(data):
	return np.array([[correlation_xy(x,y) for y in data] for x in data])

def correlation_xy(x,y):
	mean_x = np.mean(x)
	std_x = (np.sum([(xi - mean_x) ** 2 for xi in x]) / (len(x) - 1)) ** (1/2)
	mean_y = np.mean(y)
	std_y = (np.sum([(yi - mean_y) ** 2 for yi in y]) / (len(y) - 1)) ** (1/2)

	return np.cov(x,y)[0][1] / (std_x * std_y)

import numpy as np
from scipy.stats import rankdata

# data:
#   number of elements in data = number of people answering the quiz
#   number of elements in each data element = number of questions in the quiz

#   [9,2,5,8]:      answers for person 1
#   [9,6,8,7,10,6]: answers for construct 1

data = np.array([
    [9,2,5,8],
    [6,1,3,2],
    [8,4,6,8],
    [7,1,2,6],
    [10,5,6,9],
    [6,2,4,7]
])

print("Pearson:")
print(pearson(data))
print("")
print("Spearman:")
print(spearman(data))
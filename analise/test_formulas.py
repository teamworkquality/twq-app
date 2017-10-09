import numpy as np
from scipy.stats import rankdata
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math

import icc
import pearson_spearman as ps
import shapiro_wilk as sw
import plot_data_normal_graph as pdng

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

# icc's:
# 	icc(2,1):
print("ICC(2,1) = " + str(icc.icc2_1(data)))
# 	icc(2,k):
print("ICC(2,k) = " + str(icc.icc2_k(data)))
# 	icc(3,1):
print("ICC(3,1) = " + str(icc.icc3_1(data)))
# 	icc(3,k):
print("ICC(3,k) = " + str(icc.icc3_k(data)))

print("")

# Pearson correlation:
print("Pearson correlation:")
print(ps.pearson(data))

print("")

# Spearman correlation:
print("Spearman correlation:")
print(ps.spearman(data))

print("")

# Shapiro-Wilk test:
print("Shapiro-wilk test:")
w, p_value = sw.shapiro_wilk(data)
# 	w:
print("w       = " + str(w))
# 	p_value:
print("p_value = " + str(p_value))

print("")

# Plot normal data graph:
print("Plot normal data graph:")
x, mean, sigma = pdng.plot_data_normal_graph(data)
plt.plot(x, mlab.normpdf(x, mean, sigma))
plt.show()
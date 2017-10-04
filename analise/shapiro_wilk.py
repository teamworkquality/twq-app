def shapiro_wilk(data):
	data = data.T
	w, p_value = stats.shapiro(data)
	return w, p_value

import numpy as np
from scipy import stats

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

w, p_value = shapiro_wilk(data)

print("w       = " + str(w))
print("p_value = " + str(p_value))
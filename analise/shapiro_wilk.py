import numpy as np
from scipy import stats

def shapiro_wilk(data):
	data = data.T
	w, p_value = stats.shapiro(data)
	return w, p_value

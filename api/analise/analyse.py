import numpy as np
from scipy.stats import rankdata
from scipy import stats

### ICC BEGIN
def icc(data, icc_type):
    Y = data

    # n: number of people answering the quiz
    # k: number of constructs in the quiz
    [n, k] = Y.shape

    # Degrees of Freedom
    dfb = n - 1
    dfj = k - 1
    dfe = (n - 1) * (k - 1)

    # Sum Square Total
    mean_Y = np.mean(Y)
    SST = ((Y - mean_Y) ** 2).sum()

    # create the design matrix for the different levels
    x = np.kron(np.eye(k), np.ones((n, 1)))  # sessions
    x0 = np.tile(np.eye(n), (k, 1))  # subjects
    X = np.hstack([x, x0])

    # Sum Square Error
    predicted_Y = np.dot(np.dot(np.dot(X, np.linalg.pinv(np.dot(X.T, X))), X.T), Y.flatten('F'))
    residuals = Y.flatten('F') - predicted_Y
    SSE = (residuals ** 2).sum()
    EMS = SSE / dfe

    # Sum square column effect - between colums
    SSC = ((np.mean(Y, 0) - mean_Y) ** 2).sum() * n
    JMS = SSC / dfj

    # Sum Square subject effect - between rows/subjects
    SSR = SST - SSC - SSE
    BMS = SSR / dfb

    ICC = -1

    if icc_type == 'icc2_1':
        # ICC(2,1) = (mean square subject - mean square error) /
        # (mean square subject + (k-1)*mean square error +
        # k*(mean square columns - mean square error)/n)
        ICC = (BMS - EMS) / (BMS + (k-1) * EMS + k * (JMS - EMS) / n)

    elif icc_type == "icc2_k":
        # ICC(2,k) = (mean square subject - mean square error) /
        # (mean square subject + (mean square columns - mean square error)/n))
        ICC = (BMS - EMS) / (BMS + ((JMS + EMS) / n))

    elif icc_type == 'icc3_1':
        # ICC(3,1) = (mean square subject - mean square error) /
        # (mean square subject + (k-1) * mean square error)
        ICC = (BMS - EMS) / (BMS + (k-1) * EMS)

    elif icc_type == 'icc3_k':
        # ICC(3,k) = (mean square subject - mean square error) /
        # mean square subject
        ICC = (BMS - EMS) / BMS

    return ICC

def icc2_1(data): return icc(data, 'icc2_1')
def icc2_k(data): return icc(data, 'icc2_k')
def icc3_1(data): return icc(data, 'icc3_1')
def icc3_k(data): return icc(data, 'icc3_k')
### ICC END

### SPEARMAN AND PEARSON BEGIN
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
### SPEARMAN AND PEARSON END

### SHAPIRO BEGIN
def shapiro_wilk(data):
    data = data.T
    w, p_value = stats.shapiro(data)
    return w, p_value
### SHAPIRO END

### CRONBACK BEGIN
def cronbach(data):
    itemvars = data.var(axis=1, ddof=1) # ddof=1 means /N-1, ddof=0 means /N
    tscores = data.sum(axis=0) #sum per judge
    nitems = len(data) # qtd of form itens
    return nitems / (nitems-1.) * (1 - itemvars.sum() / tscores.var(ddof=1))
### CRONBACK END

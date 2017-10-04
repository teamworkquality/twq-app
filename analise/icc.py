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

import numpy as np

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

print("ICC(2,1) = " + str(icc2_1(data))) # aprox. 0.29
print("ICC(2,k) = " + str(icc2_k(data))) # aprox. 0.62
print("ICC(3,1) = " + str(icc3_1(data))) # aprox. 0.71
print("ICC(3,k) = " + str(icc3_k(data))) # aprox. 0.91
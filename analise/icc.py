def icc(data, icc_type):
    ''' Calculate intraclass correlation coefficient for data within
        Brain_Data class

    ICC Formulas are based on:
    Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: uses in
    assessing rater reliability. Psychological bulletin, 86(2), 420.

    icc1:  x_ij = mu + beta_j + w_ij
    icc2/3:  x_ij = mu + alpha_i + beta_j + (ab)_ij + epsilon_ij

    Code modifed from nipype algorithms.icc
    https://github.com/nipy/nipype/blob/master/nipype/algorithms/icc.py

    Args:
        icc_type: type of icc to calculate (icc: voxel random effect,
                icc2: voxel and column random effect, icc3: voxel and
                column fixed effect)

    Returns:
        ICC: intraclass correlation coefficient
    '''

    # n: number of targets
    # k: number of judges

    Y = data
    [n, k] = Y.shape

    # Degrees of Freedom
    dfb = n - 1
    dfw = n * (k - 1)
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
    predicted_Y = np.dot(np.dot(np.dot(X, np.linalg.pinv(np.dot(X.T, X))),
                         X.T), Y.flatten('F'))
    residuals = Y.flatten('F') - predicted_Y
    SSE = (residuals ** 2).sum()
    EMS = SSE / dfe

    # Sum square column effect - between colums
    SSC = ((np.mean(Y, 0) - mean_Y) ** 2).sum() * n
    JMS = SSC / dfj

    # Sum Square subject effect - between rows/subjects
    SSR = SST - SSC - SSE
    BMS = SSR / dfb

    # SSW = ((Y - np.mean(Y, 0)) ** 2).sum()
    # print((Y - np.mean(Y, 0)) ** 2)
    # WMS = SSW / dfw

    # print("SST = " + str(SST))
    # print("SSE = " + str(SSE))
    # print("SSC = " + str(SSC))
    # print("SSR = " + str(SSR))
    # print("SSW = " + str(SSW))
    
    ICC = -1

    if icc_type == 'icc1':
        # Not implemented yet
        # ICC = (BMS - WMS) / (BMS + (k-1) * WMS)
        ICC = -1

    elif icc_type == 'icc2_1':
        # ICC(2,1) = (mean square subject - mean square error) /
        # (mean square subject + (k-1)*mean square error +
        # k*(mean square columns - mean square error)/n)
        ICC = (BMS - EMS) / (BMS + (k-1) * EMS + k * (JMS - EMS) / n)

    elif icc_type == 'icc3_1':
        # ICC(3,1) = (mean square subject - mean square error) /
        # (mean square subject + (k-1)*mean square error)
        ICC = (BMS - EMS) / (BMS + (k-1) * EMS)

    elif icc_type == 'icc3_k':
        # ICC(3,1) = (mean square subject - mean square error) /
        # mean square subject
        ICC = (BMS - EMS) / BMS

    return ICC

import numpy as np

data = np.array([
    [9,2,5,8],
    [6,1,3,2],
    [8,4,6,8],
    [7,1,2,6],
    [10,5,6,9],
    [6,2,4,7]
])

# print("ICC(1,1): " + str(icc(data,'icc1'))) # aprox. 0.17
print("ICC(2,1): " + str(icc(data,'icc2_1'))) # aprox. 0.29
print("ICC(3,1): " + str(icc(data,'icc3_1'))) # aprox. 0.71
print("ICC(3,k): " + str(icc(data,'icc3_k'))) # aprox. 0.71
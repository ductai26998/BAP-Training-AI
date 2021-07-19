import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def initial_data(N: int = 1000, D: int = 2, K: int = 3, data_name: str = 'data.png'):
    """
    Initial data for train, test and validate
    Parameters:
        N: int: The sample numbers
        D: int: The feature numbers of input
        K: int: the numbers of output
        data_name: str: The data name
    """
    X = np.zeros((N * K, D))  # data matrix (each row = single example)
    y = np.zeros(N * K, dtype='int8')  # class labels
    for j in range(K):
        ix = range(N * j, N * (j + 1))
        r = np.linspace(0.0, 1, N)  # radius
        t = np.linspace(j * 4, (j + 1) * 4, N) + np.random.randn(N) * 0.2  # theta
        X[ix] = np.c_[r * np.sin(t), r * np.cos(t)]
        y[ix] = j

    # lets visualize the data:
    fig = plt.figure(1)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
    plt.show()
    # fig.savefig(data_name)
    return X, y

def remap(y, K):
    m = len(y)
    out = np.zeros((m, K))
    for index in range(m):
        out[index][y[index]] = 1
    return out

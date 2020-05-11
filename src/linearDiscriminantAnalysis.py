"""
    this is an illustration of LDA
    @author: dataByte

"""

import numpy as np
import matplotlib.pyplot as plt


"""
    step by step process of LDA

"""


c1 = np.array([
    [4, 1],
    [2, 4],
    [2, 3],
    [3, 6],
    [4, 4]
])

c2 = np.array([
    [9, 10],
    [6, 8],
    [9, 5],
    [8, 7],
    [10, 8]
])

plt.style.use('seaborn-whitegrid')
plt.figure(figsize= (8, 8))
plt.scatter(c1[:, 0], c1[:, 1], color="r", label='class 1')
plt.scatter(c2[:, 0], c2[:, 1], color="b", label='class 2')
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.legend()
plt.show()


# step1: compute within class scatter matrix || sw = s1 + s2 [ s1 and s2 are the respective scatter matrices ]

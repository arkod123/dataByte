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
"""
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(8, 8))
plt.scatter(c1[:, 0], c1[:, 1], color="r", label='class 1')
plt.scatter(c2[:, 0], c2[:, 1], color="b", label='class 2')
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.legend()
plt.show()
"""

# step1: compute within class scatter matrix || sw = s1 + s2 [ s1 and s2 are the respective scatter matrices ]
## calculate the mean of respective class
mu_c1_x = np.mean(c1[:, 0])
mu_c1_y = np.mean(c1[:, 1])
mu_c2_x = np.mean(c2[:, 0])
mu_c2_y = np.mean(c2[:, 1])


## calculate respective (x1 - mu) and (y1 - mu) of respective classes
def meanCalc(matrix, class_mu):
    new_matrix = np.empty(matrix.shape)
    for i in range(0, matrix.shape[0]):
        new_matrix[i, 0] = matrix[i][0] - class_mu[0]
        new_matrix[i, 1] = matrix[i][1] - class_mu[1]
    return new_matrix


c1_new = meanCalc(c1, np.array([mu_c1_x, mu_c1_y]))
c2_new = meanCalc(c2, np.array([mu_c2_x, mu_c2_y]))

## function for within class scatter matrix calc
def withinClassScatterMatrix(matrix):
    """
    calculate within class scatter matrix
    formula: Sw = sum((x - mu).(x - mu)^T)
    """
    data_SW = []
    for i in range(0, matrix.shape[0]):
        a = np.array([
            [matrix[i][0]],
            [matrix[i][1]]
        ])
        data_SW.append(np.dot(a, a.T))
    SW = (np.sum(data_SW, axis=0)) / matrix.shape[0]
    return SW


## calculate sw
s1 = withinClassScatterMatrix(c1_new)
s2 = withinClassScatterMatrix(c2_new)
# since i have 2 classes here therefore the final scatter matrix will be addition of individual scatter matrix
sw = np.add(s1, s2)


# step2: compute between class scatter matrix
## function for between class scatter matrix
# formula:  SB = ( class1_mu - class2_mu ).(class1_mu - class2_mu)^T
def betweenClassScatterMatrix(class1_mu, class2_mu):
    a = np.array([
        [np.subtract(class1_mu, class2_mu)[0]],
        [np.subtract(class1_mu, class2_mu)[1]]
    ])
    return np.dot(a, a.T)

mean_values_c1 = np.array([mu_c1_x, mu_c1_y])
mean_values_c2 = np.array([mu_c2_x, mu_c2_y])

sb = betweenClassScatterMatrix(mean_values_c1, mean_values_c2)

# step3: Compute the Eigenvalues and Eigenvectors of sw^-1 sb
eigval, eigvec = np.linalg.eig(np.dot(np.linalg.inv(sw),sb))

# Select the largest eigenvalues
eigen_pairs = [[np.abs(eigval[i]), eigvec[:, i]] for i in range(len(eigval))]
eigen_pairs = sorted(eigen_pairs, key=lambda k: k[0], reverse=True)
print(eigen_pairs)
# let the project vector v, which has the highest eigen value
v = eigen_pairs[0][1]

print(np.dot(c1, v))
print(np.dot(c2, v))


# projection plot
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(8, 8))
plt.scatter(c1[:, 0], c1[:, 1], color="r", label='class 1')
plt.scatter(c2[:, 0], c2[:, 1], color="b", label='class 2')
plt.plot(np.linspace(0, 12), np.linspace(0, 12)*(v[1]/v[0]), color='black', linestyle='--', linewidth=1.5)

plt.xlim(0, 12)
plt.ylim(0, 12)
plt.legend()
plt.show()
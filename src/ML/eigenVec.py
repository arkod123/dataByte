"""
    illustration of eigen vectors and eigen values
    @author: dataByte


"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la

"""
### example 1
# main vector
v = np.array([[2], [1]])

# define matrix
A = np.array([
    [-1, 3],
    [2, -2]
])
# transformed vector
Av = A.dot(v)
# plot
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(8, 8))
origin = [0, 0], [0, 0]
plt.quiver(*origin, v[0], v[1], color=['r'], scale=5)
plt.quiver(*origin, Av[0], Av[1], color=['g'], scale=5)
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.show()
"""

### example 2
A = np.array([[5, 1],
              [3, 3]])

# let the transform equation be : v = A.v
v = np.array([
    [1],
    [2]
])
# lets get the eigen vectors
eig_val, eig_vec = la.eig(A)
# first eigen vector
eig_vec_1 = np.array([
    [eig_vec.T[0][0]],
    [eig_vec.T[0][1]]
])

# transformed matrix
Av = np.dot(A, v)
Av1 = np.dot(A, eig_vec_1)

print("matrix --> ", A.flatten(), "\n"
      "vector --> ", v.flatten(), "\n"
      "dot product (A.V) --> ", Av.flatten(), "\n"
      "eigen_vector --> ", eig_vec_1.flatten(), "\n"
      "new dot product (A. eigVec) -->", Av1.flatten(), "\n")

# visualization

def plotVec(vec, cols, scale=1, alpha = 1):
    x = np.concatenate([[0, 0], vec.flatten()])
    plt.quiver([x[0]],
               [x[1]],
               [x[2]],
               [x[3]], angles='xy', scale_units='xy', scale=scale, color=cols, alpha=alpha)

plt.style.use('seaborn-whitegrid')
plt.figure()
plt.axvline(x=0, color="#FF9C33", zorder=0)
plt.axhline(y=0, color='#FF9C33', zorder=0)

# plot the first vector
plotVec(v, 'r')
plotVec(Av, 'g', scale=3)
plotVec(eig_vec_1, 'b')
plotVec(Av1, 'y', scale=3)
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.show()




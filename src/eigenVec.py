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
A = np.array([[5, 1], [3, 3]])

# let the transform equation be : v = A.v
v = np.array([
    [0.70710678],
    [ 0.70710678]
])

Av = np.dot(A, v)

print(Av)
# plot
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(8, 8))
origin = [0, 0], [0, 0]
plt.quiver(*origin, v[0], v[1], color=['r'], scale=11)
plt.quiver(*origin, Av[0], Av[1], color=['g'], scale=11)
plt.xlim(-1,9)
plt.ylim(-1, 9)
plt.show()






















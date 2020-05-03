"""
    Illustration of linear transformation and eigenVectors
    @author: dataByte | LC02
"""


## import Libraries
import numpy as np
import matplotlib.pyplot as plt


### --> Example 1
"""
    T(A . v1) = v2 
    visualize in 3d plot
"""
# define the vector A
A = np.array([[2, 1],
              [1, 1]
             ])
# define the factor vector v1
v1 = np.array([2, 3])
# final product
v2 = np.dot(A, v1)

# plot
"""
x, y = A.T
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(8,8))
plt.scatter(x, y)
x1, y1 = v2.T
plt.scatter(x1, y1)
plt.show()
"""
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10, 10))
origin = [0], [0]
x, y = A.T
plt.scatter(x, y, s=250)
plt.quiver(*origin, A[:, 0], A[:, 1], color=['r', 'g'], scale=5)
x1, y1 = v2.T
plt.scatter(x1, y1, s=250)
plt.quiver(*origin, v2[0], v2[1], color='b', scale=8)
plt.xlim(-0.5, 8)
plt.ylim(-0.5, 8)
plt.show()

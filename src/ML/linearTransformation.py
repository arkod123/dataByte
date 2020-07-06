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

# define the vector A
A = np.array([[2, 1],
              [1, 1]
             ])
# define the factor vector v1
v1 = np.array([2, 3])
# final product
v2 = np.dot(A, v1)

# plot
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(10, 10))
origin = [0, 0], [0, 0]
print(origin)
print(A[:, 0])
x, y = A.T
plt.scatter(x, y, s=250)
plt.quiver(*origin, A[:, 0], A[:, 1], color=['r', 'g'], scale=5)
x1, y1 = v2.T
plt.scatter(x1, y1, s=250)
plt.quiver(*origin, v2[0], v2[1], color='b', scale=8)
plt.xlim(-0.5, 8)
plt.ylim(-0.5, 8)
plt.show()
"""


### --> Example 2

def transform(vecs):
    transform_array = np.empty((0, vecs.shape[1]), float)
    for elem in vecs:
        x, y = elem[0], elem[1]
        res = np.array([[(2*x + y),
                         (x + y)]])
        transform_array = np.append(transform_array, res, axis=0)
    return transform_array

### defining vector
u = np.array([[1, 0]])
v = np.array([[0, 2]])
vecs = np.concatenate((u, v))
v2 = transform(vecs)

origin = [0, 0], [0, 0]
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(8, 8))
plt.quiver(*origin, vecs[:, 0], vecs[:, 1], color=['r', 'g'], scale=5)
plt.quiver(*origin, v2[:, 0], v2[:, 1], color=['r', 'g'], linestyle='dashed', scale=5)
plt.ylim(-1, 4)
plt.xlim(-1, 4)
plt.show()




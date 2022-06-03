import numpy as np
A = np.array([[1,2,3,4,5],
              [2,1,2,3,4],
              [3,2,1,2,3],
              [4,3,2,1,2],
              [5,4,3,2,1]])
b = np.array([7,-1,-3,5,17])
print(np.dot(np.linalg.inv(A),b))

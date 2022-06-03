import numpy as np
B = np.array([np.arange(4)+1,
              np.arange(4)+12,
              np.arange(4)+25,
              np.arange(4)+100])
print(B.transpose())

D = np.arange(11,52,10)
diagonal = np.diag(D)
print(diagonal)

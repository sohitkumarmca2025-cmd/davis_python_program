import numpy as np

arr = np.array([10, 20, 30])

print((arr - arr.min()) / (arr.max() - arr.min()))

# Output:
# [0.  0.5 1. ]

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

arr[arr % 2 != 0] = -1

print(arr)

# Output:
# [-1  2 -1  4 -1]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import myteta

# Create python function that calculates angle between 2 vectors in degrees
# (use numpy functions to implement the function).
a = np.array([1, 0, 0])
b = np.array([0, 1, 0])
print(f'teta(a & b) = {myteta.angle_teta180(a, b)}')
c = np.array([1, 2, 3])
d = np.array([3, 2, 1])
print(f'teta(c & d) = {myteta.angle_teta180(c, d)}')
f = np.array([1, 0.36, 0])
g = np.array([-1, 0, 0])
print(f'teta(f & g) = {myteta.angle_teta180(f, g)}')

# To visualize vectors in 2D space remove the 3rd coordinate from each vector.
# Use plt.quiver to plot vectors the resulted 2D vectors. Use [0, 0] as an origin
# point for all vectors.
origin_x = [0 for i in range(6)]
origin_y = [0 for i in range(6)]
a = a[:2]
print(a)
x_coords = [a[0], b[0], c[0], d[0], f[0], g[0]]
y_coords = [a[1], b[1], c[1], d[1], f[1], g[1]]
print(origin_x)
print(a[1], b[1], c[1], d[1], f[1], g[1])
plt.quiver(origin_x, origin_y, x_coords, y_coords, color=['r', 'b', 'g', 'c', 'm', 'y'], scale=10)
plt.show()

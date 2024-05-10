import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a null vector of size 10
# Hint: np.zeros()
null_vector = np.zeros(10)
print(f'null_vector = {null_vector}\n')

# Create a vector with values ranging from 299 to 369
# Hint: np.arange()
first_vector = np.arange(299, 370)
print(f'first_vector = {first_vector}\n')

# Make the 5th element of the existing vector to be 1
# Hint: np.array works quite similar to python list.
# Remember how to extract element of list by the index of its element.
first_vector[4] = 1
print(f' 5th element = 1 in first_vector = ')
print(f'{first_vector} \n')

# Reverse the existing vector (the 1st element becomes the last one)
# Hint: np.array works quite similar to python list.
# Remember how to reverse a list.
reverse_vector = first_vector[::-1]
print(f'reverse_vector = {reverse_vector}\n')

# Create a 3x3 matrix with values ranging from 0 to 8
# Hint: np.reshape()
first_matrix = np.reshape(np.arange(9), (3, 3))
print(f'first_matrix = {first_matrix}')

# Create a 3x3 matrix with a random float values
# Hint: np.random.rand()
second_matrix = np.random.rand(3, 3)
print(f'second_matrix = {second_matrix}')

# Create a 3x3 matrix with a random int values
# Hint: np.random.randint()
int_matrix = np.random.randint(1, 10, (3, 3))
print(f'\nint_matrix = ')
print(int_matrix)

# Find min, max and mean values of the existing matrix
min_int_matrix = np.min(int_matrix)
max_int_matrix = np.max(int_matrix)
mean_int_matrix = round(np.mean(int_matrix), 4)
sum_int_matrix = np.sum(int_matrix)
print(f'\nmin = {min_int_matrix}, max = {max_int_matrix}')
print(f'mean = {mean_int_matrix}, sum = {sum_int_matrix}\n')

# Reshape the existing matrix into a vector
# Hint: np.reshape(), np.size()
size_row = np.size(int_matrix, 0)
size_column = np.size(int_matrix, 1)
print(f'rows: {size_row}, columns: {size_column}\n')

int_vector_1 = np.reshape(int_matrix, -1)
int_vector_2 = np.reshape(int_matrix, -1, order='F')
print(f'order = "C": {int_vector_1}, order = "F": {int_vector_2}\n')


# Add a border filled with 0's around the existing array
# Hint: np.pad()
def pad_width(vector, iaxis_pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 0)
    vector[:iaxis_pad_width[0]] = pad_value
    vector[-iaxis_pad_width[1]:] = pad_value


border_matrix = np.pad(int_matrix, 1, pad_width, padder=0)
print(f'border_matrix = ')
print(border_matrix)

# Create 5x3 matrix and 3x2 matrix with a random int values, calculate dot-product of the created matrices
# Hint: np.dot()
a_1 = np.random.randint(1, 10, (5, 3))
a_2 = np.random.randint(1, 5, (3, 2))
a_dot = np.dot(a_1, a_2)
print(f'\ndot_a = ')
print(a_dot)

# Create a vector with a random float values, negate all elements
# which are between 3 and 8
# (substitute original values with -1 * original value), in place.
# Hint: a[(condition 1) & (condition 2)]
vec_1 = 10 * np.random.rand(10)
vec_2 = vec_1[:]
print(f'\nvec_1 = {vec_1}')

for i, el in enumerate(vec_2):
    if 3 < el < 8:
        vec_2[i] = -el
print(f'vec_2 = {vec_2}\n')

# Create 2 vectors of the same chape, stack them vertically
# Hint: np.concatenate(), np.vstack()
a = np.reshape(np.arange(1, 5), (2, 2))
print(f'a = ')
print(a)
b = np.reshape(np.arange(6, 10), (2, 2))
print(f'\nb = ')
print(b)
c = np.concatenate((a, b), 0)
print(f'concatenate((a, b), 0) = ')
print(c)
d = np.vstack((a, b))
print(f'vstack((a,b)) = ')
print(d)

# Take the existing vestors, stack them horizontally
# Hint: np.concatenate(), np.hstack()
c = np.concatenate((a, b), 1)
print(f'concatenate((a, b), 1) = ')
print(c)
d = np.hstack((a, b))
print(f'hstack((a,b)) = ')
print(d)

# Flatten the resulted array
# Hint: np.flatten(), np.ravel(), np.reshape()
c_flatten = c.flatten()
print(f'\nc.flatten() = {c_flatten}')
d_ravel = d.ravel()
print(f'c.ravel() = {d_ravel}')
d_reshape = np.reshape(d, -1)
print(f'd_reshape(d, -1) = {d_reshape}')

# Replace the maximum value by 0 in the existing vector
# Hint: np.argmax()
max_value = c_flatten.argmax()
print(f'\nindex of max_value in c = {max_value}')
c_flatten[max_value] = 0
print(f'c = {c_flatten}')

# Create 2 random arrays A and B of the same shape, check if the created arrays are equal.
# Hint: np.allclose(), np.array_equal()
A= np.random.randint(0, 2, size=4)
B = np.random.randint(0, 2, size=4)
print(f'\nA = {A}')
print(f'B = {B}')
print(f'Are A and B equal? {np.allclose(A, B)}, {np.array_equal(A, B)}\n')
print(f'A == B ?')
print(A == B)

# Create 2D array or take any existinng 2D array, swap any 2 rows of this 2D array.
# Hint: array[[]] = array[[]]
a_1 = np.random.randint(0, 9,  size=(5, 5))
a_1[3] = a_1[3] * 10
print(f'\n 2D array = ')
print(a_1)
b_1 = a_1.copy()
b_1[1] = a_1[3]
b_1[3] = a_1[1]
print(f'\n New 2D array = ')
print(b_1)

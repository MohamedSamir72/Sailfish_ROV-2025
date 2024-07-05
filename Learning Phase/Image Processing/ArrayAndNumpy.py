import time
import numpy as np
import array

# a and b is an array of array with int of 8 bytes size
a = array.array('q')
for i in range(50000):
    a.append(i)

b = array.array('q')
for i in range(50000, 100000):
    b.append(i)

# classic dot product of vectors implementation
start_time = time.process_time()
classic_dot_product = 0.0

for i in range(len(a)):
    classic_dot_product += a[i] * b[i]
end_time = time.process_time()


print(f"classic_dot_product = {str(classic_dot_product)}")
print(f"Computation time using loops = {str(1000*(end_time-start_time))}ms")

# NumPy dot product of vectors implementation
vectorised_start_time = time.process_time()
vectorised_dot_product = np.dot(a, b)
vectorised_end_time = time.process_time()

print(f"\nvectorised_dot_product = {str(vectorised_dot_product)}")
print(f"Computation time using vectorization = {str(1000*(vectorised_end_time-vectorised_start_time))}ms")
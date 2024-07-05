import time 
import numpy as np

# Measure the time excetion for create list with 153,600 element (480x320)
start_list = time.time()

# li = [i for i in range(0, 153600)]    # List Comprehension

li=[]
for i in range(0, 153600):
    li.append(i)

end_list = time.time()

print(start_list)
print(end_list)

print(f"time for list: {float(end_list-start_list)}")



# Measure the time excetion for create numpy array with 153,600 element (480x320)
start_nparray = time.time()

array = np.ones((480, 320))

end_nparray = time.time()
print(start_nparray)
print(end_nparray)
print(f"time for numpy array: {float(start_nparray-end_nparray)}")


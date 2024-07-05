import numpy as np

# Initalize random values with shape (2, 10)
radius_circles1 = np.random.rand(2, 5)
radius_circles2 = np.random.randn(2, 5)

height1 = np.random.randint(1, 5)
height2 = np.random.randint(1, 5, (2, 5))


# Calculate the volume of the circles
volume1 = np.pi*(np.power(radius_circles1, 2))*height1
volume2 = np.pi*(np.power(radius_circles2, 2))*height2

print(f"Type of class: {type(volume1)}")
print(volume1)
print(volume2)

print('#'*65)

max_volume = volume1.max()
max_index_volume = volume1.argmax()

print(f"The max value: {max_volume}")
print(f"The max index: {max_index_volume}")

mean_volume = np.mean(volume2)
median_volume = np.median(volume2)

print(f"The mean of array: {mean_volume}")
print(f"The median of array: {median_volume}")

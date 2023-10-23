import matplotlib.pyplot as plt
import numpy as np


# Data for chart
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])


# plots it
plt.plot(x1,y1,x2,y2)
plt.title("Chart Python")
plt.xlabel("Date")
plt.ylabel("Sales")
# shows it
plt.show()
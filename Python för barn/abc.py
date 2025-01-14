import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams["figure.figsize"] = [12,8]

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]

plt.subplot(2,2,1)
plt.plot(x_vals, y_vals, 'bo-')

plt.subplot(2,2,2)
plt.plot(x_vals, y_vals, 'rx-')

plt.subplot(2,2,3)
plt.plot(x_vals, y_vals, 'g*-')

plt.subplot(2,2,4)
plt.plot(x_vals, y_vals, 'g*-')

plt.show()
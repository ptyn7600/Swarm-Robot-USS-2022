
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
# x_angle_of_object = np.array([0, 10, 20, 30, 40, 50, 60, 70])
# k1 = np.array([10599.39878314, 8958.31756603, 10802.8758637, 12256.5657322, 12470.0684827, 11981.9479903, 11971.15544348,
#                9353.90116377])
# k2 = np.array([-0.91937492, -0.81858459, -0.90763696, -0.95153704, -0.93195211, -0.89389485, -0.90951861,
#                -0.73270896])
# y_angle_from_sensor = np.array([])

# ax = plt.axes(projection='3d')
# ax.scatter3D(k1, k2, x_angle_of_object)
# ax.plot3D(k1, k2, x_angle_of_object,'gray')
# # plt.plot(x_angle_of_object, k1, label='K1')
# plt.show()
#
# plt.plot(x_angle_of_object, k2, label='K2')
# plt.show()
# plt.xlabel('angle of the object')
# plt.ylabel('angle from the sensor')
# plt.legend()

# ============ Plotting 18cm offset angle data ==============

# For offset angle 18cm
x_angle = np.array([-10, -9, -7, -5, -4, -2, 0, 2, 4, 5, 7, 9, 10])
y_reading_mean = np.array([0, 10, 10, 10, 10, 10, 674, 120, 10, 10, 10, 10, 10])
y_reading_std = np.array([0, 0, 0, 0, 0, 0, 78, 115, 0, 0, 0, 0, 0])

plt.plot(x_angle, y_reading_mean, label='Mean')
plt.plot(x_angle, y_reading_std, label='std')
plt.xlabel('angle from the sensor')
plt.ylabel('sensor reading')
plt.legend(labels=['mean', 'std'])
plt.savefig('D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\angle_from_sensor\\')
plt.show()

# -*- coding: utf-8 -*-
"""
the code for estimating the constants k1 and k2 in the equation:

voltage=k1*distance**(k2)

"""
import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits import mplot3d

# data for estimation
distances = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10,
                      10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5,
                      20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24])
angles = [0, 10, 20, 30, 40, 50, 60, 70]
raw_measurements_total_1 = np.arange(343)
raw_measurements_total_2 = np.array([1413, 1932, 2229, 2412, 3056, 3399, 3449, 3175, 2901, 2638, 2473, 2269, 2078, 1970, 1845, 1718, 1590, 1521, 1435,
     1370, 1306, 1241, 1199, 1140, 1087, 1066, 1022, 978, 956, 912, 889, 840, 817, 795, 773, 750, 728, 706, 683, 684,
     662, 662, 639, 617, 616, 594, 594, 572, 572])
# raw_measurements_total = np.arange(49)
count = 0
root= 'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\angle_of_object\\degree_'
filename_degree = 10
while (filename_degree < 71):
    filename = root + str(filename_degree) + '.csv'
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            # print(row[1])
            raw_measurements_total_1[count] = row[1]
            count += 1
    filename_degree += 10
angles_total = np.repeat([angles], 49, axis=1).flatten()
distances_total = (np.repeat([distances], 8,axis=0)).flatten()
raw_measurements_total = np.concatenate([raw_measurements_total_1, raw_measurements_total_2])

ax = plt.axes(projection='3d')
ax.scatter3D(distances_total, angles_total, raw_measurements_total)
ax.plot3D(distances_total, angles_total, raw_measurements_total,'gray')
# plt.plot(x_angle_of_object, k1, label='K1')
plt.show()



# print(raw_measurements_total)
# print(raw_measurements_total.shape)

# plt.plot(distances, raw_measurements_total)
# plt.xlabel('distance [cm]')
# plt.ylabel('raw sensor reading [V]')
# nameFig = 'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\angle_of_object\\graph\\degree_70_gen.png'
# plt.savefig(nameFig)
# plt.show()
#
# distances_trimed = distances[6:]
# raw_measurements_total_trimed = raw_measurements_total[6:]
#
# n = distances_trimed.shape[0]
# y = np.zeros(shape=(n, 1))
# A = np.zeros(shape=(n, 2))
#
# for i in range(n):
#     y[i, 0] = np.log(raw_measurements_total_trimed[i])
#     A[i, 0] = 1
#     A[i, 1] = np.log(distances_trimed[i])
#
# # solution
# c = np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T, A)), A.T), y)
# k1 = np.exp(c[0])
# k2 = c[1]
# print(k1, k2, sep="---")
#
#
# # test on the estimation data
# raw_measurements_total_trimed_prediction = np.zeros(shape=(n, 1))
# for i in range(n):
#     raw_measurements_total_trimed_prediction[i] = k1 * distances_trimed[i] ** (k2)
#
# plt.plot(distances_trimed, raw_measurements_total_trimed_prediction, 'xr', label='least-squares prediction')
# plt.plot(distances_trimed, raw_measurements_total_trimed, 'k', label='real data')
# plt.xlabel('distance [cm]')
# plt.ylabel('voltage [V]')
# plt.legend()
# nameFig = 'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\angle_of_object\\graph\\degree_70_est.png'
# plt.savefig(nameFig)
# plt.show()

# test on the validation data
# n1 = distances2.shape[0]
# raw_measurements2_prediction = np.zeros(shape=(n1, 1))
# for i in range(n1):
#     raw_measurements2_prediction[i] = k1 * distances2[i] ** (k2)
# plt.plot(distances2, raw_measurements2_prediction, 'xr', label='least-squares prediction')
# plt.plot(distances2, raw_measurements2, 'k', label='real data')
# plt.xlabel('distance [cm]')
# plt.ylabel('voltage [V]')
# plt.legend()
# plt.savefig('validation_curve.png')
# plt.show()
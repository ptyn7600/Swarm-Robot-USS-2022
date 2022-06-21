# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math


def function2D(dis, ang, k1, k2):
    returnArr = np.empty(dis.size * ang.size)
    count = 0
    for eachAngle in ang:
        for eachDis in dis:
            result = k1*(np.exp(k2*eachDis))
            returnArr[count] = result
            count += 1
    return returnArr

if __name__ == "__main__":
    # ------------ Variables -------------------------
    print("=== Calculating number of samples ===")
    numberAngle = 4
    numberDistance = 18
    n = numberAngle * numberDistance
    print("Number of sample is " + str(n) + "\n")

    # ----------- Generating data --------------------
    print("=== Generting the data: sensor reading, distance, angle ===")
    mu_array_0=np.array([2896, 2465, 2087, 1815, 1605, 1425, 1280, 1168, 1074,  998,  913,  864,  802, 748,  702,  625, 550, 435])
    mu_array_30=np.array([3121, 2604, 2230, 1936, 1705, 1510, 1360, 1236, 1126, 1054,  977,  908,  853,  802,  747, 708, 656,  637])
    mu_array_40=np.array([3257, 2704, 2280, 1980, 1724, 1539, 1377, 1231, 1138, 1063,  985,  917,  851,  802,  765, 703, 665,  613])
    mu_array_50=np.array([3482, 3178, 2494, 2031, 1901, 1680, 1514, 1138, 1235, 1144, 1088, 1008,  953,  827,  773, 730, 696,  606])
    mu_array_60=np.array([3398, 3112, 2442, 2120, 1875, 1677, 1527, 1376, 1222, 1032, 761, 518, 284, 110, 36, 11, 10, 10])
    mu_array_70=np.array([3427, 3086, 2644, 2230, 1951, 1714, 1565, 1414, 1314, 1173, 963, 763, 550, 334, 124, 37, 10, 10])
    # For ignoring 60-70 degree data
    v = (np.matrix(np.concatenate((mu_array_0, mu_array_30, mu_array_40, mu_array_50)))).T
    # Including 60-70 degree data
    # v = (np.matrix(np.concatenate((mu_array_0, mu_array_30, mu_array_40, mu_array_50, mu_array_60, mu_array_70)))).T
    # print("v: ", end="")
    # print(v)
    # ------------ distance column ---------------------
    d = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
    d = (np.repeat([d], numberAngle, axis=0)).flatten()
    # print("Distance array : ")
    # print(d)
    print("Distance array shape: ", end="")
    print(d.shape)
    # ------------ theta column ---------------------
    # For ignoring 60-70 degree data
    theta = np.array([0, 30, 40, 50])
    # Including 60-70 degree data
    # theta = np.array([0, 30, 40, 50, 60, 70])
    theta = (np.repeat([theta], numberDistance)).flatten()
    # print("Angle : ", end="")
    # print(theta)
    print("Angle shape : ", end="")
    print(theta.shape)
    column_1 = np.full(n, 1)
    # ------------ A matrix ---------------------
    A = (np.matrix([column_1, d])).T
    print("A: ")
    print(A)
    # ------------ A matrix ---------------------
    print("Shape of A: ", end="")
    print(A.shape)

    print("Shape of v", end="")
    print(v.shape)

    # ------------ Start to find solutoin -------
    # solution
    c = np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T, A)), A.T), np.log(v))
    print("x: ")
    print(c)
    k1 = np.exp(c[0])
    k2 = c[1]
    print("k1: ",end="")
    print(k1)
    print("k2: ",end="")
    print(k2)

    # ------------ Plotting the solution 3D -------
    # Creating figure
    fig = plt.figure(figsize=(14, 9))
    ax = plt.axes(projection='3d')

    distance = np.linspace(4, 21, num=200)
    angle = np.linspace(0, 70, num=50)
    f = function2D(distance, angle, k1, k2)

    angle = (np.repeat([angle], 200)).flatten()
    distance = (np.repeat([distance], 50, axis=0)).flatten()
    # print(distance)
    # X, Y = np.meshgrid(distance, angle)
    ax.scatter3D(distance, angle, f)
    ax.scatter3D(d, theta, v, color='red')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # print(distance.shape)
    # print(angle.shape)
    # print(f.shape)
    # plt.savefig('D:\\Research\\Swarm-Robot-USS-2022\\Data\IR\\Distribution\\new\\images\\leastSquareMethod-include60-70\\3D_overall_look')
    # plt.savefig('D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\images\\leastSquareMethod-deleted6070\\3D_overall_look')
    # plt.savefig('D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\images\\leastSquareMethod-deleted6070\\mean_exp_method\\3D_overall_look')
    # plt.show()

    # ------------ Plotting the solution 2D -------
    # Creating figure
    fig = plt.figure()

    distance = np.linspace(4, 21, num=200)
    f = function2D(distance, np.array([0]), k1, k2)
    plt.plot(distance, f)
    plt.scatter(np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), mu_array_0, color='red')
    # plt.savefig('D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\images\\leastSquareMethod-deleted6070\\mean_exp_method\\70degree')
    plt.show()






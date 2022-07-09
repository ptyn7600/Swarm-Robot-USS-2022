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
    std_array_0 = np.array([9, 11, 10, 15, 17, 20, 23, 25, 26, 35, 42, 54, 64, 64, 75, 74, 83, 89])
    std_array_30 = np.array([6, 10, 10, 12, 12, 13, 20, 20, 20, 26, 32, 36, 41, 52, 63, 63, 59, 79])
    std_array_40 = np.array([4, 10, 9, 9, 15, 15, 22, 25, 27, 28, 37, 37, 54, 62, 69, 82, 79, 87])
    std_array_50 = np.array([7, 4, 8, 11, 12, 14, 14, 26, 24, 28, 25, 41, 43, 61, 70, 77, 97, 98])
    std_array_60 = np.array([9, 15, 18, 33, 36, 45, 53, 67, 65, 59, 72, 94, 102, 77, 41, 7, 0, 0])
    std_array_70 = np.array([9, 12, 13, 19, 23, 33, 43, 49, 63, 57, 89, 87, 80, 103, 85, 46, 4, 0])
    # For ignoring 60-70 degree data
    v = (np.matrix(np.concatenate((std_array_0, std_array_30, std_array_40, std_array_50)))).T
    # Including 60-70 degree data
    # v= (np.matrix(np.concatenate((std_array_0, std_array_30, std_array_40, std_array_50, std_array_60, std_array_70)))).T
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
    # plt.savefig('D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\images\\leastSquareMethod-deleted6070\\std_v0\\3D_overall_look')
    # plt.show()

    # ------------ Plotting the solution 2D -------
    # Creating figure
    fig = plt.figure()

    distance = np.linspace(4, 21, num=200)
    f = function2D(distance, np.array([0]), k1, k2)
    plt.plot(distance, f)
    # plt.scatter(np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), std_array_0, color='red')
    x = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
    x = (np.repeat([x], 4, axis=0)).flatten()
    v_test = np.concatenate((std_array_0, std_array_30, std_array_40, std_array_50))
    print(x)
    print(v_test)
    plt.scatter(x, v_test, color='red')
    # plt.savefig('D:\\Research\\Swarm-Robot-USS-2022\\Data\IR\\Distribution\\new\\images\\leastSquareMethod-include60-70\\0degree')
    # plt.savefig('D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\images\\leastSquareMethod-deleted6070\\std_v0\\0degree')
    plt.show()






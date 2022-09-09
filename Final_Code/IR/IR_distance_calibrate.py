import random
from statistics import mean as mu
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn as sns; sns.set()
import pandas as pd
from random import randrange

import math
# from numpy.random import normal
from numpy.random import seed
from scipy.stats import norm
from tabulate import tabulate

from scipy.integrate import simps
from numpy import trapz
from matplotlib.animation import FuncAnimation
from random import randint
from csv import reader

files = ['D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\4cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\5cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\6cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\7cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\8cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\9cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\10cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\11cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\12cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\13cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\14cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\15cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\16cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\17cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\18cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\19cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\20cm_00degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\21cm_00degree.csv'
         ]

def trainingMean(mu):
    # ------------ distance column ---------------------
    d = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
    print("Distance array shape: ", end="")
    print(d.shape)

    # ------------ A matrix ---------------------
    n = len(d)
    column_1 = np.full(n, 1)
    A = (np.matrix([column_1, np.log(d)])).T
    print("A: ")
    print(A)
    # ------------ A matrix ---------------------
    print("Shape of A: ", end="")
    print(A.shape)
    # ------------ v matrix ---------------------
    y = np.log(mu)
    print("Shape of v: ", end="")
    print(y.shape)

    # ------------ Start to find solutoin -------
    c = np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T, A)), A.T), y)
    c = (c.tolist())[0]
    print("c: ")
    print(c)
    k1 = np.exp(c[0])
    k2 = c[1]
    print("k1: ", end="")
    print(k1)
    print("k2: ", end="")
    print(k2)
    return [k1, k2]

def trainingStd(std):
    # ------------ distance column ---------------------
    d = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
    print("Distance array shape: ", end="")
    print(d.shape)

    # ------------ A matrix ---------------------
    n = len(d)
    column_1 = np.full(n, 1)
    A = (np.matrix([column_1, d])).T
    print("A: ")
    print(A)
    # ------------ A matrix ---------------------
    print("Shape of A: ", end="")
    print(A.shape)
    # ------------ v matrix ---------------------
    y = np.log(std)
    print("Shape of v: ", end="")
    print(y.shape)

    # ------------ Start to find solutoin -------
    c = np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T, A)), A.T), y)
    c = (c.tolist())[0]
    print("c: ")
    print(c)
    k1 = np.exp(c[0])
    k2 = c[1]
    print("k1: ", end="")
    print(k1)
    print("k2: ", end="")
    print(k2)
    return [k1, k2]


if __name__ == "__main__":
    mean = []
    std = []
    fileNumber = 0
    for file in files:
        df = pd.read_csv(file)
        columnName = 'x-' + str(fileNumber + 4)
        data = df[columnName]
        mean.append(data.mean())
        std.append(data.std())
        fileNumber += 1
    k = trainingMean(np.array(mean))    # For the mean
    j = trainingStd(std)                # For the std

    d = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
    # Plotting Mean estimation
    fig = plt.figure(figsize=(14, 9))
    x_distance = np.arange(4,21,0.1)
    y_estimate = k[0]*(x_distance**k[1])

    plt.scatter(d, mean, color='orange')
    plt.plot(x_distance, y_estimate, color='green')

    # Plotting std estimation
    fig = plt.figure(figsize=(14, 9))
    x_distance = np.arange(4, 21, 0.1)
    y_estimate = j[0] * ( np.exp(j[1]*x_distance))

    plt.scatter(d, std, color='orange')
    plt.plot(x_distance, y_estimate, color='green')
    plt.show()




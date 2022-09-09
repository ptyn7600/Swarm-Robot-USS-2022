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

# Files
files = ['D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_1cm.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_2cm.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_8cm.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_10cm.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_20cm.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_50cm.csv'
         ]

real_files = ['D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\probability_8cm_0degree.csv',
              'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\probability_20cm_0degree.csv',
              'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\probability_20cm.csv',
              'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\probability_50cm.csv'
              ]
# Make sure the length of data is odd
def findConfidenceInterval(data, confidence):
    # Sort Data
    data.sort()
    # Find the index of the closest number to the mean
    idx_median = len(data)//2

    dataSample = round(len(data) * confidence)
    # Fiding the interval
    if ((dataSample%2) == 0):
        sampleEachSide = dataSample / 2
        minIndx = int((idx_median - sampleEachSide) if (idx_median - sampleEachSide > 0) else 0)
        maxIndx = int((minIndx + dataSample) if ((minIndx + dataSample) < len(data)) else (len(data) - 1))
        minIndx = int((maxIndx - dataSample) if (maxIndx - dataSample > 0) else 0)
        return [data[minIndx], data[maxIndx]]
    else:
        sampleEachSide = (dataSample-1) / 2
        minIndx = int((idx_median - sampleEachSide) if (idx_median - sampleEachSide > 0) else 0)
        maxIndx = int((minIndx + sampleEachSide*2) if ((minIndx + sampleEachSide*2) < len(data)) else (len(data) - 1))
        minIndx = int((maxIndx - sampleEachSide*2) if ((maxIndx - sampleEachSide*2) > 0) else 0)
        if ((minIndx==0) and (maxIndx == (len(data)-1))):
            return [data[minIndx], data[maxIndx]]
        elif (minIndx == 0):
            return [data[minIndx], data[maxIndx+1]]
        elif (maxIndx == (len(data) - 1)):
            return [data[minIndx-1], data[maxIndx]]
        else:
            temp = np.asarray([data[minIndx-1],data[maxIndx+1]])
            selectData = (np.abs(temp - idx_median)).argmin()
            if (selectData == 0):
                return [temp[selectData], data[maxIndx]]
            else:
                return [data[minIndx], temp[selectData]]


# root = 'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\temp\\comparison\\'
if __name__=="__main__":
    fileRead = 0
    probMat = []
    state_dist = np.arange(1, 60.1, 0.1)
    state_angle =  np.arange(0,61,1)

    x_dist_3D = (np.repeat([state_dist], len(state_angle), axis=0)).flatten()
    y_angle_3D = (np.repeat([state_angle], len(state_dist))).flatten()

    fig = plt.figure(figsize=(19.20, 9.83))
    ax = plt.axes(projection='3d')
    root = 'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\temp\\show_july13\\'
    angle = 0
    # ================= REAL ==========================
    with open(real_files[fileRead], 'r') as read_obj:
        csv_reader = reader(read_obj)
        countTrial = 0
        for row in csv_reader:
            # if (countTrial == 0):
            #     row = list(map(np.float64, row))
            rowShape = np.reshape(row, (-1, len(state_dist)))
            #     angle = 0
            #     while (angle < 60):
            #         fig = plt.figure(figsize=(19.20, 9.83))
            #         average_plot = np.array(np.average(np.asmatrix(rowShape[angle]), axis=0))
            #         average_plot = average_plot.flatten()
            #         plt.plot(state_dist, average_plot, color='red')
            #         plt.xlim(0, 60)
            #         # plt.ylim(0, 1)
            #         fileName = root + str(angle) + 'degree'
            #         angle += 1
            #         plt.savefig(fileName)
            # countTrial += 1
            probMat.append(np.array(rowShape, np.float64))
    probMat = np.array(probMat)
    #print(probMat.shape)
    # Plotting the average distribution
    average_plot = np.array((np.array(probMat).mean(axis=0)))
    average_plot = average_plot.flatten()
    color_map = plt.get_cmap('spring')
    scatter_plot = ax.scatter3D(x_dist_3D, y_angle_3D, average_plot, cmap='viridis')
    # plt.colorbar(scatter_plot)
    # ax.set_zlim(0, 1)



    # print(probMat)
    # # Plotting the average distribution
    # average_plot = np.array(np.average(np.asmatrix(probMat), axis=0))
    # average_plot = average_plot.flatten()
    # plt.plot(state, average_plot, color='red')
    # plt.xlim(0, 60)
    # plt.ylim(0, 1)
    #
    # # Plotting the confidence interval
    # percent = 0.9
    # returnArr = []
    # probMat = np.asmatrix(probMat)
    # confidenceInterval = []
    # for i in range(state.size):
    #     confidentData = (((probMat[:, i]).flatten(order='C')).tolist())[0]
    #     confidenceInterval.append(findConfidenceInterval(confidentData, percent))
    # confidenceIntervalMat = np.asmatrix(confidenceInterval)
    # lowerBound = (((confidenceIntervalMat[:, 0]).flatten(order='C')).tolist())[0]
    # upperBound = (((confidenceIntervalMat[:, 1]).flatten(order='C')).tolist())[0]
    # plt.fill_between(state, lowerBound, upperBound, alpha=0.6)


    # ================= SIMULATOR ============================
    # probMat = []
    #
    # with open(files[fileRead], 'r') as read_obj:
    #     csv_reader = reader(read_obj)
    #     for row in csv_reader:
    #         probMat.append(np.array(row[:590], np.float64))
    #
    # # Plotting the average distribution
    # average_plot = np.array(np.average(np.asmatrix(probMat), axis=0))
    # average_plot = average_plot.flatten()
    # plt.plot(state, average_plot, color='green')
    # plt.xlim(0, 60)
    # plt.ylim(0, 1)
    #
    # # Plotting the confidence interval
    # percent = 0.9
    # returnArr = []
    # probMat = np.asmatrix(probMat)
    # confidenceInterval = []
    # for i in range(state.size):
    #     confidentData = (((probMat[:, i]).flatten(order='C')).tolist())[0]
    #     confidenceInterval.append(findConfidenceInterval(confidentData, percent))
    # confidenceIntervalMat = np.asmatrix(confidenceInterval)
    # lowerBound = (((confidenceIntervalMat[:, 0]).flatten(order='C')).tolist())[0]
    # upperBound = (((confidenceIntervalMat[:, 1]).flatten(order='C')).tolist())[0]
    # plt.fill_between(state, lowerBound, upperBound, alpha=0.6)
    #
    # plt.legend(labels=['real', 'real-region', 'simulator','simulator-region'])
    # plt.savefig(root + 'cm')
    plt.show()
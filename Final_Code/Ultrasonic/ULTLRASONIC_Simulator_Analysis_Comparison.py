import random
from statistics import mean as mu

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
# files = ['D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_1cm.csv',
#          'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_2cm.csv',
#          'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_8cm.csv',
#          'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_10cm.csv',
#          'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_20cm.csv',
#          'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\C-Code-Simulator-Analysis\\ULTRASONIC\\data\\probability_50cm.csv'
#          ]
files= ['D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Simulator\\probability_1cm.csv',
        'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Simulator\\probability_2cm.csv',
        'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Simulator\\probability_8cm.csv',
        'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Simulator\\probability_10cm.csv',
        'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Simulator\\probability_20cm.csv',
        'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Simulator\\probability_50cm.csv',
        ]
real_files = ['D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Real\\probability_1cm.csv',
              'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Real\\probability_2cm.csv',
              'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Real\\probability_8cm.csv',
              'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Real\\probability_10cm.csv',
              'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Real\\probability_20cm.csv',
              'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\Analys\\probability_arr\\Real\\probability_50cm.csv',
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


root = 'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\temp\\comparison\\'
if __name__=="__main__":
    rightSize = 20
    numSize = 19
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"

    fileRead = 4
    probMat = []
    state = np.arange(1, 60, 0.1)

    # ================= REAL ==========================
    with open(real_files[fileRead], 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            probMat.append(np.array(row[:590], np.float64))

    print(probMat)
    # Plotting the average distribution
    average_plot = np.array(np.average(np.asmatrix(probMat), axis=0))
    average_plot = average_plot.flatten()
    plt.plot(state, average_plot, color='red')
    plt.xlim(0, 60)
    plt.ylim(0, 1)

    # Plotting the confidence interval
    percent = 0.9
    returnArr = []
    probMat = np.asmatrix(probMat)
    confidenceInterval = []
    for i in range(state.size):
        confidentData = (((probMat[:, i]).flatten(order='C')).tolist())[0]
        confidenceInterval.append(findConfidenceInterval(confidentData, percent))
    confidenceIntervalMat = np.asmatrix(confidenceInterval)
    lowerBound = (((confidenceIntervalMat[:, 0]).flatten(order='C')).tolist())[0]
    upperBound = (((confidenceIntervalMat[:, 1]).flatten(order='C')).tolist())[0]
    plt.fill_between(state, lowerBound, upperBound, alpha=0.6)


    # ================= SIMULATOR ============================
    probMat = []

    with open(files[fileRead], 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            probMat.append(np.array(row[:590], np.float64))

    # Plotting the average distribution
    average_plot = np.array(np.average(np.asmatrix(probMat), axis=0))
    average_plot = average_plot.flatten()
    plt.plot(state, average_plot, color='green')
    plt.xlim(0, 60)
    plt.ylim(0, 1)

    # Plotting the confidence interval
    percent = 0.9
    returnArr = []
    probMat = np.asmatrix(probMat)
    confidenceInterval = []
    for i in range(state.size):
        confidentData = (((probMat[:, i]).flatten(order='C')).tolist())[0]
        confidenceInterval.append(findConfidenceInterval(confidentData, percent))
    confidenceIntervalMat = np.asmatrix(confidenceInterval)
    lowerBound = (((confidenceIntervalMat[:, 0]).flatten(order='C')).tolist())[0]
    upperBound = (((confidenceIntervalMat[:, 1]).flatten(order='C')).tolist())[0]
    plt.fill_between(state, lowerBound, upperBound, alpha=0.6)

    plt.legend(labels=['real', 'real-region', 'simulator','simulator-region'], prop={'size': rightSize})
    plt.title("Confidence Data for Real and Simulation of the US Sensor at 20cm", fontsize=rightSize, fontweight="bold")
    plt.xlabel("Distance (cm)", fontsize=rightSize)
    plt.ylabel("Probability", fontsize=rightSize)

    # plt.xticks(np.concatenate((np.arange(0,6,1), np.arange(6,60,5))))
    plt.xticks(np.concatenate((np.arange(0,17,5), np.arange(17,27,1), np.arange(27,61,5))))
    # plt.xticks(np.arange(0,61,5), fontsize=numSize)
    # plt.savefig(root + 'cm')
    plt.show()
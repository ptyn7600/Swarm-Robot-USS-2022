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

# New Files
files = ['D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.5\\1cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.5\\2cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.5\\8cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.5\\10cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.5\\20cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.5\\50cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.5\\100cm_0degree.csv'
         ]

root = 'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\Analys\\200trials_10samples\\'
state = np.arange(1, 60, 0.1)
# confidence = 0.9
def trainAndgraph(data):
    mean_a = 0.9581686069037303
    mean_b = 0.7625882833237847
    std_a = 0.009280269184555247
    std_b = 0.48783070995817385

    p_last = np.array(np.repeat(1 / state.size, state.size), np.float64)
    p_next = np.array(np.repeat(0.0, state.size), np.float64)
    # print("data : ", data)
    for val in data:
        count = 0
        for eachState in state:
            mean = mean_a * eachState + mean_b
            std = std_a * eachState + std_b
            # print("mean ", mean)
            # print("std ", std)
            prob = norm(mean, std).pdf(val)
            p_next[count] = prob * p_last[count]
            count += 1
        p_last = p_next / (sum(p_next))
    # plt.plot(state, p_last, '--')
    return p_last

def findConfidenceIntervalMean(data, confidence):
    # Find the mean
    mean_data = mu(data)
    # Sort Data
    data.sort()
    # Find the index of the closest number to the mean
    array = np.asarray(data)
    idx_mean = (np.abs(array - mean_data)).argmin()

    dataSample = round(len(data) * confidence)
    # Fiding the interval
    if ((dataSample%2) == 0):
        sampleEachSide = dataSample / 2
        minIndx = int((idx_mean - sampleEachSide) if (idx_mean - sampleEachSide > 0) else 0)
        maxIndx = int((minIndx + dataSample) if ((minIndx + dataSample) < len(data)) else (len(data) - 1))
        minIndx = int((maxIndx - dataSample) if (maxIndx - dataSample > 0) else 0)
        return [data[minIndx], data[maxIndx]]
    else:
        sampleEachSide = (dataSample-1) / 2
        minIndx = int((idx_mean - sampleEachSide) if (idx_mean - sampleEachSide > 0) else 0)
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
            selectData = (np.abs(temp - mean_data)).argmin()
            if (selectData == 0):
                return [temp[selectData], data[maxIndx]]
            else:
                return [data[minIndx], temp[selectData]]

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

if __name__=="__main__":
    # straight line y = a*x + b
    mean_a = 0.9581686069037303
    mean_b = 0.7625882833237847
    std_a = 0.009280269184555247
    std_b = 0.48783070995817385

    fileNumber = 0
    numberSample = 10
    trial = 200
    distToPrint = [1,2,8,10,20,50,100]
    while (fileNumber < 7):
        fig = plt.figure(figsize=(19.20,9.83))
        # data
        df = pd.read_csv(files[fileNumber])
        data = list(df['x'])
        probMat = []
        for i in range(trial):
            dataPick = []
            for sample in range(numberSample):
                random_index = random.randint(0, len(data)-1)
                dataPick.append(data.pop(random_index))
            probMat.append(trainAndgraph(dataPick))

        # Plotting the average distribution
        average_plot = np.array(np.average(np.asmatrix(probMat), axis=0))
        average_plot = average_plot.flatten()
        plt.plot(state, average_plot, color='red')
        plt.xlim(0, 60)
        plt.ylim(0, 1)
        # Plotting the overlap
        percent = 0.9
        returnArr = []
        probMat = np.asmatrix(probMat)
        confidenceInterval = []
        for i in range(state.size):
            confidentData = (((probMat[:,i]).flatten(order='C')).tolist())[0]
            confidenceInterval.append(findConfidenceInterval(confidentData, confidence))
        confidenceIntervalMat = np.asmatrix(confidenceInterval)
        lowerBound = (((confidenceIntervalMat[:, 0]).flatten(order='C')).tolist())[0]
        upperBound = (((confidenceIntervalMat[:, 1]).flatten(order='C')).tolist())[0]
        plt.fill_between(state, lowerBound, upperBound, alpha=0.6)

        # Move to next file
        fileNumber += 1

        plt.title('The Average Graph of 200 Trials with 10 Samples Each')
        plt.xlabel('Distances (cm)')
        plt.ylabel('Probability')
        plt.show()
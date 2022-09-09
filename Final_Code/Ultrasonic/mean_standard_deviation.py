import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn as sns; sns.set()
import pandas as pd
import math
import scipy.stats as stats
from numpy.random import normal
from numpy.random import seed

fileCount = 21
files = ['D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\1cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\2cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\3cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\4cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\5cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\6cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\7cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\8cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\9cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\10cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\11cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\12cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\13cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\14cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\15cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\16cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\17cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\18cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\19cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\20cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\21cm_0degree.csv'
         ]

def plotMeanStd():
    # Combine Data Files
    count = 0
    distance = np.arange(1,22,1)
    mean = []
    std = []
    while (count < fileCount):
        temp = pd.read_csv(files[count])
        data = temp['x']
        mean.append(data.mean())
        std.append(data.std())
        count = count + 1
    plt.plot(distance, mean)
    plt.plot(distance, std)
    plt.xticks(distance)
    return [mean, std]

def plotLinebestFit(data_x, data_y):
    theta = np.polyfit(data_x, data_y, 1)
    y_line = theta[1] + theta[0]*data_x
    plt.plot(data_x, y_line)
    return theta

if __name__=="__main__":
    # Distances array
    distance = np.arange(1,22,1)

    # Plot the relationship of mean and std to distances
    fig = plt.figure(figsize=(19.20,9.83))
    [mean, std] = plotMeanStd()

    # Plot the line best fit of the mean and std
    print(plotLinebestFit(distance, mean))
    print(plotLinebestFit(distance, std))

    plt.title('The Graph of Mean and Standard Deviation to Distances')
    plt.xlabel('Distances (cm)')
    plt.ylabel('Estimated Distances (cm)')
    fig.legend(labels=['mean','standard deviation','mean-best-fit','std-best-fit'])
    plt.show()

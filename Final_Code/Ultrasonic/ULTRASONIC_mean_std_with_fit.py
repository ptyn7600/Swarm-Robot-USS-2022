import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd

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
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\21cm_0degree.csv',
         ]

rightSize = 20
numSize = 19
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
# Combine Data Files
count = 0
mean = []
std = []
while (count < fileCount):
    temp = pd.read_csv(files[count])
    data = temp['x']
    mean.append(data.mean())
    std.append(data.std())
    count = count + 1

# Plotting Mean estimation
fig = plt.figure(figsize=(14, 9))
x_distance = np.arange(1,22,1)
plt.plot(x_distance, mean)
# PLotting mean best fit
theta = np.polyfit(x_distance, mean, 1)
mean_fit = theta[1] + theta[0] * x_distance
plt.plot(x_distance, mean_fit, linestyle='--')


# Plotting std estimation
plt.plot(x_distance, std)
# PLotting mean best fit
theta = np.polyfit(x_distance, std, 1)
std_fit = theta[1] + theta[0] * x_distance
plt.plot(x_distance, std_fit, linestyle='--')

plt.legend(loc='center right', labels=['Mean', 'Mean Best-fit', 'Standard Deviation', 'Standard Deviation Best-fit'])
plt.title("Relationship of Mean and Standard Deviation to Distance with Fit", fontsize=rightSize, fontweight="bold")
plt.xticks(x_distance, fontsize=numSize)
plt.yticks(fontsize=numSize)
plt.xlabel("Expected Distances (cm)", fontsize=rightSize)
plt.ylabel("Estimated Distances (cm)", fontsize=rightSize)
plt.show()
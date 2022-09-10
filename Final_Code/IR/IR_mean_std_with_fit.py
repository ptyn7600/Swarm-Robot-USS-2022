import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd

fileCount = 18
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
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\IR\\0degree\\21cm_00degree.csv',
         ]

rightSize = 16
numSize = 14
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
# Combine Data Files
count = 0
mean = []
std = []
while (count < fileCount):
    temp = pd.read_csv(files[count])
    columnName = 'x-'+ str(count+4)
    data = temp[columnName]
    mean.append(data.mean())
    std.append(data.std())
    count = count + 1

# Plotting Mean estimation
fig, ax = plt.subplots()
x_distance = np.arange(4,22,1)
ax.plot(x_distance, mean, color="orange")
# PLotting mean best fit
mean_a = 11955.224610613135
mean_b = -0.9738407600162202
mean_fit = mean_a*np.power(x_distance, np.full(len(x_distance), mean_b))
ax.plot(x_distance, mean_fit, linestyle='--', color='black')

ax.set_ylabel("Sensor Raw Reading", fontsize=rightSize)
ax.set_xlabel("Expected Distances (cm)", fontsize=rightSize)
ax.legend(loc='center left', labels=['Mean', 'Mean Best-fit'], facecolor='white')

# Plotting std estimation
ax2 = ax.twinx()
ax2.plot(x_distance, std, color="blue")
ax2.set_ylabel("Standard Deviation", fontsize=rightSize)

# PLotting mean best fit
std_a = 5.574431613205327
std_b = 0.14072513618767238
std_fit = std_a*np.exp(x_distance*std_b)
ax2.plot(x_distance, std_fit, linestyle='--', color='purple')

ax2.legend(loc='center right', labels=['Standard Deviation', 'Standard Deviation Best-fit'], facecolor='white')
ax2.grid(False)


ax.tick_params(axis='both', which='major', labelsize=numSize)
ax2.tick_params(axis='both', which='major', labelsize=numSize)
plt.title("Relationship of Mean and Standard Deviation to Distance with Fit", fontsize=rightSize, fontweight="bold")
plt.xticks(x_distance)

plt.grid(False)
ax.set_facecolor("white")
ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['right'].set_color('black')
ax.spines['left'].set_color('black')
ax.tick_params(top=False, bottom=True, left=True, right=True)
plt.show()
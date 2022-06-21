import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn as sns; sns.set()
import pandas as pd
import scipy.stats as stats
from numpy.random import normal
from numpy.random import seed

# Files for 0 Degree
files = ['D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_-10degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_-9degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_-7degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_-5degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_-4degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_-2degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_2degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_4degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_5degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_7degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_9degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_10degree.csv']

def normal_dist(x , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

# root= 'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\'
# filename = root + '5cm_0degree' + '.csv'
# data = np.arange(1000)
# count = 0

# with open(filename, newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',')
#     for row in spamreader:
#         data[count] = row[0]
#         count = count + 1


# tips = pd.read_csv('D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\5cm_0degree.csv')
# # penguins = sns.load_dataset("D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\5cm_0degree.csv")
# sns.displot(data=tips, x="x", kde=True)
#
# plt.savefig("D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\images\\5cm_0degree")
# plt.show()

# merging two csv files
# df = pd.me(
#     map(pd.read_csv, [files[0], files[1]]), ignore_index=True)
# print(df)

fig, ax1 = plt.subplots()
count = 0
df = pd.read_csv(files[count])
while (count < 12):
    count = count + 1
    temp = pd.read_csv(files[count])
    df = pd.concat([df, temp], axis = 1)
# print(df)

x = np.linspace(-100, 100, 1000)
count = 0
mu_array=np.arange(13)
std_array=np.arange(13)
seed(1)
for column in df.columns:
    plt.hist(df[column], density=True)
    mu = df[column].mean()
    std = df[column].std()
    mu_array[count] = mu
    std_array[count] = std
    count = count + 1

print(mu_array)
print(std_array)

x_axis = angleArr = np.array([-10, -9, -7, -5, -4, -2, 0, 2, 4, 5, 7, 9, 10])
color = 'tab:red'
plt.plot(x_axis, mu_array, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.xticks(x_axis)

# ax2 = ax1.twinx()
# color = 'tab:blue'
# ax2.plot(x_axis, std_array, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
# fig.tight_layout()  # otherwise the right y-label is slightly clipped


count = 0
while (count < 13):
    data = normal(loc=mu_array[count], scale=std_array[count], size=200)
    sns.distplot(data, hist=False, kde=True)
    count = count + 1

fig.legend(labels=['x-4','x-5', 'x-6','x-7','x-8', 'x-9', 'x-10', 'x-11', 'x-12', 'x-13', 'x-14', 'x-15',
                   'x-16', 'x-17', 'x-18', 'x-19', 'x-20', 'x-21'])

plt.show()
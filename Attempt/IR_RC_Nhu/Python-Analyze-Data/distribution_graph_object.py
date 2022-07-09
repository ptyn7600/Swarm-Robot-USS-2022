import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn as sns; sns.set()
import pandas as pd
import scipy.stats as stats
from numpy.random import normal
from numpy.random import seed

# Files for 0 Degree
files = ['D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\4cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\5cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\6cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\7cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\8cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\9cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\10cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\11cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\12cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\13cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\14cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\15cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\16cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\17cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\18cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\19cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\20cm_00degree.csv',
             'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\0degree\\Redo\\21cm_00degree.csv']

# Files for 0 Degrees
files_0 = ['C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\4cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\5cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\6cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\7cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\8cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\9cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\10cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\11cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\12cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\13cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\14cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\15cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\16cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\17cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\18cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\19cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\20cm_0degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\0degree\\21cm_0degree.csv']


# Files for 30 Degrees
files_30 = ['C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\4cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\5cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\6cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\7cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\8cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\9cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\10cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\11cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\12cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\13cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\14cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\15cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\16cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\17cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\18cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\19cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\20cm_30degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\30degree\\21cm_30degree.csv']


# Files for 40 Degrees
files_40 = ['C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\4cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\5cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\6cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\7cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\8cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\9cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\10cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\11cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\12cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\13cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\14cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\15cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\16cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\17cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\18cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\19cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\20cm_40degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\40degree\\21cm_40degree.csv']
# Files for 50 Degrees
files_50 = ['C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\4cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\5cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\6cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\7cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\8cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\9cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\10cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\11cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\12cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\13cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\14cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\15cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\16cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\17cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\18cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\19cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\20cm_50degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\50degree\\21cm_50degree.csv']
# Files for 60 Degrees
files_60 = ['C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\4cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\5cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\6cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\7cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\8cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\9cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\10cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\11cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\12cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\13cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\14cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\15cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\16cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\17cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\18cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\19cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\20cm_60degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\60degree\\21cm_60degree.csv']
# Files for 70 Degrees
files_70 = ['C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\4cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\5cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\6cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\7cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\8cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\9cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\10cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\11cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\12cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\13cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\14cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\15cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\16cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\17cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\18cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\19cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\20cm_70degree.csv',
         'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\70degree\\21cm_70degree.csv']

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
while (count < 17):
    count = count + 1
    temp = pd.read_csv(files[count])
    df = pd.concat([df, temp], axis = 1)
# print(df)

x = np.linspace(-100, 100, 1000)
count = 0
mu_array=np.arange(18)
std_array=np.arange(18)
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

x_axis = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
color = 'tab:red'
plt.plot(x_axis, mu_array, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.xticks(x_axis)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.plot(x_axis, std_array, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()  # otherwise the right y-label is slightly clipped


# count = 0
# while (count < 18):
#     data = normal(loc=mu_array[count], scale=std_array[count], size=200)
#     sns.distplot(data, hist=False, kde=True)
#     count = count + 1
#
# fig.legend(labels=['x-4','x-5', 'x-6','x-7','x-8', 'x-9', 'x-10', 'x-11', 'x-12', 'x-13', 'x-14', 'x-15',
#                    'x-16', 'x-17', 'x-18', 'x-19', 'x-20', 'x-21'])

plt.show()
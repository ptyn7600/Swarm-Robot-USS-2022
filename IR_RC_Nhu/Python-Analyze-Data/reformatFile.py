import numpy as np
import matplotlib.pyplot as plt
import csv
import seaborn as sns; sns.set()
import pandas as pd
import scipy.stats as stats
from numpy.random import normal
from numpy.random import seed

angleArr = np.array([-10, -9, -7, -5, -4, -2, 0, 2, 4, 5, 7, 9, 10])
root= 'D:\\Research\\Swarm-Robot-USS-2022\\Data\\IR\\Distribution\\new\\OffsetAngle_18cm\\18cm_offset_'
degree = 00
# while (degree < 71):
distance = 0
while(distance < 13):
    # filename = root + str(degree) + 'degree\\' + '' + str(distance) + 'cm_' +  str(degree) +'degree' + '.csv'
    filename = root + str(angleArr[distance]) + 'degree.csv'
    print(filename)
    df = pd.read_csv(filename, header=None)
    newName = 'x-' + str(angleArr[distance])
    df.rename(columns={0: newName}, inplace=True)
    df.to_csv(filename, index=False)
    distance += 1
    # degree += 10

# distance = 4
# while(distance < 22):
#     filename = root + str(degree) + 'degree\\' + '' + str(distance) + 'cm_' + str(degree) + 'degree' + '.csv'
#     with open("filename",'r') as f:
#         with open("updated_test.csv",'w') as f1:
#             next(f) # skip header line
#             for line in f:
#                 f1.write(line)
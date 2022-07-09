import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
import numpy as np
import math
# ============== Files ======================
files = ['D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_10samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_50samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_100samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_200samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_300samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_400samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_500samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_600samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_700samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_800samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_900samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_1000samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_1500samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Final_Data\\Ultrasonic\\Section2.2.2\\10cm_0degree_2000samples.csv']
# ==================== Save File Root =================
root = 'D:\\Research\\Swarm-Robot-USS-2022\\Final_Graph\\Ultrasonic\\Section2.2.2\\'

fig, axs = plt.subplots(2, 2, figsize=(19.20,9.83))
binwidth = 0.1
# ============== 10 Samples ======================
df = pd.read_csv(files[0])
axs[0, 0].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs[0, 0].set_title('10 Samples')

# ============== 50 Samples ======================
df = pd.read_csv(files[1])
axs[0, 1].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs[0, 1].set_title('50 Samples')

# ============== 100 Samples ======================
df = pd.read_csv(files[2])
axs[1, 0].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth),  lw=0)
axs[1, 0].set_title('100 Samples')

# ============== 200 Samples ======================
df = pd.read_csv(files[3])
axs[1, 1].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs[1, 1].set_title('200 Samples')

plt.savefig(root + 'figure3_1')

# =======================================================================================================
fig1, axs1 = plt.subplots(2, 2,figsize=(19.20,9.83))
# ============== 300 Samples ======================
df = pd.read_csv(files[4])
axs1[0, 0].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs1[0, 0].set_title('300 Samples')

# ============== 400 Samples ======================
df = pd.read_csv(files[5])
axs1[0, 1].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs1[0, 1].set_title('400 Samples')

# ============== 500 Samples ======================
df = pd.read_csv(files[6])
# axs1[1, 0].hist((df['x']), density=False, bins=size, lw=0)
axs1[1, 0].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs1[1, 0].set_title('500 Samples')

# ============== 600 Samples ======================
df = pd.read_csv(files[7])
axs1[1, 1].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs1[1, 1].set_title('6000 Samples')

plt.savefig(root + 'figure3_2')

# ================================================================================================
fig2, axs2 = plt.subplots(2, 2, figsize=(19.20,9.83))

# ============== 700 Samples ======================
df = pd.read_csv(files[8])
axs2[0, 0].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs2[0, 0].set_title('700 Samples')

# ============== 800 Samples ======================
df = pd.read_csv(files[9])
axs2[0, 1].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs2[0, 1].set_title('800 Samples')

# ============== 900 Samples ======================
df = pd.read_csv(files[10])
axs2[1, 0].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs2[1, 0].set_title('900 Samples')

# ============== 1000 Samples ======================
df = pd.read_csv(files[11])
axs2[1, 1].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs2[1, 1].set_title('1000 Samples')

plt.savefig(root + 'figure3_3')

# ================================================================================================
fig3, axs3 = plt.subplots(2, 1, figsize=(19.20,9.83))
# ============== 1500 Samples ======================
df = pd.read_csv(files[12])
axs3[0].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs3[0].set_title('1500 Samples')

# ============== 2000 Samples ======================
df = pd.read_csv(files[13])
axs3[1].hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0)
axs3[1].set_title('2000 Samples')


plt.savefig(root + 'figure3_4')
plt.show()


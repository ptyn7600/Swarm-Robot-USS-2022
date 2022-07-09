import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
import numpy as np
import math
# ============== Files ======================
files = ['D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_10samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_50samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_100samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_500samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_1000samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_1500samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_2000samples.csv']
#
# files_test = ['D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_100samples.csv',
#          'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_200samples.csv',
#          'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_300samples.csv',
#          'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_400samples.csv',
#          'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_500samples.csv']

# files = ['C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_10samples.csv',
#          'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_50samples.csv',
#          'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_100samples.csv',
#          'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_200samples.csv',
#          'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_300samples.csv',
#          'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_400samples.csv',
#          'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_500samples.csv',
#          'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_600samples.csv',
#          'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_700samples.csv',
#          'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_800samples.csv',
#          'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_900samples.csv',
#          'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_1000samples.csv']
#
# files_test = ['C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_100samples.csv',
#               'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_200samples.csv',
#               'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_300samples.csv',
#               'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_400samples.csv',
#               'C:\\Users\\Phan_Tra_Yen_Nhu\\Desktop\\Study-Material\\Miami-Semester\\Research\\USS-2022\\data\\ultrasonic\\dist-test\\10cm_0degree_500samples.csv']


# V1 of measuring
files = ['D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_10samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_50samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_100samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_200samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_300samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_400samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_500samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_1000samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_1500samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\10cm_0degree_2000samples.csv']
# V2 of measuring
files_new = ['D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_10samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_50samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_100samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_200samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_300samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_400samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_500samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_600samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_700samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_800samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_900samples.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Data\\Ultrasonic\\testing\\v2\\10cm_0degree_1000samples.csv']

fig, axs = plt.subplots(2, 2, figsize=(19.20,9.83))
# ============== 10 Samples ======================
df = pd.read_csv(files[0])
# ---- Sturge’s rule
# size = 1 + math.ceil(math.log2(df.size))
# ---- Freedman-Diaconis rule
first_quartile = np.percentile(df['x'], 25)
third_quartile = np.percentile(df['x'], 75)
bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# ---- #bin = # of samples
# size = df['x'].size
print(size)
# axs[0, 0].hist((df['x']), density=False, bins=size, lw=0)
axs[0, 0].hist((df['x']), density=False, lw=0)
axs[0, 0].set_title('10 Samples')

# ============== 50 Samples ======================
df = pd.read_csv(files[1])

# ---- Sturge’s rule
# size = 1 + math.ceil(math.log2(df.size))
# ---- Freedman-Diaconis rule
first_quartile = np.percentile(df['x'], 25)
third_quartile = np.percentile(df['x'], 75)
bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# ---- #bin = # of samples
# size = df['x'].size
print(size)
# axs[0, 1].hist((df['x']), density=False, bins=size, lw=0)
axs[0, 1].hist((df['x']), density=False, lw=0)
axs[0, 1].set_title('50 Samples')

# ============== 100 Samples ======================
df = pd.read_csv(files[2])
# ---- Sturge’s rule
# size = 1 + math.ceil(math.log2(df.size))
# ---- Freedman-Diaconis rule
first_quartile = np.percentile(df['x'], 25)
third_quartile = np.percentile(df['x'], 75)
bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# ---- #bin = # of samples
# size = df['x'].size
print(size)

# axs[1, 0].hist((df['x']), density=False, bins=size, lw=0)
axs[1, 0].hist((df['x']), density=False, lw=0)
axs[1, 0].set_title('100 Samples')

# ============== 500 Samples ======================
df = pd.read_csv(files[3])
# ---- Sturge’s rule
# size = 1 + math.ceil(math.log2(df.size))
# ---- Freedman-Diaconis rule
first_quartile = np.percentile(df['x'], 25)
third_quartile = np.percentile(df['x'], 75)
bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# ---- #bin = # of samples
# size = df['x'].size
print(size)
# axs[1, 1].hist((df['x']), density=False, bins=size, lw=0)
axs[1, 1].hist((df['x']), density=False, lw=0)
axs[1, 1].set_title('200 Samples')

plt.savefig('./figure1_v1', dpi=600)

# =======================================================================================================
fig1, axs1 = plt.subplots(2, 2,figsize=(19.20,9.83))
# ============== 1000 Samples ======================
df = pd.read_csv(files[4])
# ---- Sturge’s rule
# size = 1 + math.ceil(math.log2(df.size))
# ---- Freedman-Diaconis rule
first_quartile = np.percentile(df['x'], 25)
third_quartile = np.percentile(df['x'], 75)
bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# ---- #bin = # of samples
# size = df['x'].size
print(size)
# axs1[0, 0].hist((df['x']), density=False, bins=size, lw=0)
axs1[0, 0].hist((df['x']), density=False, lw=0)
axs1[0, 0].set_title('300 Samples')

# ============== 1500 Samples ======================
df = pd.read_csv(files[5])
# ---- Sturge’s rule
# size = 1 + math.ceil(math.log2(df.size))
# ---- Freedman-Diaconis rule
first_quartile = np.percentile(df['x'], 25)
third_quartile = np.percentile(df['x'], 75)
bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# ---- #bin = # of samples
# size = df['x'].size
print(size)
# axs1[0, 1].hist((df['x']), density=False, bins=size, lw=0)
axs1[0, 1].hist((df['x']), density=False, lw=0)
axs1[0, 1].set_title('400 Samples')

# ============== 2000 Samples ======================
df = pd.read_csv(files[6])
# ---- Sturge’s rule
# size = 1 + math.ceil(math.log2(df.size))
# ---- Freedman-Diaconis rule
first_quartile = np.percentile(df['x'], 25)
third_quartile = np.percentile(df['x'], 75)
bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# ---- #bin = # of samples
# size = df['x'].size
print(size)
# axs1[1, 0].hist((df['x']), density=False, bins=size, lw=0)
axs1[1, 0].hist((df['x']), density=False, lw=0)
axs1[1, 0].set_title('500 Samples')

# ============== 500 Samples ======================
df = pd.read_csv(files[7])
# ---- Sturge’s rule
# size = 1 + math.ceil(math.log2(df.size))
# ---- Freedman-Diaconis rule
first_quartile = np.percentile(df['x'], 25)
third_quartile = np.percentile(df['x'], 75)
bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# ---- #bin = # of samples
# size = df['x'].size
print(size)
# axs1[1, 1].hist((df['x']), density=False, bins=size, lw=0)
axs1[1, 1].hist((df['x']), density=False, lw=0)
axs1[1, 1].set_title('1000 Samples')

plt.savefig('./figure2_v1')

# ================================================================================================
fig2, axs2 = plt.subplots(2, 2, figsize=(19.20,9.83))

# ============== 200 Samples ======================
df = pd.read_csv(files[8])
# ---- Sturge’s rule
# size = 1 + math.ceil(math.log2(df.size))
# ---- Freedman-Diaconis rule
first_quartile = np.percentile(df['x'], 25)
third_quartile = np.percentile(df['x'], 75)
bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# ---- #bin = # of samples
# size = df['x'].size
print(size)
# axs2[0, 0].hist((df['x']), density=False, bins=size, lw=0)
axs2[0, 0].hist((df['x']), density=False, lw=0)
axs2[0, 0].set_title('1500 Samples')

# ============== 300 Samples ======================
df = pd.read_csv(files[9])
# ---- Sturge’s rule
# size = 1 + math.ceil(math.log2(df.size))
# ---- Freedman-Diaconis rule
first_quartile = np.percentile(df['x'], 25)
third_quartile = np.percentile(df['x'], 75)
bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# ---- #bin = # of samples
# size = df['x'].size
print(size)
# axs2[0, 1].hist((df['x']), density=False, bins=size, lw=0)
axs2[0, 1].hist((df['x']), density=False, lw=0)
axs2[0, 1].set_title('2000 Samples')

# ============== 400 Samples ======================
# df = pd.read_csv(files[10])
# # ---- Sturge’s rule
# # size = 1 + math.ceil(math.log2(df.size))
# # ---- Freedman-Diaconis rule
# first_quartile = np.percentile(df['x'], 25)
# third_quartile = np.percentile(df['x'], 75)
# bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
# size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# # ---- #bin = # of samples
# size = df['x'].size
# print(size)
# axs2[1, 0].hist((df['x']), density=False, bins=size, lw=0)
# # axs2[1, 0].hist((df['x']), density=False, lw=0)
# axs2[1, 0].set_title('900 Samples')
#
# # ============== 500 Samples ======================
# df = pd.read_csv(files[11])
# # ---- Sturge’s rule
# # size = 1 + math.ceil(math.log2(df.size))
# # ---- Freedman-Diaconis rule
# first_quartile = np.percentile(df['x'], 25)
# third_quartile = np.percentile(df['x'], 75)
# bin_width = 2 * (third_quartile - first_quartile)/((df['x'].size)**(1/3))
# size = math.ceil((df['x'].max() - df['x'].min())/bin_width)
# # ---- #bin = # of samples
# size = df['x'].size
# print(size)
# axs2[1, 1].hist((df['x']), density=False, bins=size, lw=0)
# # axs2[1, 1].hist((df['x']), density=False, lw=0)
# axs2[1, 1].set_title('1000 Samples')

plt.savefig('./figure3_v1')
plt.show()


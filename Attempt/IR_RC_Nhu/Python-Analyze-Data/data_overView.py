import numpy as np
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
mu_array_0=np.array([2896, 2465, 2087, 1815, 1605, 1425, 1280, 1168, 1074,  998,  913,  864,  802, 748,  702,  625,  550, 435])
std_array_0=np.array([10,  6, 15, 17, 20, 24, 30,33, 34, 47, 58, 63, 69, 80, 91, 83, 89, 99])

mu_array_00=np.array([2926, 2458, 2103, 1825, 1613, 1444, 1285, 1170, 1082, 1003,  932,  871,  812,  756, 703, 657, 632, 595])
std_array_00=np.array([9, 11, 10, 15, 17, 20, 23, 25, 26, 35, 42, 54, 64, 64, 75, 74, 83, 89])

mu_array_30=np.array([3121, 2604, 2230, 1936, 1705, 1510, 1360, 1236, 1126, 1054,  977,  908,  853,  802,  747,  708, 656,  637])
std_array_30=np.array([6, 10, 10, 12, 12, 13, 20, 20, 20, 26, 32, 36, 41, 52, 63, 63, 59, 79])

mu_array_40=np.array([3257, 2704, 2280, 1980, 1724, 1539, 1377, 1231, 1138, 1063,  985,  917,  851,  802,  765,  703, 665,  613])
std_array_40=np.array([4, 10,  9,  9, 15, 15, 22, 25, 27, 28, 37, 37, 54, 62, 69, 82, 79, 87])

mu_array_50=np.array([3482, 3178, 2494, 2031, 1901, 1680, 1514, 1138, 1235, 1144, 1088, 1008,  953,  827,  773, 730, 696,  606])
std_array_50=np.array([7,  4,  8, 11, 12, 14, 14, 26, 24, 28, 25, 41, 43, 61, 70, 77, 97, 98])

mu_array_60=np.array([3398, 3112, 2442, 2120, 1875, 1677, 1527, 1376, 1222, 1032, 761, 518, 284, 110, 36, 11, 10, 10])
std_array_60=np.array([9,  15,  18,  33,  36,  45,  53,  67,  65,  59,  72,  94, 102,  77,  41,   7,   0,   0])

mu_array_70=np.array([3427, 3086, 2644, 2230, 1951, 1714, 1565, 1414, 1314, 1173, 963, 763, 550, 334, 124, 37, 10, 10])
std_array_70=np.array([9, 12,  13,  19,  23,  33,  43,  49,  63,  57, 89,  87,  80, 103,  85, 46,   4, 0])

x_axis = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
# color = 'tab:red'
# plt.plot(x_axis, mu_array_0)
# plt.plot(x_axis, mu_array_00)
# plt.plot(x_axis, mu_array_30)
# plt.plot(x_axis, mu_array_40)
# plt.plot(x_axis, mu_array_50)
# plt.plot(x_axis, mu_array_60)
# plt.plot(x_axis, mu_array_70)
# ax1.tick_params(axis='y', labelcolor=color)
# plt.xticks(x_axis)
# plt.legend(labels=['mean-0degree','mean-00degree','mean-30degree', 'mean-40degree','mean-50degree','mean-60degree', 'mean-70degree'])

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.plot(x_axis, std_array_0)
ax2.plot(x_axis, std_array_00)
ax2.plot(x_axis, std_array_30)
ax2.plot(x_axis, std_array_40)
ax2.plot(x_axis, std_array_50)
ax2.plot(x_axis, std_array_60)
ax2.plot(x_axis, std_array_70)
ax2.tick_params(axis='y', labelcolor=color)
plt.xticks(x_axis)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.legend(labels=['std-0degree','std-00degree', 'std-30degree', 'std-40degree','std-50degree','std-60degree', 'std-70degree'])
plt.show()
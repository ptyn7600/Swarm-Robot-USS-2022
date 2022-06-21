import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))
#
# x = np.linspace(4, 21, num=40)
# y = np.linspace(4, 21, num=40)
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)
#
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.contour3D(X, Y, Z, 50, cmap='binary')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# # print(Z)
# plt.show()
#
# # nx, ny = (3, 2)
# # x = np.linspace(0, 1, nx)
# # y = np.linspace(0, 1, ny)
# # print(x)
# # print(y)

x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T # transpose

print(x)
print(y)
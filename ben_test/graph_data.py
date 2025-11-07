import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from math import pi, sin, cos



data = pd.read_csv('/home/aero/aero/ben_test/data.csv')
A = [data['Ax'].tolist(), data['Ay'].tolist(), data['Az'].tolist()]
G = [data['Gx'].tolist(), data['Gy'].tolist(), data['Gz'].tolist()]

dt = 0.1

a, v, vi, dx, va, r = [[0,0,0] for i in range(6)]
X = [[0], [0], [0]]

va_c = [G[0][0], G[1][0], G[2][0]]

for i in range(len(A[0])):
    a = [A[0][i], A[1][i], A[2][i]]
    va = [G[0][i] - va_c[0], G[1][i] - va_c[1], G[2][i] - va_c[2]]
    for dim in range(3):
        a[dim] = A[dim][i]
        av = G[dim][i]
        a[dim] /= 9.80665
        vi[dim] = v[dim]
        v[dim] = vi[dim] + a[dim]*dt
        dx[dim] = vi[dim]*dt + 0.5*a[dim]*pow(dt,2)

        va[dim] *= pi/180
        r[dim] += va[dim]*dt
    #create rotational matrices and adjust positions accordingly
    Rx = np.array([[1, 0, 0], [0, cos(r[0]), -sin(r[0])], [0, sin(r[0]), cos(r[0])]]) #roll
    Ry = np.array([[cos(r[1]), 0, sin(r[1])], [0, 1, 0], [-sin(r[1]), 0, cos(r[1])]]) #pitch
    Rz = np.array([[cos(r[2]), -sin(r[2]), 0], [sin(r[2]), cos(r[2]), 0], [0, 0, 1]]) #yaw
    pos = Rx @ Ry @ Rz @ np.array([[dx[0]], [dx[1]], [dx[2]]])
    pos = pos.tolist()

    for dim in range(3):
        X[dim].append(X[dim][len(X[dim])-1] + pos[dim][0])
    

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title('drone position')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

ax.plot3D(X[0], X[1], X[2], 'red')
plt.show()
print(X)
plt.savefig('/home/aero/aero/ben_test/graph.png')
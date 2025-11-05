from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('/home/aero/aero/ben_test/data.csv')
A = [data['Ax'].tolist(), data['Ay'].tolist(), data['Az'].tolist()]
G = [data['Gx'].tolist(), data['Gy'].tolist(), data['Gz'].tolist()]

for i in range(len(A[0])):
    

#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.set_title('drone position')
#ax.set_xlabel('x axis')
#ax.set_ylabel('y axis')
#ax.set_zlabel('z axis')

#ax.plot3D(X[0], X[1], X[2], 'red')
#plt.show()
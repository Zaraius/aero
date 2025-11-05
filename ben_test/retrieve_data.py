import datetime
import csv
import os
from imu_test import IMU
from cam_test import CameraFootage
from graph_data import PositionGraph
from time import sleep
from matplotlib import pyplot as plt

dt = 0.5

imu = IMU()
imu.MPU_Init()

cap = CameraFootage()
cap.clear_folder()

graph = PositionGraph(dt)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title('drone position')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')


if os.path.isfile("/home/aero/ben_test/data.csv"):
	os.remove("/home/aero/ben_test/data.csv")

with open("/home/aero/ben_test/data.csv", 'w', newline='') as fp:
	csv.writer(fp).writerow(['Time', 'Photo', 'Ax', 'Ay', 'Az', 'Gx', 'Gy', 'Gz'])

print('collection started')
while True:
	try:
		time = datetime.datetime.now().strftime("%H:%M:%S:%f")
		
		[Ax, Ay, Az, Gx, Gy, Gz] = imu.read_data()
		X = graph.new_input(Ax, Ay, Az, Gx, Gy, Gz)

		imgName = cap.save_frame()
		with open("/home/aero/ben_test/data.csv", 'a', newline='') as f:
			csv.writer(f).writerow([time, imgName, Ax, Ay, Az, Gx, Gy, Gz])

		ax.plot3D(X[0], X[1], X[2], 'red')
		plt.show(block=False)
		plt.pause(0.001)

		sleep(dt)
	except KeyboardInterrupt:
		cap.stop_recording()
		break

print('\ncollection stopped')
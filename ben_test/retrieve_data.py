import datetime
import csv
import os
from imu_test import IMU
from cam_test import CameraFootage
from time import sleep

dt = 0.5

imu = IMU()
imu.MPU_Init()

cap = CameraFootage()
cap.clear_folder()


if os.path.isfile("/home/aero/aero/ben_test/data.csv"):
	os.remove("/home/aero/aero/ben_test/data.csv")

with open("/home/aero/aero/ben_test/data.csv", 'w', newline='') as fp:
	csv.writer(fp).writerow(['Time', 'Photo', 'Ax', 'Ay', 'Az', 'Gx', 'Gy', 'Gz'])

print('collection started')
while True:
	try:
		time = datetime.datetime.now().strftime("%H:%M:%S:%f")
		
		[Ax, Ay, Az, Gx, Gy, Gz] = imu.read_data()

		imgName = cap.save_frame()
		with open("/home/aero/aero/ben_test/data.csv", 'a', newline='') as f:
			csv.writer(f).writerow([time, imgName, Ax, Ay, Az, Gx, Gy, Gz])

		sleep(dt)

	except KeyboardInterrupt:
		cap.stop_recording()
		break

print('\ncollection stopped')
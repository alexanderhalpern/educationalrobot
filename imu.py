# from microbit import *
# from mpu9250 import MPU9250
# from mpu9250 import MPU9250
# imu = MPU9250('X')

# while True:

#     print(imu.accel.xyz)
#     print(imu.gyro.xyz)
#     print(imu.mag.xyz)
#     print(imu.temperature)
#     print(imu.accel.z)

#     sleep(1000)
from MPU6050_Unified import sleep_ms
from MPU6050 import MPU6050

# Example code for PiicoDev Motion Sensor MPU6050
# Cross-platform compatible sleep function


motion = PiicoDev_MPU6050()

while True:

    # Accelerometer data
    accel = motion.read_accel_data()  # read the accelerometer [ms^-2]
    aX = accel["x"]
    aY = accel["y"]
    aZ = accel["z"]
    print("x:" + str(aX) + " y:" + str(aY) + " z:" + str(aZ))

    # Gyroscope Data
#     gyro = motion.read_gyro_data()   # read the gyro [deg/s]
#     gX = gyro["x"]
#     gY = gyro["y"]
#     gZ = gyro["z"]
#     print("x:" + str(gX) + " y:" + str(gY) + " z:" + str(gZ))

    # Rough temperature
#     temp = motion.read_temperature()   # read the device temperature [degC]
#     print("Temperature: " + str(temp) + "°C")

    # G-Force
#     gforce = motion.read_accel_abs(g=True) # read the absolute acceleration magnitude
#     print("G-Force: " + str(gforce))

    sleep_ms(100)

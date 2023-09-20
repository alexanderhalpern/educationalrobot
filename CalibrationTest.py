from microbit import *
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
from PiicoDev_Unified import sleep_ms
from PiicoDev_MPU6050 import PiicoDev_MPU6050

# Example code for Motion Sensor MPU6050
# Cross-platform compatible sleep function


motion = PiicoDev_MPU6050()


def calibrate_accelerometer():

    display.scroll("Calibrating...", delay=50)

    raw_data = []
    samples = 100
    for i in range(samples):
        accel = motion.read_accel_data()
        raw_data.append(accel)
        sleep_ms(int(1000/samples))

    accel_cal_values = {}
    accel_cal_values['x'] = -1 * (sum([val["x"] for val in raw_data]) / samples)
    accel_cal_values['y'] = -1 * (sum([val["y"] for val in raw_data]) / samples)
    accel_cal_values['z'] = 9.81 - (sum([val["z"] for val in raw_data]) / samples)
    print("Adjusting acceleromter using the following constants:", accel_cal_values)

    return accel_cal_values

def calibrate_gyro():
    display.scroll("Calibrating...", delay=50)

    raw_data = []
    samples = 100
    for i in range(samples):
        accel = motion.read_gyro_data()
        raw_data.append(accel)
        sleep_ms(int(1000/samples))

    gyro_cal_values = {}
    gyro_cal_values['x'] = -1 * (sum([val["x"] for val in raw_data]) / samples)
    gyro_cal_values['y'] = -1 * (sum([val["y"] for val in raw_data]) / samples)
    gyro_cal_values['z'] = -1 * (sum([val["z"] for val in raw_data]) / samples)
    print("Adjusting gyro using the following constants:", gyro_cal_values)

    return gyro_cal_values
    


calibrate_accelerometer()
calibrate_gyro()

while False:

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


# from microbit import *

# sleep(1000)

# print("Hello Terminal!")

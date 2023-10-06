from microbit import *
import radio
import time
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
# pin1=left
# pin2=right

# controlling distance with time
forwardreverseTime = 1450
turnTime = 700
# servo motor compensation:
# 1.0 = 100% C
# 1.1 = 80% C
# ...
# 1.5 = 0% STOPPED
# ...
# 1.9 = 80% CC
# 2.0 = 100% CC
pin1Comp = 0.0
pin2Comp = 0.125
# 50Hz to 20 ms pulse
pin1.set_analog_period(20)
pin2.set_analog_period(20)

# rotationSquare = 0.769148546224 #35.5*pi/145 = rev  |  35.5mm wheel dia, 145mm distance of mat

# specific motor control functions


def stop():
    pin1.write_analog(0)
    pin2.write_analog(0)
    # display.show(stopSign)
    # sleep(1000)


def forward(left, right):
    pin1.write_analog(1023 * (left-pin1Comp) / 20)
    pin2.write_analog(1023 * (right+pin2Comp) / 20)
    # display.show(Image.ARROW_N)
    # sleep(forwardreverseTime)  # one tire revolution
    # stop()


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
    accel_cal_values['x'] = -1 * \
        (sum([val["x"] for val in raw_data]) / samples)
    accel_cal_values['y'] = -1 * \
        (sum([val["y"] for val in raw_data]) / samples)
    accel_cal_values['z'] = 9.81 - \
        (sum([val["z"] for val in raw_data]) / samples)
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


accel_cal_values = calibrate_accelerometer()
gyro_cal_values = calibrate_gyro()
start = time.ticks_ms()
global_time_start = time.ticks_ms()
acceleration_buffer = []
velocity_buffer = []
time_delta = 1 * 50  # t secs * 1000 ms
mode = 0
(vX, vY) = (0, 0)
(pX, pY) = (0, 0)
counter = 0
while True:

    accel = motion.read_accel_data()  # read the accelerometer [ms^-2]
    aX = accel["x"] + accel_cal_values['x']
    aY = accel["y"] + accel_cal_values['y']
    aZ = accel["z"] + accel_cal_values['z']

    aX, aY, aZ = float('%.2f' % aX), float('%.2f' % aY), float('%.2f' % aZ)

    print(aX, aY, aZ)
    acceleration_buffer.append((aX, aY))
    # if counter % 20 == 0:
    # print("X accel", accel["x"], "Y accel",
    #       accel["y"], "Z accel", accel["z"])

    if len(acceleration_buffer) >= 2:
        print("acceleration buffer", acceleration_buffer,
              "vX:" + '%.2f' % vX + " vY:" + '%.2f' % vY)
        if velocity_buffer:
            print("compare", vX, velocity_buffer[-1][0])
        vX += (
            (acceleration_buffer[-1][0] + acceleration_buffer[-2][0]) / 2) * (time_delta / 1000)
        vY += (
            (acceleration_buffer[-1][1] + acceleration_buffer[-2][1]) / 2) * (time_delta / 1000)

        acceleration_buffer.pop(0)
        velocity_buffer.append((float('%.2f' % vX), float('%.2f' % vY)))
        # if counter % 20 == 0:
        #     print("vX:" + str(vX) + " vY:" + str(vY))

    if len(velocity_buffer) >= 2:
        print("velocity_buffer", velocity_buffer, "pX:" + '%.2f' %
              pX + " pY:" + '%.2f' % pY)
        pX += ((velocity_buffer[-1][0] +
                velocity_buffer[-2][0]) / 2) * (time_delta / 1000)
        pY += ((velocity_buffer[-1][1] +
                velocity_buffer[-2][1]) / 2) * (time_delta / 1000)
        pX, pY = float('%.2f' % pX), float('%.2f' % pY)
        velocity_buffer.pop(0)
        # if counter % 20 == 0:
        # print()

    # print("x:" + str(aX) + " y:" + str(aY) + " z:" + str(aZ))
    radio.send(("x:" + str(aX)[0:5] + " y:" +
               str(aY)[0:5] + " z:" + str(aZ)[0:5]))

    sleep_ms(time_delta)
    counter += 1

# from microbit import *
# from mpu9250 import MPU9250


# rightButton = pin15

# rightButton.set_pull(rightButton.PULL_UP)

# imu = MPU9250('X')
# print(imu.accel.xyz)
# print(imu.gyro.xyz)
# print(imu.mag.xyz)
# print(imu.temperature)
# print(imu.accel.z)

# while True:
#     if rightButton.read_digital() == 0:
#         display.show(Image.HAPPY)
#         sleep(5000)
#     else:
#         display.show(Image.SAD)


# print_to_terminal.py

from microbit import *

sleep(1000)

print("Hello Terminal!")



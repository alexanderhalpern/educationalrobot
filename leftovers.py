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


# from microbit import *

# sleep(1000)

# print("Hello Terminal!")



    # Accelerometer data
    # if time.ticks_diff(time.ticks_ms(), start) > 5000:
    #     start = time.ticks_ms()
    #     mode = (mode + 1) % 3
    # if mode == 0:
    #     forward(2.0, 1.0)
    # if mode == 1:
    #     forward(2.0, 1.3)
    # if mode == 2:
    #     stop()
    # print(time.ticks_diff(time.ticks_ms(), start))

        if velocity_buffer:
            print("compare", vX, velocity_buffer[-1][0])
                    print("acceleration buffer", acceleration_buffer,
              "vX:" + '%.2f' % vX + " vY:" + '%.2f' % vY)
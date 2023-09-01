from microbit import *
import radio
radio.on()
while True:
    res = radio.receive()
    if res:
        print(res)

    sleep(10)

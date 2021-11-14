import utime
from machine import Pin, Timer

utime.sleep(1)
uart = machine.UART(1, 115200)
utime.sleep(1)

def ultra(trigger_pin, echo_pin):
    trigger = Pin(trigger_pin, Pin.OUT)
    echo = Pin(echo_pin, Pin.IN)
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    while echo.value() == 0:
        signaloff = utime.ticks_us()

    while echo.value() == 1:
        signalon = utime.ticks_us()

    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

def return_distance(t):
    distance1 = ultra(3, 2)
    distance2 = ultra(20, 21)
    # print(f"front,{distance1},rear,{distance2}\n")
    uart.write(f"front,{distance1},rear,{distance2}\n")
    # print(distance)

timer = Timer()
timer.init(freq=10, mode=Timer.PERIODIC, callback=return_distance)

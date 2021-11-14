import sys

sys.path.append("..")

import time

from Motor.bot_motor import BotMotorController

motorcontroller = BotMotorController(default_speed=70, max_speed=100)
motorcontroller.add_motor("Motor1", 13, 19, 26, True, True, 1000)
motorcontroller.add_motor("Motor2", 17, 27, 22, True, False, 1000)
motorcontroller.start_motor()
motorcontroller.car_move_forwards()
time.sleep(1.0)

motorcontroller.car_move_backwards()
time.sleep(1.0)

motorcontroller.car_move_left()
time.sleep(1.0)

motorcontroller.car_move_right()
time.sleep(1.0)

motorcontroller.car_move_backwards_right()
time.sleep(1.0)

motorcontroller.car_move_backwards_left()
time.sleep(1.0)

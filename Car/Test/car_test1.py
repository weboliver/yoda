import sys

sys.path.append("..")

import time

from Automation.automation import Automation
from Automation.automation_programs import AutomationPrograms
from car import Car
from Motor.bot_motor import BotMotorController
from Sensors.ultrasonic import UltraSonic

sensor_object = UltraSonic()
programs = AutomationPrograms()
selfDriving = Automation(programs)
selfDriving.add_sensor("UltraSonic", sensor_object)

motorcontroller = BotMotorController(default_speed=45, max_speed=100)
motorcontroller.add_motor("Motor1", 19, 13, 26, True, True, 50)
motorcontroller.add_motor("Motor2", 27, 17, 22, True, False, 50)

newcar = Car("Lukes Car", motorcontroller, None, selfDriving)

newcar.start()
newcar.drive("autoprogram_one")

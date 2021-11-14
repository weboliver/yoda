import threading
import time

import RPi.GPIO as GPIO

from Motor.motor import MotorController


class Car:
    def __init__(self, name, motor: MotorController, controller = None, automation = None):
        self._name = name
        self._stopped = False
        self._motorengine = motor
        self._controller = controller
        self._motorevents = {}
        self._automation = automation
        automation.set_car(self)
    
    def get_name(self):
        return self._name

    def get_controller(self):
        return self._controller

    def get_automation(self):
        return self._automation

    def start(self):
        self._stopped = False
        self.get_motorengine().start_motor()

    def get_motorengine(self):
        return self._motorengine

    def motorevents(self):
        pass

    def get_sensors(self):
        if self._automation:
            return self._automation.get_sensors()

    def get_automation_controller(self):
        return self._automation

    def get_automation_service(self, program_name: str):
        if self._automation:
            driving_controller = self.get_automation_controller()
            driving_controller.autoprogram(program_name)

    def handleevent(self, actionevent):
        motor = self.get_motorengine()
        if actionevent["action"] == "forward":
            motor.car_move_forwards()
        elif actionevent["action"] == "backwards":
            motor.car_move_backwards()
        elif actionevent["action"] == "stop":
            motor.stop()
        elif actionevent["action"] == "startmotor":
            motor.start_motor()
        elif actionevent["action"] == "stopmotor":
            motor.stop()
        elif actionevent["action"] == "leftspin":
            motor.car_spin_left()
        elif actionevent["action"] == "rightspin":
            motor.car_spin_right()
        elif actionevent["action"] == "backwards_and_right_spin":
            motor.car_move_backwards(duration = actionevent["value"][1])
            motor.car_move_right(duration = actionevent["value"][0])
        elif actionevent["action"] == "forward_and_left_spin":
            motor.car_move_forwards(duration = actionevent["value"][1])
            motor.car_move_left(duration = actionevent["value"][0])
        elif actionevent["action"] == "leftslide":
            motor.car_slide_left()
        elif actionevent["action"] == "rightslide":
            motor.car_slide_right()
        elif "autoprogram" in actionevent["action"]:
            self.get_automation_service(actionevent["action"])
        else:
            motor.stop()

    def stop(self):
        self._stopped = True
        self.get_motorengine().stop()
    
    def drive(self, automation_program: str = None):
        if self._stopped:
            return
        self.thread = threading.Thread(target=self._drive(automation_program))
        print("starting thread")
        self.thread.start()


    def _drive(self, automation_program: str = None):
        controller = self.get_controller()
        automation = self.get_automation()
        if (controller and controller.get_device()) or automation:
            while True:
                time.sleep(0.05)
                try:
                    auto_program = None
                    if automation_program:
                        auto_program = automation_program
                    if automation and auto_program:
                        actionevent = automation.autoprogram(auto_program)
                        if actionevent:
                            self.handleevent(actionevent)
                    if controller:
                        actionevent = controller.get_action()
                        if actionevent:
                            self.handleevent(actionevent)

                except:
                    print("Ending Controller ..")
                    GPIO.cleanup()
                    break
        else:
            print("No X-Box Controller found ..")

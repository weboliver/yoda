from Automation.automation_events import AutomationEvents


# Umbenennen in Automation
class Automation:
    def __init__(self, programs = None):
        self._eventController = AutomationEvents()
        self._sensors = {}
        self._programs = programs
        self.get_programs().set_event_controller(self.get_event_controller())
        self._car = None

    def set_car(self, car):
        self.get_programs().set_car(car)
        self._car = car

    def get_car(self):
        return self._car

    def get_event_controller(self):
        return self._eventController

    def add_sensor(self, sensor_name, sensor_object):
        self._sensors[sensor_name] = sensor_object

    def get_sensors(self):
        return self._sensors

    def get_programs(self):
        return self._programs

    def autoprogram(self, program_name):
        result = {}
        if self.get_programs():
            if program_name == "autoprogram_one":
                result = self.get_programs().program_one()
            if program_name == "autoprogram_stop":
                result = self.get_programs().program_stop()
        return result
            

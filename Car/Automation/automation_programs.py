from Automation.automation_events import AutomationEvents


class AutomationPrograms:

    def __init__(self):
        self._car = None

    def set_car(self, car):
        self._car = car

    def get_car(self):
        return self._car

    def set_event_controller(self, event_controller: AutomationEvents):
        self._event_controller = event_controller

    def get_event_controller(self):
        return self._event_controller

    def get_sensors(self):
        return self.get_car().get_sensors()

    def program_one(self):
        result = {}
        sensors = self.get_sensors()
        eventcontroller = self._event_controller
        
        for sensor_name in sensors:
            sensor_result = sensors[sensor_name].read_one()
            result[sensor_name] = sensor_result
        
        event = eventcontroller.find_event("FORWARD", "MOVE")
        try:
            if result["UltraSonic"]["front"] >= 35:
                event = eventcontroller.find_event("FORWARD", "MOVE")
            elif result["UltraSonic"]["front"] < 35:
                event = eventcontroller.find_event("KOLLISIONFRONT", "OBSTACLE")
            elif result["UltraSonic"]["rear"] >= 35:
                event = eventcontroller.find_event("BACKWARD", "MOVE")
            elif result["UltraSonic"]["rear"] < 35:
                event = eventcontroller.find_event("KOLLISIONBACK", "OBSTACLE")
        except:
            pass

        result = event
        # result["events"] = eventcontroller.get_events()

        return result

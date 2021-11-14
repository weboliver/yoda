class AutomationEvents():
    def __init__(self):
        self._events = {}
        self.init_events()

    def add_event(self, name, typeofevent, code, type_id, value, action):
        eventkey = f"KEY_{name}_{typeofevent}"
        self._events[eventkey] = {}
        self._events[eventkey]["name"] = name
        self._events[eventkey]["typeofevent"] = typeofevent
        self._events[eventkey]["code"] = code
        self._events[eventkey]["type_id"] = type_id
        self._events[eventkey]["value"] = value
        self._events[eventkey]["action"] = action


    def init_events(self):
        self.add_event("FORWARD", "MOVE", 1, 1, 0.05, "forward")
        self.add_event("BACKWARD", "MOVE", 2, 1, 0.05, "backwards")
        self.add_event("LEFT", "MOVE", 3, 1, 0.05, "leftspin")
        self.add_event("RIGHT", "MOVE", 4, 1, 0.05, "rightspin")
        self.add_event("LEFTBACK", "MOVE", 5, 1, 0.05, "leftspinback")
        self.add_event("RIGHTBACK", "MOVE", 6, 1, 0.05, "rightspinback")
        self.add_event("KOLLISIONFRONT", "OBSTACLE", 7, 20, [0.5,1.0], "backwards_and_right_spin")
        self.add_event("KOLLISIONBACK", "OBSTACLE", 8, 20, [0.5,1.0], "forward_and_left_spin")

    def get_events(self):
        return self._events

    def find_event(self, event_name, event_key):
        all_events = self.get_events()
        eventkey = f"KEY_{event_name}_{event_key}"
        if eventkey in all_events:
            return all_events[eventkey]
        return None



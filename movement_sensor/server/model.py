
class MovementSensorModel(object):
    def set_last_activity(self):
        pass

    def get_last_activity(self):
        pass

    def set_mode(self, mode):
        pass

    def set_sleep_mode(self):
        self.set_mode("S")

    def get_mode(self):
        pass

    def save_movement_time(self, time):
        pass
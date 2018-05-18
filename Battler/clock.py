import time

class Clock():
    def __init__(self):
        self.start_game = time.time()

    def duration_of_games(self):
        current_time = time.time()
        duration = current_time - self.start_game
        return duration

    @staticmethod
    def set_time(recharge):
        return time.time() + recharge

    @staticmethod
    def is_time(time_recharge):
        current_time - time.time()
        delta = current_time - time_recharge
        if delta >= 0:
            return True
        else:
            return False            
import time

class Clock():
    def __init__(self):
        self.start_game = time.time()

    def duration_of_games(self):
        current_time = time.time()
        duration = time.strftime("%H:%M:%S", time.gmtime(current_time - self.start_game))
        return duration


def set_time(recharge):
    return time.time() + recharge


def is_time(time_recharge):
    current_time = time.time()
    delta = current_time - time_recharge
    return True if delta >= 0 else False

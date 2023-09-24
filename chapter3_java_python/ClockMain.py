class ClockMain:

    def __init__(self, hour, minutes, second):
        self._hour = hour
        self._second = second
        self._minutes = minutes

    def set_hour(self, hour):
        if hour < 24:
            self._hour = hour

    def get_hour(self):
        return self._hour

    def set_minutes(self, minutes):
        if minutes < 59:
            self._minutes = minutes

    def get_minutes(self):
        return self._minutes

    def set_second(self, second):
        if second < 59:
            self._second = second

    def get_second(self):
        return self._second

    def display_time(self):
        return f'{self._hour}:{self._minutes}:{self._second}'

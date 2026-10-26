# Event class definition and inherited subclasses
from datetime import date as date_type, time as time_type

class Event:

    def __init__(self, name, date, topic):
        self.name = name
        self.topic = topic

        if isinstance(date, date_type):
            self.date = date
        else: raise TypeError("date must be datetime.date object")


class AllDayEvent(Event):

    def __init__(self, name, date, topic):
        super().__init__(name, date, topic)

class TimedEvent(Event):

    def __init__(self, name, date, topic, time, duration, location):
        super().__init__(name, date, topic)
        self.duration = duration
        self.location = location

        if isinstance(time, time_type):
            self.time = time
        else: raise TypeError("time must be datetime.time object")
        

class Deadline(Event):

    def __init__(self, name, date, topic, time):
        super().__init__(name, date, topic)

        if isinstance(time, time_type):
            self.time = time
        else: raise TypeError("time must be datetime.time object")
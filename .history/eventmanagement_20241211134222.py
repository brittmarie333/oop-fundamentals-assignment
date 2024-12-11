#Extend an existing Event class by adding a feature to keep track of the number of participants.

# Code Example: Basic Event class without participant tracking.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date


#Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
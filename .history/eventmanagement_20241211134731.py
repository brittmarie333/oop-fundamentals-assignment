#Extend an existing Event class by adding a feature to keep track of the number of participants.

# Code Example: Basic Event class without participant tracking.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

#Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
    
    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count
    
event = Event("Christmas Party", "12/14/2025")

#add participants
event.add_participant("Brittany Pitts")
event.add_participant("Ronald Waters")
event.add_participant("Prince Eddis")

print("Your RSVPS are coming in! The following will be attending the party ")
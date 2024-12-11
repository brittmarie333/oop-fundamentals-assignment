#Extend an existing Event class by adding a feature to keep track of the number of participants.

# Code Example: Basic Event class without participant tracking.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []  # List to store participant names

    def add_participant(self, participant_name):
        """Add a participant to the event."""
        self.participants.append(participant_name)

    def get_participant_count(self):
        """Return the current number of participants."""
        return len(self.participants)

    def get_participant_list(self):
        """Return the list of participants."""
        return self.participants

event = Event("Christmas Party", "12/14/2025")

# Add participants
event.add_participant("Brittany")
event.add_participant("Ronald")
event.add_participant("Prince")

print("Your RSVPs are coming in! The following will be attending the party: \n", event.get_participant_list())
print(f"Total participants: {event.get_participant_count()}")


class EventLogger:
    def __init__(self):
        self.events = []

    def log(self,event_type,**data):
        self.events.append({
            "type":event_type,
            **data
        })

    def clear(self):
        self.events=[]

    def get_events(self):
        return self.events
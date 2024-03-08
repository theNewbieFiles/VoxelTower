import uuid

class EventSystem: 
    
    def __init__(self) -> None:
        self.subscribers = dict()
    
    def on(self, event_name: str, callback):
        subscriber_id = uuid.uuid4()
        
        if not event_name in self.subscribers:
            self.subscribers[event_name] = []; 
        self.subscribers[event_name].append((subscriber_id, callback))
        
        return subscriber_id
    
    def remove(self, event_name:str, subcriber_id):
        if not event_name in self.subscribers: 
            return
        newList = []
        
        for sid, fn in self.subscribers[event_name]: 
            if sid != subcriber_id:
                newList.append((sid, fn))
        
        self.subscribers[event_name] = newList
        
        
    def broadcast(self, event_name: str, data):
        if not event_name in self.subscribers: 
            return
        for sid, fn in self.subscribers[event_name]: 
            fn(data)
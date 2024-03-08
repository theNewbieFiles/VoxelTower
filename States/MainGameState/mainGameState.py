from stateManagement.baseState import BaseState
from eventSystem.EventSystem import EventSystem
from settings import * 
from consts import *
    
    
class MainGameState(BaseState):
    def __init__(self, eventSystem: EventSystem, state) -> None:
        super().__init__()
        self.eventSystem = eventSystem   
        self.state = state
        
        self.time = 0
    
    def update(self):
        print("__Main Game__")
        
        self.time = testClock(self.time)
        
        if self.time > 10:
            self.eventSystem.broadcast(QUIT, None)
    
    def render(self):
        ...
        
        
        
        
def testClock(time):
    time += 1
    return time 
from stateManagement.baseState import BaseState
from eventSystem.EventSystem import EventSystem
from settings import * 
from consts import *


class InitLoadState(BaseState):
    
    def __init__(self, eventSystem: EventSystem) -> None:
        super().__init__()
        self.eventSystem = eventSystem
        self.timer = 0
    
    def update(self):
        print("updating...")
        self.timer += 1
        
        if self.timer >= 10:
            self.eventSystem.broadcast(INITALIALIZING_DONE, None)
        

        
    


    def render(self):
        print("rendering initload")
    
    
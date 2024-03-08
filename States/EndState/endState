from stateManagement.baseState import BaseState
from eventSystem.EventSystem import EventSystem
from settings import * 
from consts import *

class EndState(BaseState):
    def __init__(self, eventSystem: EventSystem, state) -> None:
        super().__init__()
        self.eventSystem = eventSystem   
        self.state = state

    def update(self):
        print("End_State")
        self.eventSystem.broadcast(QUIT, None)
    
    def render(self):
        ...
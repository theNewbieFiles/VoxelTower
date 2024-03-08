from stateManagement.baseState import BaseState
from eventSystem.EventSystem import EventSystem
from settings import * 
from consts import *

class LoadGameState(BaseState):
    
    def __init__(self, eventSystem: EventSystem, state) -> None:
        super().__init__()
        self.eventSystem = eventSystem


    def update(self):
        print("Loading Game State")
        self.eventSystem.broadcast(MAIN_LOADING_DONE, None)
        
    def render(self):
        ...

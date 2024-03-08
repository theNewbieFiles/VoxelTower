from stateManagement.baseState import BaseState
from eventSystem.EventSystem import EventSystem
from settings import * 
from consts import *


from consts import *

class MainMenuState(BaseState):
    
    def __init__(self, eventSystem: EventSystem) -> None:
        super().__init__()
        self.eventSystem = eventSystem
    
    def update(self):
        print("Main Menu")
        self.eventSystem.broadcast(MAIN_LOADING_STARTING, None)
        
    

    def render(self):
        ...
    

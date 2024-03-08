from consts import * 
from eventSystem.EventSystem import EventSystem
from .baseState import BaseState

#states
from States.InitLoadState.initLoadState import InitLoadState
from States.MainMenuState.mainMenuState import MainMenuState
from States.LoadGameState.loadGameState import LoadGameState
from States.MainGameState.mainGameState import MainGameState
from States.EndState.endState import Endstate

class StateManager:
    
    def __init__(self, eventSystem: EventSystem) -> None:
        self.eventSystem = eventSystem
        self.currentState = BaseState()
        
        #events to listen too
        self.eventSystem.on(PROCESS_STARTED, self.processStarting)
        self.eventSystem.on(INITALIALIZING_DONE, self.mainMenu)
        self.eventSystem.on(MAIN_LOADING_STARTING, self.loadGameState)
        self.eventSystem.on(MAIN_LOADING_DONE, self.mainGameState)
        self.eventSystem.on(ENDING_CREDITS_ENTERING, self.endState)
    
    
    def processStarting(self, data):
        self.currentState = InitLoadState(self.eventSystem)
        
        
    def mainMenu(self, data):
        self.currentState.exiting()
        self.currentState = MainMenuState(self.eventSystem)
        
    def loadGameState(self, data):
        self.currentState.exiting()
        self.currentState = LoadGameState(self.eventSystem, data)
        
    def mainGameState(self, data):
        self.currentState.exiting()
        self.currentState = MainGameState(self.eventSystem, data)
    
    def pauseState(self, data):
        ...

    def endState(self,data):
        self.currentState.exiting()
        self.currentState = Endstate(self.eventSystem, data)
        
    #end state added
    
    def update(self):
        self.currentState.preUpdate()
        self.currentState.update()
        self.currentState.postUpdate()
        
    def render(self):
        
        self.currentState.render()
        self.currentState.postRender()


class BaseState:
    
    def __init__(self) -> None:
        pass
    
    def initialize(self):
        ...
    
    def entering(self):
        ...
    
    def preUpdate(self): 
        ...
    
    def update(self): 
        ...
    
    def postUpdate(self): 
        ...
    
    def render(self): 
        ...
    
    def postRender(self):
        ...
    
    def exiting(self): 
        ...
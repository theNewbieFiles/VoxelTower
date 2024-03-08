from eventSystem.EventSystem import EventSystem
from stateManagement.stateManager import StateManager
from settings import * 
from app import App

def main():
    # Do any initial setup that might be needed here
    eventSystem = EventSystem()
    stateManager = StateManager(eventSystem)

    app = App(eventSystem, stateManager)
    
    print("ready to go...")
    app.start()
    
    
    

    
    

# Check if the script is being run as the main program
if __name__ == "__main__":
    # If so, call the main function
    main()
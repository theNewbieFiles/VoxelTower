import settings
import sys
import pygame as pg
import moderngl as mgl
import consts

from settings import *
from consts import * 
from stateManagement.stateManager import StateManager
from eventSystem.EventSystem import EventSystem

class App:
    def __init__(self, eventSystem: EventSystem, stateManager: StateManager) -> None:
        self.eventSystem = eventSystem
        self.stateManager = stateManager
        self.running = True
        
        #pygame
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)
        pg.display.set_mode(settings.WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        
        #context for opengl
        self.ctx = mgl.create_context()
        
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        
        self.ctx.gc_mode = 'auto'
        
        #events
        self.eventSystem.on(QUIT, self.end)
        
        self.eventSystem.broadcast(PROCESS_STARTED, None)
        
        
        self.start()
        
    def start(self):
        
        while self.running:
            
            self.stateManager.update()
            self.stateManager.render()
        
        
        
    def end(self, data):
        print("Quiting")
        sys.exit()
        



# def App(state): 
#     pg.init()
#     pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
#     pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
#     pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
#     pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)
#     pg.display.set_mode(settings.WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
    
#     #context for opengl
#     ctx = mgl.create_context()
    
#     ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
    
#     ctx.gc_mode = 'auto'
    
    
    
    
#     State = {}
#     stateFunction = Initalize_InitLoadState(State, [])
    
#     running = True
    
#     while running:
#         events = pg.event.get()
#         for event in events:
#             if event.type == pg.QUIT:
#                 running = False

#         stateFunction = stateFunction()
        
#         ctx.clear(color=BG_COLOR)
#         pg.display.flip()
        
        
#     #no longer in the loop, exit the program
#     pg.quit()
#     sys.exit()
    

# def input(events, State):
#     ...
    
        


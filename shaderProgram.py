



#This will load the vertex and fragment shader programs
def getProgram(shaderName, ctx):
    with open(f'shaders/{shaderName}.vert') as file: 
        vertexShader = file.read()
        
    with open(f'shaders/{shaderName}.frag') as file: 
        fragmentShader = file.read()
        
    #this compiles the shaders    
    return ctx.program(vertex_shader=vertexShader, fragment_shader=fragmentShader)
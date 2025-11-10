import imgui
import glfw
import OpenGL.GL as gl
from imgui.integrations.glfw import GlfwRenderer

def init():
    global window
    global renderer
    
    if not glfw.init():
        print("Could not initialize OpenGL context")
        exit(1)

    # OS X supports only forward-compatible core profiles from 3.2
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(1280, 720, "My editor", None, None)
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print("Could not initialize Window")
        exit(1)


    gl.glClearColor(*(0,0,0,1))
    imgui.create_context()
    renderer = GlfwRenderer(window)
    
def should_close():
    return glfw.window_should_close(window)


def update_begin():
    glfw.poll_events()
    renderer.process_inputs()
    imgui.new_frame()

def update_end():
    imgui.render()
    gl.glClearColor(*(0,0,0,1))
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    renderer.render(imgui.get_draw_data())
    glfw.swap_buffers(window)
    
def finish():
    renderer.shutdown()
    glfw.terminate()
    


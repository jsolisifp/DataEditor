import imgui
import glfw
import OpenGL.GL as gl
from imgui.integrations.glfw import GlfwRenderer


class ImguiUtils:
    
    window = None
    renderer = None
    
    @classmethod
    def init(cls):
        
        if not glfw.init():
            print("Could not initialize OpenGL context")
            exit(1)
    
        # OS X supports only forward-compatible core profiles from 3.2
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)
    
        # Create a windowed mode window and its OpenGL context
        cls.window = glfw.create_window(1280, 720, "My editor", None, None)
        glfw.make_context_current(cls.window)
    
        if not ImguiUtils.window:
            glfw.terminate()
            print("Could not initialize Window")
            exit(1)
    
    
        gl.glClearColor(*(0,0,0,1))
        imgui.create_context()
        cls.renderer = GlfwRenderer(cls.window)
        
    @classmethod
    def should_close(cls):
        return glfw.window_should_close(cls.window)
    
    
    @classmethod
    def update_begin(cls):
        glfw.poll_events()
        cls.renderer.process_inputs()
        imgui.new_frame()
    
    @classmethod
    def update_end(cls):
        imgui.render()
        gl.glClearColor(*(0,0,0,1))
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        cls.renderer.render(imgui.get_draw_data())
        glfw.swap_buffers(ImguiUtils.window)
        
    @classmethod
    def finish(cls):
        cls.renderer.shutdown()
        glfw.terminate()
    


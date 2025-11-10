import imgui
from imgui_utils import ImguiUtils


class DataEditor:
    
    
    def __init__(self):
        
        # Inicialización del programa

        self.file_loaded = False
        self.file_contents = []
        self.help_visible = False

        self.line_selected_index = 0

    def Init(self):
        
        ImguiUtils.init()

    def ShouldClose(self):
        
        return ImguiUtils.should_close();
    
    def Update(self):
        
        ImguiUtils.update_begin()
        
        # Main menu bar
        
        if imgui.begin_main_menu_bar():
            
            if imgui.begin_menu("File"):
                
                if imgui.menu_item("New")[0]:
                    print("New clicked")
                    
                if imgui.menu_item("Open")[0]:
                    print("Open clicked")
                    file = open("documento.csv", "r")
                    self.file_contents = file.readlines()
                    file.close()
                    self.file_loaded = True
    
                if imgui.menu_item("Save", enabled = self.file_loaded)[0]:
                    print("Save clicked")
                    file = open("documento.csv", "w")
                    file.writelines(self.file_contents)
                    file.close()
    
                if imgui.menu_item("Close", enabled = self.file_loaded)[0]:
                    self.file_loaded = False
                    print("Close clicked")
    
                if imgui.menu_item("Exit")[0]:
                    print("Exit clicked")
    
                imgui.end_menu()
                
            if imgui.begin_menu("Edit"):
                
                if imgui.menu_item("Cut")[0]:
                    print("Cut clicked")
                    
                if imgui.menu_item("Copy")[0]:
                    print("Copy clicked")
    
                if imgui.menu_item("Paste")[0]:
                    print("Paste clicked")
    
                if imgui.menu_item("Delete")[0]:
                    print("Delete clicked")
    
                imgui.end_menu()            
            
            if imgui.begin_menu("Help"):
                
                if imgui.menu_item("Show help")[0]:
                    self.help_visible = True
                    print("Show help")
                    
                    
                imgui.end_menu()
            
            imgui.end_main_menu_bar()
        
        # Ventanas
        
        if self.file_loaded:
            imgui.begin("Document")
            _, self.line_selected_index = imgui.listbox("File contents", self.line_selected_index, self.file_contents, 100)
            imgui.end()
    
        if self.help_visible:
            self.help_visible = imgui.begin("Help", True)[1]
            imgui.text("This is a simple text lines editor by\n"
                       "By José Manuel Solís\n")
            imgui.end()
            
        if self.file_loaded:
            imgui.begin("Line tool")
            
            if self.line_selected_index > 0:
                if imgui.button("Move up"):            
                    self.file_contents.insert(self.line_selected_index - 1, self.file_contents.pop(self.line_selected_index))
                    self.line_selected_index -= 1
            if self.line_selected_index < len(self.file_contents) - 1:
                if imgui.button("Move down"):
                    self.file_contents.insert(self.line_selected_index + 1, self.file_contents.pop(self.line_selected_index))
                    self.line_selected_index += 1
            if len(self.file_contents) >= 1:
                if imgui.button("Delete"):
                    self.file_contents.pop(self.line_selected_index)
            if len(self.file_contents) >= 1:
                if imgui.button("Duplicate"):
                    line_to_duplicate = self.file_contents[self.line_selected_index]
                    self.file_contents.insert(self.line_selected_index + 1, line_to_duplicate)
            
            imgui.end()
    
    
        # Actualizar la UI aquí
        
        ImguiUtils.update_end()
    
    def Finish(self):
        ImguiUtils.finish()





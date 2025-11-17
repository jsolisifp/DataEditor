import imgui
from imgui_utils import ImguiUtils


class App:
    
    
    def __init__(self):
        
        # Inicialización del programa

        self.document_opened = False
        self.document_loaded = False
        self.document_file_name = ""
        self.help_visible = False
        self.paste_available = False 
        self.open_file_popup = False
        self.popup_file_not_exists = False

    def Init(self):
        
        ImguiUtils.init()
        
        self.OnInit()

    def ShouldClose(self):
        
        return ImguiUtils.should_close();
    
    def Update(self):
        
        ImguiUtils.update_begin()
        
        # Main menu bar
        
        if imgui.begin_main_menu_bar():
            
            if imgui.begin_menu("File"):
                
                if imgui.menu_item("New")[0]:
                    self.OnNew()
                    self.document_loaded = False
                    self.document_opened = True
                    
                if imgui.menu_item("Open")[0]:
                    self.open_file_popup = True
    
                if imgui.menu_item("Save", enabled = self.document_loaded)[0]:
                    self.OnSave()
    
                if imgui.menu_item("Close", enabled = self.document_opened)[0]:
                    self.OnClose()
                    self.document_loaded = False
                    self.document_opened = False
    
                if imgui.menu_item("Exit")[0]:
                    self.OnExit()
    
                imgui.end_menu()
                
            if imgui.begin_menu("Edit"):
                
                edit_enabled = self.document_opened and self.HasSelection()
                paste_enabled = self.document_opened and self.paste_available
                
                if imgui.menu_item("Cut", enabled = edit_enabled)[0]:
                    self.OnCut()
                    self.paste_available = True
                    
                if imgui.menu_item("Copy", enabled = edit_enabled)[0]:
                    self.OnCopy()
                    self.paste_available = True
    
                if imgui.menu_item("Paste", enabled = paste_enabled)[0]:
                    self.OnPaste()
                    self.paste_available = True
    
                if imgui.menu_item("Delete", enabled = edit_enabled)[0]:
                    self.OnDelete()
    
                imgui.end_menu()            
                
            self.ShowMenus()
            
            if imgui.begin_menu("Help"):
                
                if imgui.menu_item("Show help")[0]:
                    self.help_visible = True
                    print("Show help")
                    
                    
                imgui.end_menu()
            
            imgui.end_main_menu_bar()
        
        # Ventanas
        
        if self.document_opened:
            imgui.begin("Document")
            
            self.ShowDocument()

            imgui.end()
    
        if self.help_visible:
            self.help_visible = imgui.begin("Help", True)[1]
            
            self.ShowHelp()
            
            imgui.end()
            
        self.ShowTools()
    
    
        if self.open_file_popup:
            imgui.open_popup("Open file")
            self.popup_file_not_exists = False
            self.open_file_popup = False
    
        if imgui.begin_popup("Open file"):        
            _, self.document_file_name = imgui.input_text("File name", self.document_file_name, 256)
            if self.popup_file_not_exists:
                imgui.text("No se pudo abrir el fichero")
            if imgui.button("Open"): 
                try:
                    file = open(self.document_file_name)
                except FileNotFoundError:
                    self.popup_file_not_exists = True
                else:
                    file.close()
                    self.OnOpen(self.document_file_name)
                    self.document_loaded = True
                    self.document_opened = True
                    imgui.close_current_popup()

            imgui.end_popup()
        
        ImguiUtils.update_end()
    
    def Finish(self):
        ImguiUtils.finish()


    def OnInit(self):
        pass

    def OnNew(self):
        pass
    
    def OnOpen(self, document_file_name):
        pass
    
    def OnSave(self):
        pass

    def OnClose(self):
        pass

    def OnCut(self):
        pass

    def OnCopy(self):
        pass

    def OnPaste(self):
        pass

    def OnDelete(self):
        pass

    def OnExit(self):
        pass
    
    def ShowDocument(self):
        pass
    
    def ShowHelp(self):
        pass
    
    def ShowTools(self):
        pass
    
    def ShowMenus(self):
        pass
    
    def HasSelection(self):
        return False
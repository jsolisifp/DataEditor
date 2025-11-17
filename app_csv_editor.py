from app import App
import imgui

class CSVEditor(App):
        
    def OnInit(self):
        self.file_contents = []
        self.line_selected_index = -1
        self.copied_line = None;

    def OnNew(self):
        self.file_contents = ["Name,Age,Height", "Pepe,23,1.8", "Juan,50,1.7", "Ana,30,1.7"]
        self.line_selected_index = -1
    
    def OnOpen(self, file_name):
        print("Open clicked")
        file = open(file_name, "r")
        self.file_contents = file.readlines()
        file.close()

    def OnSave(self):
        print("Save clicked")
        file = open("documento.csv", "w")
        file.writelines(self.file_contents)
        file.close()

    def OnClose(self):
        print("Close clicked")
        
    def OnCut(self):
        print("Cut clicked");
        self.copied_line = self.file_contents.pop(self.line_selected_index)
        self.line_selected_index -= 1;
        

    def OnCopy(self):
        print("Copy clicked");
        self.copied_line = self.file_contents[self.line_selected_index]

    def OnPaste(self):
        print("Paste clicked");
        self.file_contents.insert(self.line_selected_index, self.copied_line)
        self.line_selected_index += 1;

    def OnDelete(self):
        print("Delete clicked");
        self.file_contents.pop(self.line_selected_index)
        self.line_selected_index -= 1;


    def OnExit(self):
        print("Exit clicked")
        
    def ShowDocument(self):
        _, self.line_selected_index = imgui.listbox("File contents", self.line_selected_index, self.file_contents, 100)

    def ShowHelp(self):
        imgui.text("This is a simple text lines editor by\n"
                   "By José Manuel Solís\n")

    def ShowMenus(self):
        pass

    def ShowTools(self):
        if self.document_opened:
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
                    if(len(self.file_contents) == 0):
                        self.line_selected_index = -1
            if len(self.file_contents) >= 1:
                if imgui.button("Duplicate"):
                    line_to_duplicate = self.file_contents[self.line_selected_index]
                    self.file_contents.insert(self.line_selected_index + 1, line_to_duplicate)
            
            imgui.end()
            
    def HasSelection(self):
        return self.line_selected_index >= 0

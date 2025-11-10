from data_editor import DataEditor

editor = DataEditor()
editor.Init()

while not editor.ShouldClose():
    editor.Update()
    
editor.Finish()





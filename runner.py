class Runner:
    
    @classmethod
    def Run(cls, app):
        app.Init()

        while not app.ShouldClose():
            app.Update()
            
        app.Finish()





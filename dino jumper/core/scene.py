class Scene:

    def __init__(self):
        self._cast = self.create_cast()
        self._script = self.create_script()

    def create_cast(self):
        pass

    def create_script(self):
        pass

    def get_cast(self):
        return self._cast

    def get_script(self):
        return self._script
  
    
    
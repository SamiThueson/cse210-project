from core.action import Action


class DrawActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._draw_animal(cast)

    def _draw_animal(self, cast):
        animals = cast.get_actors("animals")
        for animal in animals:
            animal.draw()
    
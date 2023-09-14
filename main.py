from pynput import mouse

class board:
    def __init__(self):
        self.tl = None
        self.br = None
        
        self.capture_regision()

        print(self.tl, self.br)

    def capture_regision(self):
        with mouse.Events() as events:
            for event in events:
                if self.tl is not None and self.br is not None:
                    break
                if type(event) is not mouse.Events.Click:
                    continue
                if event.pressed == False:
                    continue
                if self.tl is None:
                    self.tl = (event.x, event.y)
                else:
                    self.br = (event.x, event.y)


b = board()



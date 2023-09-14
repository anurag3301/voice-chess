from pynput import mouse
import cv2
import pyautogui
import numpy as np

class board:
    def __init__(self):
        self.tl = None
        self.br = None
        self.tl = (2750, 66)        
        self.br = (3382, 700)
        self.capture_regision()
        self.capture_screen()

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

    def capture_screen(self):
        screenshot = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        image = image[self.tl[1]:self.br[1], self.tl[0]:self.br[0]]
        shape = image.shape
        for i in range(1, 8):
            image = cv2.line(image, (0, shape[1]//8*i), (shape[0], shape[1]//8*i), (0, 0, 255), 2)
        for i in range(1, 8):
            image = cv2.line(image, (shape[0]//8*i, 0), (shape[0]//8*i, shape[1]), (0, 0, 255), 2)

        top = image[0:shape[0]//8, 0:shape[1]]
        bottom = image[shape[0]//8*7:shape[0], 0:shape[1]]

        if top.mean() > bottom.mean():
            print("You playing as Black")
        else:
            print("You playing as White")

        cv2.imshow('Screenshot', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


b = board()



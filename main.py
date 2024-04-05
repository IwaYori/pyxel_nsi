import pyxel
class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    @staticmethod
    def draw():
        pyxel.cls(0)


App()

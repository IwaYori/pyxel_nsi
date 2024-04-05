import pyxel

pyxel.init(160, 160)
def update():
    if pyxel.btnp(pyxel.KEY_ESCAPE):
        pyxel.quit()

def draw():
    pyxel.cls(0)


pyxel.run(update, draw)

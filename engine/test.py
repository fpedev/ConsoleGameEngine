from src import DisplayManager
from libraries import LightingLibrary

display = DisplayManager.create(rows=25, size=100, fill=None)

testLight = LightingLibrary.Light(20,20,5)

while True:




    ################################################################
    display.render()
    display.clear()
    testLight.draw(display)
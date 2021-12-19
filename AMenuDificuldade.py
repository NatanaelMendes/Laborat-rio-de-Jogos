from PPlay.window import *
from PPlay.gameimage import *


def menu_dificuldade():
    window = Window(800, 600)
    const = 100
    mouse = Window.get_mouse()
    background = GameImage("menu background.jpg")
    easy_png = GameImage("easy.png")
    medium_png = GameImage("medium.png")
    hard_png = GameImage("hard.png")
    easy_png.x = medium_png.x = hard_png.x = window.width/2 - easy_png.width/2
    easy_png.y = const
    medium_png.y = easy_png.y + const
    hard_png.y = medium_png.y + const
    while True:
        if mouse.is_button_pressed(1) and (mouse.is_over_object(easy_png)):
            return (1)
        if mouse.is_button_pressed(1) and mouse.is_over_object(medium_png):
            return (2)
        if mouse.is_button_pressed(1) and mouse.is_over_object(hard_png):
            return (3)
        background.draw()
        easy_png.draw()
        medium_png.draw()
        hard_png.draw()
        window.update()
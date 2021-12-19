from PPlay.mouse import *
from AMenuDificuldade import *
from AJogatina import *
from PPlay.window import *


def iniciar(bool, altura, largura):
    window = Window(altura, largura)
    window.set_title("Space Invaders")
    background = GameImage("menu background.jpg")
    iniciar_png = GameImage("iniciar.png")
    dificuldade_png = GameImage("Dificuldade.png")
    ranking_png = GameImage("Ranking.png")
    sair_png = GameImage("Sair.png")

    iniciar_png.x = window.width / 3 - iniciar_png.width / 3
    dificuldade_png.x = iniciar_png.x
    ranking_png.x = iniciar_png.x * 2
    sair_png.x = iniciar_png.x * 2

    iniciar_png.y = window.height / 5
    dificuldade_png.y = window.height * 2 / 5
    ranking_png.y = window.height / 5
    sair_png.y = window.height * 2 / 5
    mouse = Window.get_mouse()
    nivel = 1

    while bool:
        if mouse.is_button_pressed(1) and (mouse.is_over_object(sair_png)):
            window.close()
        if mouse.is_button_pressed(1) and mouse.is_over_object(dificuldade_png):
            nivel = menu_dificuldade()
        if mouse.is_button_pressed(1) and mouse.is_over_object(iniciar_png):
            bool = play(nivel, altura, largura)

        background.draw()
        iniciar_png.draw()
        dificuldade_png.draw()
        ranking_png.draw()
        sair_png.draw()
        window.update()
        mouse = Mouse()
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameimage import *


def criar_monstros(linha, coluna):
    for i in range(linha):
        lin = []
        for j in range(coluna):
            alien = Sprite("monster2.png")
            alien.x = (window.width/linha*2) * i/5+ alien.width/2
            alien.y = (window.height/coluna*2) * j/5+ alien.height/2
            lin.append(alien)
        matrix.append(lin)

def desenha_monstro(vel_monster):
    for i in range(A):
        for j in range(B):
            matrix[i][j].draw()
            if matrix[0][0].x >= 5:
                vel_monster *= -1
            if matrix[A - 1][B - 1].x <= window.width - 5:
                vel_monster *= -1
            matrix[i][j].x += vel_monster * window.delta_time()



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

def play(nivel, vel_monster):
    window = Window(800, 600)
    background = GameImage("menu background.jpg")
    teclado = Window.get_keyboard()
    spaceship = Sprite("nave.png", 1)
    spaceship.x = window.width/2 - spaceship.width/2
    spaceship.y = window.height - spaceship.height - 10
    contador = 0
    lista_bullet = []
    criar_monstros(A, B)

    while True:
        if teclado.key_pressed("ESC"):
            lista_bullet.clear()
            return True
        if teclado.key_pressed("a") and spaceship.x >= 5:
            spaceship.x -= vel_ship * window.delta_time()
        if teclado.key_pressed("d") and spaceship.x + spaceship.width <= window.width - 5:
            spaceship.x += vel_ship * window.delta_time()
        contador += window.delta_time()
        if teclado.key_pressed("space") and contador >= 0.1 * nivel:
            bullet = Sprite("tiro.png", 1)
            bullet.x = spaceship.x + spaceship.width/2 - 4
            bullet.y = spaceship.y - bullet.y - 10
            lista_bullet.append(bullet)
            contador = 0
        background.draw()
        spaceship.draw()
        for bala in lista_bullet:
            bala.draw()
            bala.y -= vel_bullet * window.delta_time()
            for bala in lista_bullet:
                if bala.y < 0 - bullet.width:
                    lista_bullet.remove(bala)
        desenha_monstro(vel_monster)


        window.update()


window = Window(800, 600)
background = GameImage("menu background.jpg")
iniciar_png = GameImage("iniciar.png")
dificuldade_png = GameImage("Dificuldade.png")
ranking_png = GameImage("Ranking.png")
sair_png = GameImage("Sair.png")
matrix = []
A = B = 5
vel_ship = 250
vel_bullet = 300
vel_monster = 200

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
bool = True


while bool:
    if mouse.is_button_pressed(1) and (mouse.is_over_object(sair_png)):
        window.close()
    if mouse.is_button_pressed(1) and mouse.is_over_object(dificuldade_png):
        nivel = menu_dificuldade()
    if mouse.is_button_pressed(1) and mouse.is_over_object(iniciar_png):
        bool = play(nivel, vel_monster)


    background.draw()
    iniciar_png.draw()
    dificuldade_png.draw()
    ranking_png.draw()
    sair_png.draw()
    window.update()
    mouse = Mouse()

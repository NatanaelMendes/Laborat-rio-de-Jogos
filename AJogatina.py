from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from AMonstros import *

def criar_bala():
    fiiire = Sprite("tiro.png", 1)
    return fiiire

def play(nivel, altura, largura):
    window = Window(altura, largura)
    background = GameImage("menu background.jpg")
    teclado = Window.get_keyboard()
    spaceship = Sprite("nave.png", 1)
    spaceship.x = window.width/2 - spaceship.width/2
    spaceship.y = window.height - spaceship.height - 10
    vel_ship = 250
    vel_bullet = 300
    vel_monster = 100
    contador = 0
    lista_bullet = []
    a, b = 6, 6
    matrix = []
    matrix = cria_monstro(a, b, matrix)
    y_monster = 0


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
            bullet = criar_bala()
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
        for i in range(a):
            for j in range(b):
                matrix[i][j].draw()
                matrix[i][j].x += vel_monster * window.delta_time()
        if matrix[-1][-1].x > window.width - matrix[-1][-1].width - 5:
            vel_monster *= -1
            y_monster += matrix[-1][-1].width/2
            for i in range(a):
                for j in range(b):
                    matrix[i][j].y += y_monster
        if matrix[0][0].x < 5:
            vel_monster *= -1
            y_monster += matrix[0][0].width/2
            for i in range(a):
                for j in range(b):
                    matrix[i][j].y += y_monster
        window.update()


from PPlay.sprite import *

def cria_monstro(a, b, matrix):
    alt = 30
    lar = 60
    for i in range(a):
        lin = []
        for j in range(b):
            alien = Sprite("monster2.png", 1)
            alien.x = (lar * i) + alien.width/2
            alien.y = (alt * j) + alien.height/2
            lin.append(alien)
        matrix.append(lin)
    return matrix


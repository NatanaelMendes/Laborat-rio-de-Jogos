from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

# dimensão da janela
janela = Window(800, 600)

#nome para a janela
janela.set_title("Pong")

#incicializando controles
teclado = Window.get_keyboard()

#imagem: Pad, Bola, Fundo
fundo = GameImage("Img2.jpg")
padE = Sprite("PadE.png", 1)
padD = Sprite("PadD.png", 1)
bola = Sprite("pkball.png", 1)

#centralizando a bola e pads
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2
padE.x = 15
padE.y = janela.height / 2 - padE.height / 2
padD.x = janela.width - padD.width - 15
padD.y = janela.height / 2 - padD.height / 2

#Velocidade dos objetos
velbolax = 200
velbolay = 140
velPad = 180

#contador de pontos
placarD = 0
placarE = 0
batidas = 0
contador_tempo = 0
contador_frame = 0
fps = 0
#janela em loop
while True:
# movimento dos players
#    if teclado.key_pressed("UP") and padD.y >= 3:
 #       padD.y = padD.y - velPad * janela.delta_time()
#    if teclado.key_pressed("DOWN") and (padD.y + padD.height <= janela.height - 3):
 #       padD.y = padD.y + velPad * janela.delta_time()
    if teclado.key_pressed("w") and padE.y >= 3:
        padE.y = padE.y - velPad * janela.delta_time()
    if teclado.key_pressed("s") and (padE.y + padE.height <= janela.height - 3):
        padE.y = padE.y + velPad * janela.delta_time()

#AI
    if bola.y > padD.y:
        padD.y += (velPad*0.70)*janela.delta_time()
    if bola.y < padD.y:
        padD.y -= (velPad*0.60)*janela.delta_time()

# contador de frames por segundo
    contador_tempo += janela.delta_time()
    contador_frame +=1
    if contador_tempo >= 1:
        fps = contador_frame
        contador_tempo = 0
        contador_frame = 0

# velocidade igual pra qualquer framerate
    bola.x += velbolax * janela.delta_time()
    bola.y += velbolay * janela.delta_time()

# se a bolinha colidir com o pad
    if bola.collided(padD):
        velbolax *= -1
        bola.x -= bola.height/4
        batidas +=1
#metade do pad
        if batidas == 4:
            padE = Sprite("padmetade.png", 1)
            padE.x = 15
            padE.y = janela.height / 2 - padE.height / 2

    if bola.collided(padE):
        velbolax *= -1
        bola.x += bola.height/4
        batidas += 1

#se a bola colidir com teto e chão
    if bola.y <= 0:
        bola.y = bola.height
        velbolay *= -1

    if bola.y == janela.height - bola.height - 5:
        bola.y = janela.height + bola.height
        velbolay *= -1

# rebatendo no teto e chão
    if ((bola.y + bola.height) >= janela.height-5) or (bola.y < 5):
        velbolay *= -1

# centralizar apos pontuar + contador de pontos
    if ((bola.x + bola.width) >= janela.width):
        bola.x = janela.width / 2 - bola.width / 2
        bola.y = janela.height / 2 - bola.height / 2
        placarE +=1
        padE = Sprite("PadE.png", 1)
        padE.x = 15
        padE.y = janela.height / 2 - padE.height / 2
        batidas = 0
    if (bola.x <= 0):
        bola.x = janela.width / 2 - bola.width / 2
        bola.y = janela.height / 2 - bola.height / 2
        placarD += 1
        padE = Sprite("PadE.png", 1)
        padE.x = 15
        padE.y = janela.height / 2 - padE.height / 2
        batidas = 0




# graficos
    fundo.draw()
    bola.draw()
    padD.draw()
    padE.draw()
    janela.draw_text(str(placarE), janela.width / 5, 25, 50, (255, 255, 0), "Arial", True, False)
    janela.draw_text(str(placarD), (janela.width * 4)/ 5, 25, 50, (255, 255, 0), "Arial", True, False)
    janela.draw_text("FPS "+ str(fps), (janela.width) *2 / 5, 25, 50, (255, 255, 0), "Arial", True, False)
    janela.update()
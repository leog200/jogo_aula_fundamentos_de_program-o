import pygame
import random
import time
pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("Peleia Gaúcha")
altura = 960
largura = 800
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
preto = (0,0,0)
fundo = pygame.image.load("assets/fundoo.jpg")
gaucho = pygame.image.load("assets/manolima.png")
queroquero = pygame.image.load("assets/queroqueroo.png")




def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,preto)
    gameDisplay.blit(textoDisplay, (880,80))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",25)
    fonte2  = pygame.font.Font("freesansbold.ttf",19)
    textoDisplay = fonte.render("BAAA VIVENTE, O QUERO - QUERO TE PEGOU!!",True,preto)
    textoDisplay2 = fonte2.render("mas não te acanhe e clica no ENTER para tentar escapar dele, tchê!",True,preto)
    gameDisplay.blit(textoDisplay, ( 150, 150))
    gameDisplay.blit(textoDisplay2, (150,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    gauchoX = 300
    gauchoY = 720
    movimentoGauchoX = 0
    larguraGaucho = 215
    alturaGaucho = 130
    alturaQueroQuero = 135
    larguraQueroQuero = 56
    posicaoQueroQueroX = 400
    posicaoQueroQueroY = -240
    velocidadeQueroQuero = 1
    pygame.mixer.music.load("assets/tontoagolpe.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)

    queroqueroSound = pygame.mixer.Sound("assets/QueroQuerocantando.wav")
    queroqueroSound.set_volume(1)
    pygame.mixer.Sound.play(queroqueroSound)

    sapucaySound = pygame.mixer.Sound("assets/sapucay.wav")
    sapucaySound.set_volume(1)
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoGauchoX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentoGauchoX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoGauchoX = 0
            
        if jogando:
            if posicaoQueroQueroY > altura:
                posicaoQueroQueroY = -240
                posicaoQueroQueroX = random.randint(0,largura)
                velocidadeQueroQuero = velocidadeQueroQuero + 1
                pygame.mixer.Sound.play(queroqueroSound)
            else:
                posicaoQueroQueroY = posicaoQueroQueroY + velocidadeQueroQuero

            if gauchoX + movimentoGauchoX >0 and gauchoX + movimentoGauchoX< largura-larguraGaucho:
                gauchoX = gauchoX + movimentoGauchoX
            gameDisplay.fill(preto)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(gaucho, (gauchoX,gauchoY))
            
            gameDisplay.blit(queroquero, (posicaoQueroQueroX,posicaoQueroQueroY))
           

            pixelsXGaucho = list(range(gauchoX, gauchoX+larguraGaucho))
            pixelsYGaucho = list(range(gauchoY,gauchoY+alturaGaucho))
            pixelXQueroQuero = list(range(posicaoQueroQueroX, posicaoQueroQueroX+larguraQueroQuero))
            pixelYQueroQuero = list(range(posicaoQueroQueroY, posicaoQueroQueroY+alturaQueroQuero))

            colisaoY = len(list(set(pixelYQueroQuero) & set(pixelsYGaucho) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXQueroQuero) & set(pixelsXGaucho) ))
                print(colisaoX)
                if colisaoX > 45:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(sapucaySound)


        pygameDisplay.update()
        clock.tick(60)

jogar()

import pygame
import sys
import constantes
import funcoes as f
import classes as c
from OpenGL.GL import *
from OpenGL.GLU import *

f.desativar_escala_windows()
pygame.init()

LARGURA_MONITOR = f.tela_largura()
ALTURA_MONITOR = f.tela_altura()
JANELA_LARGURA = LARGURA_MONITOR // 2
JANELA_ALTURA = ALTURA_MONITOR // 2

eh_tela_cheia = False

flags = pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF
tela = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA), flags)
pygame.display.set_caption("Planetário Interativo")

f.configurar_camera(JANELA_LARGURA, JANELA_ALTURA)
glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.1, 1.0)
relogio = pygame.time.Clock()
rodando = True

quadric = gluNewQuadric()

sol = c.CorpoCeleste(raio=3.0, distancia=0.0, velocidade=0.5, cor=(1.0, 1.0, 0.0))
terra = c.CorpoCeleste(raio=1.0, distancia=10.0, velocidade=1.0, cor=(0.0, 0.4, 1.0))
lua = c.CorpoCeleste(raio=0.3, distancia=2.5, velocidade=3.0, cor=(0.6, 0.6, 0.6))

terra.adicionar_satelite(lua)
sol.adicionar_satelite(terra)

while rodando:
    for event in pygame.event.get():
        rodando = f.checar_fechamento(event, rodando)

        if event.type == pygame.VIDEORESIZE:
            tela = f.tamanho_tela_botao(event, tela)
            f.configurar_camera(event.w, event.h)
            glEnable(GL_DEPTH_TEST)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                eh_tela_cheia = not eh_tela_cheia
                tela = f.tamanho_tela_f11(eh_tela_cheia, JANELA_LARGURA, JANELA_ALTURA)

                f.configurar_camera(f.tela_largura(), f.tela_altura())
                glEnable(GL_DEPTH_TEST)

            if event.key == pygame.K_ESCAPE:
                rodando = False
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    sol.atualizar_fisica()
    sol.desenhar(quadric)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()
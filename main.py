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
glClearColor(*constantes.COR_FUNDO)

relogio = pygame.time.Clock()
rodando = True

f.pausa_mouse(False)

posicoes = {
            "cam_x": 0.0,
            "cam_y": 0.0,
            "cam_z": 30.0
            }

vertical, transversal = 0.0, 0.0
pausado = False

quadric = gluNewQuadric()

sol = c.CorpoCeleste(*constantes.SOL)
terra = c.CorpoCeleste(*constantes.TERRA)
lua = c.CorpoCeleste(*constantes.LUA)
mercurio = c.CorpoCeleste(*constantes.MERCURIO)
venus = c.CorpoCeleste(*constantes.VENUS)
marte = c.CorpoCeleste(*constantes.MARTE)
jupiter = c.CorpoCeleste(*constantes.JUPITER)
saturno = c.CorpoCeleste(*constantes.SATURNO)
urano = c.CorpoCeleste(*constantes.URANO)
netuno = c.CorpoCeleste(*constantes.NETUNO)

terra.adicionar_satelite(lua)
sol.adicionar_satelite(terra)
sol.adicionar_satelite(mercurio)
sol.adicionar_satelite(venus)
sol.adicionar_satelite(marte)
sol.adicionar_satelite(jupiter)
sol.adicionar_satelite(saturno)
sol.adicionar_satelite(urano)
sol.adicionar_satelite(netuno)

pygame.mouse.get_rel()
f.inicializar_estrelas(1000)
while rodando:
    for event in pygame.event.get():
        rodando = f.checar_fechamento(event, rodando)

        if event.type == pygame.VIDEORESIZE:
            tela = f.tamanho_tela_botao(event, tela)
            f.configurar_camera(event.w, event.h)
            glEnable(GL_DEPTH_TEST)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3: 
                pausado = not pausado
                f.pausa_mouse(pausado)
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                eh_tela_cheia = not eh_tela_cheia
                tela = f.tamanho_tela_f11(eh_tela_cheia, LARGURA_MONITOR, ALTURA_MONITOR)
                
                pygame.display.flip()
                
                f.configurar_camera(LARGURA_MONITOR*2, ALTURA_MONITOR*2)
                glEnable(GL_DEPTH_TEST)

            if event.key == pygame.K_ESCAPE:
                rodando = False

    if not pausado:
        dx, dy = pygame.mouse.get_rel()
        vertical += dx * 0.2
        transversal += dy * 0.2
        transversal = max(-90.0, min(90.0, transversal)) 

        teclas = pygame.key.get_pressed()
        posicoes = f.movimentos(teclas, constantes.VEL_CAMERA, vertical, posicoes)
        sol.atualizar_fisica()  
    else:
        pygame.mouse.get_rel()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glRotatef(transversal, *constantes.ROT_EIXO_X)
    glRotatef(vertical, *constantes.ROT_EIXO_Y)
    glTranslatef(-posicoes["cam_x"], -posicoes["cam_y"], -posicoes["cam_z"])

    f.desenhar_estrelas()
    sol.desenhar(quadric)

    pygame.display.flip()
    relogio.tick(30)

pygame.quit()
sys.exit()
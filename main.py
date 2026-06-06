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

buraco_negro = c.CorpoCeleste(*constantes.BURACO_NEGRO)

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

buraco_negro.adicionar_satelite(sol)

pygame.mouse.get_rel()
f.inicializar_estrelas(constantes.NUM_ESTRELAS)
estado_atual = "menu"

while rodando:
    for event in pygame.event.get():
        rodando = f.checar_fechamento(event, rodando)

        if estado_atual == "menu" and event.type == pygame.MOUSEBUTTONDOWN:
            estado_atual = "jogando"
            pygame.mouse.set_visible(False)
            pygame.event.set_grab(True)

        elif estado_atual == "jogando":
            if event.type == pygame.VIDEORESIZE:
                tela = f.tamanho_tela_botao(event, tela)
                f.configurar_camera(event.w, event.h)
                glEnable(GL_DEPTH_TEST)
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
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

    if estado_atual == "jogando" and not pausado:
        dx, dy = pygame.mouse.get_rel()
        vertical += dx * constantes.VOL_DX
        transversal += dy * constantes.VOL_DY
        transversal = max(-90.0, min(90.0, transversal)) 

        teclas = pygame.key.get_pressed()
        posicoes = f.movimentos(teclas, constantes.VEL_CAMERA, vertical, posicoes)
        sol.atualizar_fisica()
    elif estado_atual == "jogando" and pausado:
        pygame.mouse.get_rel()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    if estado_atual == "menu":
        glDisable(GL_DEPTH_TEST)
        fonte = pygame.font.SysFont("Arial", 30)
        f.desenhar_texto_opengl(constantes.INSTRUCOES, fonte, JANELA_LARGURA, JANELA_ALTURA)
        
        glEnable(GL_DEPTH_TEST)
    elif estado_atual == "jogando":
        if not pausado:
            dx, dy = pygame.mouse.get_rel()
            vertical += dx * constantes.VOL_DX
            transversal += dy * constantes.VOL_DY
            transversal = max(-90.0, min(90.0, transversal)) 
            teclas = pygame.key.get_pressed()
            posicoes = f.movimentos(teclas, constantes.VEL_CAMERA, vertical, posicoes)
            sol.atualizar_fisica()
        else:
            pygame.mouse.get_rel()

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(transversal, *constantes.ROT_EIXO_X)
        glRotatef(vertical, *constantes.ROT_EIXO_Y)
        glTranslatef(-posicoes["cam_x"], -posicoes["cam_y"], -posicoes["cam_z"])

        f.desenhar_estrelas()
        buraco_negro.desenhar(quadric)

    pygame.display.flip()
    relogio.tick(constantes.FPS)

pygame.quit()
sys.exit()
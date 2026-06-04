import pygame
import ctypes
import constantes
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math

def configurar_camera(largura_tela, altura_tela):
    if altura_tela == 0:
         altura_tela = 1

    glViewport(0, 0, largura_tela, altura_tela)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45.0, (largura_tela / altura_tela), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def tela_largura():
    return pygame.display.Info().current_w

def tela_altura():
    return pygame.display.Info().current_h

def desativar_escala_windows():
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except AttributeError:
        pass

def checar_fechamento(event, estado_rodando):
     if event.type == pygame.QUIT:
             return False
     return estado_rodando
     
def tamanho_tela_botao(event, tela_atual):
    if event.type == pygame.VIDEORESIZE:
        flags_opengl = pygame.RESIZABLE | pygame.OPENGL | pygame.DOUBLEBUF
        return pygame.display.set_mode((event.w, event.h), flags_opengl)
    return tela_atual

def tamanho_tela_f11(eh_tela_cheia, largura_janela, altura_janela):
    flags_opengl = pygame.OPENGL | pygame.DOUBLEBUF
    
    if eh_tela_cheia:
        # Força o uso da resolução nativa do monitor (0,0)
        tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | flags_opengl)
    else:
        tela = pygame.display.set_mode((largura_janela, altura_janela), pygame.RESIZABLE | flags_opengl)
    
    # [FORÇAR ATUALIZAÇÃO]: Garante que o OpenGL saiba que a área mudou
    w, h = tela.get_size()
    glViewport(0, 0, w, h)
    
    return tela

def desenhar_estrelas(quantidade=100):
    glBegin(GL_POINTS)
    glColor3f(*constantes.COR_ESTRELAS)
    for _ in range(quantidade):
        x = random.uniform(-50, 50)
        y = random.uniform(-50, 50)
        z = random.uniform(-50, 50)
        glVertex3f(x, y, z)
    glEnd()


def movimentos(teclas, velocidade_camera, yaw, posicoes):
    if teclas[pygame.K_w]:
        posicoes["cam_x"] += math.sin(math.radians(yaw)) * velocidade_camera
        posicoes["cam_z"] -= math.cos(math.radians(yaw)) * velocidade_camera
    if teclas[pygame.K_s]:
        posicoes["cam_x"] -= math.sin(math.radians(yaw)) * velocidade_camera
        posicoes["cam_z"] += math.cos(math.radians(yaw)) * velocidade_camera
    if teclas[pygame.K_a]:
        posicoes["cam_x"] -= math.cos(math.radians(yaw)) * velocidade_camera
        posicoes["cam_z"] -= math.sin(math.radians(yaw)) * velocidade_camera
    if teclas[pygame.K_d]:
        posicoes["cam_x"] += math.cos(math.radians(yaw)) * velocidade_camera
        posicoes["cam_z"] += math.sin(math.radians(yaw)) * velocidade_camera
    if teclas[pygame.K_SPACE]: 
        posicoes["cam_y"] += velocidade_camera
    if teclas[pygame.K_LSHIFT]: 
        posicoes["cam_y"] -= velocidade_camera

    return posicoes
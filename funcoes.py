import pygame
import ctypes
import constantes
from OpenGL.GL import *
from OpenGL.GLU import *

def configurar_camera(largura_tela, altura_tela):
    if altura_tela == 0:
         altura_tela = 1

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    gluPerspective(45.0, (largura_tela / altura_tela), 0.1, 100.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -30.0)

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
        return pygame.display.set_mode((0,0), pygame.FULLSCREEN | flags_opengl)
    else:
        return pygame.display.set_mode((largura_janela, altura_janela), pygame.RESIZABLE | flags_opengl)

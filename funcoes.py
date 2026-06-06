import pygame
import ctypes
import constantes
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math

estrelas_fixas = []
_text_cache = {"id": None, "last_text": None}

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
        return pygame.display.set_mode((0, 0), pygame.FULLSCREEN | flags_opengl)
    else:
        return pygame.display.set_mode((largura_janela, altura_janela), pygame.RESIZABLE | flags_opengl)

def inicializar_estrelas(quantidade=constantes.QUANT_ESTRELAS):
    global estrelas_fixas
    estrelas_fixas = []
    for _ in range(quantidade):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        z = random.uniform(-100, 100)
        estrelas_fixas.append((x, y, z))

def desenhar_estrelas():
    glBegin(GL_POINTS)
    glColor3f(*constantes.COR_ESTRELAS)
    for x, y, z in estrelas_fixas:
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

def pausa_mouse(pausado):
    if pausado:
        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)
    else:
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        pygame.mouse.get_rel()

def desenhar_texto_opengl(texto_lista, fonte, largura_tela, altura_tela):
    global _text_cache
    
    if _text_cache["last_text"] != texto_lista:
        if _text_cache["id"]:
            glDeleteTextures(_text_cache["id"])
            
        linha_altura = fonte.get_height()
        largura_max = max([fonte.size(l)[0] for l in texto_lista]) + 10
        total_altura = (linha_altura + 10) * len(texto_lista)
        
        sup = pygame.Surface((largura_max, total_altura), pygame.SRCALPHA)
        
        for i, linha in enumerate(texto_lista):
            y_pos = i * (linha_altura + 10)
            sombra = fonte.render(linha, True, (0, 0, 0, 150))
            texto = fonte.render(linha, True, (255, 255, 255, 255))
            
            sup.blit(sombra, (2, y_pos + 2))
            sup.blit(texto, (0, y_pos))
            
        data = pygame.image.tostring(sup, "RGBA", True)
        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, sup.get_width(), sup.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        
        _text_cache.update({"id": tex_id, "last_text": texto_lista, "w": sup.get_width(), "h": total_altura})

    glDisable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, largura_tela, altura_tela, 0, -1, 1)
    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    glBindTexture(GL_TEXTURE_2D, _text_cache["id"])
    glEnable(GL_TEXTURE_2D)
    
    x_offset = (largura_tela - _text_cache["w"]) // 2
    y_offset = (altura_tela - _text_cache["h"]) // 2
    
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1); glVertex2f(x_offset, y_offset)
    glTexCoord2f(1, 1); glVertex2f(x_offset + _text_cache["w"], y_offset)
    glTexCoord2f(1, 0); glVertex2f(x_offset + _text_cache["w"], y_offset + _text_cache["h"])
    glTexCoord2f(0, 0); glVertex2f(x_offset, y_offset + _text_cache["h"])
    glEnd()
    
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glEnable(GL_DEPTH_TEST)
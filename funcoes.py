import pygame
import ctypes
import constantes
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math

estrelas_fixas = []

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

def inicializar_estrelas(quantidade=100):
    global estrelas_fixas
    estrelas_fixas = []
    for _ in range(quantidade):
        x = random.uniform(-50, 50)
        y = random.uniform(-50, 50)
        z = random.uniform(-50, 50)
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
    glDisable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    sup = pygame.Surface((largura_tela, altura_tela), pygame.SRCALPHA)
    y_inicial = (altura_tela // 2) - (len(texto_lista) * 20)

    for i, linha in enumerate(texto_lista):
        sombra = fonte.render(linha, True, (0, 0, 0))
        # Texto Principal (Branco)
        texto = fonte.render(linha, True, (255, 255, 255))
        
        # Calcula largura para centralizar
        rect = texto.get_rect(center=(largura_tela // 2, y_inicial + (i * 50)))
        
        sup.blit(sombra, rect.move(2, 2)) # Sombra deslocada 2px
        sup.blit(texto, rect)
    
    # 2. Converte para o formato que o OpenGL gosta
    data = pygame.image.tostring(sup, "RGBA", True)
    
    # 3. Cria a textura
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, largura_tela, altura_tela, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    
    # 4. Desenha usando projeção ortogonal (para não distorcer)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix() # Salva a projeção 3D
    glLoadIdentity()
    glOrtho(0, largura_tela, altura_tela, 0, -1, 1) # Projeção 2D
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 1); glVertex2f(0, 0)
    glTexCoord2f(1, 1); glVertex2f(largura_tela, 0)
    glTexCoord2f(1, 0); glVertex2f(largura_tela, altura_tela)
    glTexCoord2f(0, 0); glVertex2f(0, altura_tela)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    
    # Restaura o estado anterior
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    
    glDeleteTextures(int(tex_id))
    glEnable(GL_DEPTH_TEST)
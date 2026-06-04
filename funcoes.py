import pygame
import ctypes
import constantes

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
            return pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    return tela_atual
        

def tamanho_tela_f11(eh_tela_cheia, largura_janela, altura_janela):
    if eh_tela_cheia:
        return pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode((largura_janela, altura_janela), pygame.RESIZABLE)

import pygame
import sys
import constantes
import funcoes as f

f.desativar_escala_windows()
pygame.init()

LARGURA_MONITOR = f.tela_largura()
ALTURA_MONITOR = f.tela_altura()
JANELA_LARGURA = LARGURA_MONITOR // 2
JANELA_ALTURA = ALTURA_MONITOR // 2

eh_tela_cheia = False
tela = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA), pygame.RESIZABLE)
pygame.display.set_caption("Planetário Interativo")

relogio = pygame.time.Clock()
rodando = True

while rodando:
    for event in pygame.event.get():
        rodando = f.checar_fechamento(event, rodando)
        tela = f.tamanho_tela_botao(event, tela)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                eh_tela_cheia = not eh_tela_cheia

            tela = f.tamanho_tela_f11(eh_tela_cheia, JANELA_LARGURA, JANELA_ALTURA)

            if event.key == pygame.K_ESCAPE:
                rodando = False
        
    tela.fill(constantes.COR_FUNDO)
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()
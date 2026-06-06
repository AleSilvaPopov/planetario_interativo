from OpenGL.GL import *
from OpenGL.GLU import *


class CorpoCeleste:
    def __init__(self, raio, distancia, velocidade, cor, possui_anel=False, cor_anel=None):
        self.raio = raio
        self.distancia = distancia
        self.velocidade = velocidade
        self.cor = cor
        self.angulo = 0.0
        self.satelites = []

        self.possui_anel = possui_anel
        self.cor_anel = cor_anel if cor_anel else (0.8, 0.8, 0.8)

    def adicionar_satelite(self, satelite):
        self.satelites.append(satelite)

    def atualizar_fisica(self):
        self.angulo += self.velocidade
        for satelite in self.satelites:
            satelite.atualizar_fisica()

    def desenhar(self, quadric):
        glPushMatrix()
        
        glRotatef(self.angulo, 0.0, 1.0, 0.0)
        glTranslatef(self.distancia, 0.0, 0.0)

        glPushMatrix()
        glColor3f(*self.cor)
        gluSphere(quadric, self.raio, 32, 32)

        if self.possui_anel:
            self.desenhar_anel(quadric)

        glPopMatrix()

        for satelite in self.satelites:
            satelite.desenhar(quadric)
            
        glPopMatrix()
    
    def desenhar_anel(self, quadric):
        glPushMatrix()
        
        glColor3f(*self.cor_anel)
        
        glRotatef(90.0, 1.0, 0.0, 0.0)
        
        raio_interno = self.raio * 1.3
        raio_externo = self.raio * 2.0
        
        gluDisk(quadric, raio_interno, raio_externo, 32, 1)
        
        glPopMatrix()
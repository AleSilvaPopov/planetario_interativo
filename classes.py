from OpenGL.GL import *
from OpenGL.GLU import *


class CorpoCeleste:
    def __init__(self, raio, distancia, velocidade, cor):
        self.raio = raio
        self.distancia = distancia
        self.velocidade = velocidade
        self.cor = cor
        self.angulo = 0.0
        self.satelites = []

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
        glPopMatrix()

        for satelite in self.satelites:
            satelite.desenhar(quadric)
            
        glPopMatrix()
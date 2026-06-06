from OpenGL.GL import *
from OpenGL.GLU import *

# CLASSE: CorpoCeleste

# Encapsula o estado físico (raio, órbita, velocidade) e a lógica de renderização 
# de um objeto espacial. Utiliza hierarquia geométrica: satélites orbitam este 
# corpo de forma relativa ao sistema de coordenadas local dele.

class CorpoCeleste:
    def __init__(self, raio, distancia, velocidade, cor, possui_anel=False, cor_anel=None):
        # Propriedades Geométricas e Visuais
        self.raio = raio
        self.distancia = distancia
        self.velocidade = velocidade
        self.cor = cor

        # Estado Físico
        self.angulo = 0.0
        self.satelites = []

        # Propriedades Opcionais (Anéis)
        self.possui_anel = possui_anel
        self.cor_anel = cor_anel if cor_anel else (0.8, 0.8, 0.8)

    def adicionar_satelite(self, satelite):
        # Insere um novo objeto dependente
        self.satelites.append(satelite)

    def atualizar_fisica(self):
        # Acumula o deslocamento angular.
        self.angulo += self.velocidade

        # Propaga a atualização da física em profundidade para todos os filhos.
        for satelite in self.satelites:
            satelite.atualizar_fisica()

    def desenhar(self, quadric):
        # ISOLAMENTO HIERÁRQUICO
        glPushMatrix()
        
        # Transforma o sistema de coordenadas para a órbita deste corpo.
        # Faz o corpo transladar ao longo de um raio, descrevendo um círculo ao redor da origem atual.
        glRotatef(self.angulo, 0.0, 1.0, 0.0)
        glTranslatef(self.distancia, 0.0, 0.0)

        # Escopo Visual do Corpo
        glPushMatrix()
        glColor3f(*self.cor)
        gluSphere(quadric, self.raio, 32, 32)

        if self.possui_anel:
            self.desenhar_anel(quadric)

        glPopMatrix()
        
        # ROPAGAÇÃO PARA OS SATÉLITES
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
# ARQUIVO DE CONFIGURAÇÃO E CONSTANTES DA SIMULAÇÃO

# PALETA DE CORES (Padrão RGB/RGBA normalizado entre 0.0 e 1.0)
COR_FUNDO = (0.0, 0.0, 0.0, 1.0)
COR_ESTRELAS = (1.0, 1.0, 1.0)
COR_BURACO_NEGRO = (0,0,0)
COR_SOL = (1.0, 0.8, 0.1)
COR_MERCURIO = (0.7, 0.7, 0.7)
COR_VENUS = (0.9, 0.7, 0.3)
COR_TERRA = (0.0, 0.5, 1.0)
COR_MARTE = (0.9, 0.3, 0.2)
COR_JUPITER = (0.8, 0.6, 0.4)
COR_SATURNO = (0.9, 0.8, 0.5)
COR_URANO = (0.5, 0.8, 0.8)
COR_NETUNO = (0.2, 0.2, 0.8)
COR_LUA = (0.7, 0.7, 0.7)
COR_FOBOS     = (0.4, 0.4, 0.4)
COR_DEIMOS    = (0.5, 0.4, 0.3)
COR_IO        = (0.8, 0.8, 0.2)
COR_EUROPA    = (0.9, 0.9, 0.9)
COR_GANIMEDES = (0.5, 0.5, 0.5)
COR_CALISTO   = (0.4, 0.4, 0.4)
COR_TITA      = (0.8, 0.5, 0.2)
COR_ENCELADO  = (1.0, 1.0, 1.0)
COR_REIA      = (0.6, 0.6, 0.6)
COR_TITANIA   = (0.7, 0.7, 0.8)
COR_OBERON    = (0.6, 0.6, 0.7)
COR_MIRANDA   = (0.8, 0.8, 0.8)
COR_TRITAO    = (0.5, 0.8, 0.7)

# Cores dedicadas para geometria adicional (discos de acreção e anéis planetários)
COR_ANEL_BURACO_NEGRO = (1.0, 0.4, 0.0)
COR_ANEL_SATURNO = (0.7, 0.6, 0.5)

# PARÂMETROS GERAIS
QUANT_ESTRELAS = 10000
FPS = 30
ESCALA_TEMPO = 0.3

# CONTROLES E CÂMERA
VEL_CAMERA = 0.5
ROT_EIXO_X = (1.0, 0.0, 0.0)
ROT_EIXO_Y = (0.0, 1.0, 0.0)
VOL_DX = 0.2
VOL_DY = 0.2

# DADOS DOS CORPOS CELESTES
# Índice 0: Raio do objeto (float)
# Índice 1: Distância do centro de sua órbita (float)
# Índice 2: Velocidade orbital / Multiplicador de translação (float)
# Índice 3: Cor principal (Tupla RGB)
# Índice 4: [Opcional] Possui anel? (Booleano)
# Índice 5: [Opcional] Cor do anel (Tupla RGB)

# Corpo estático central
BURACO_NEGRO = (8.0, 0.0, 0.0, COR_BURACO_NEGRO, True, COR_ANEL_BURACO_NEGRO)

# Estrela central do sistema solar
SOL = (4.0, 60.0, 0.2, COR_SOL)

# Planetas
MERCURIO = (0.2, 5.0, 4.0, COR_MERCURIO)
VENUS    = (0.5, 6.5, 3.0, COR_VENUS)
TERRA    = (0.6, 8.0, 2.0, COR_TERRA)
MARTE    = (0.4, 9.5, 1.6, COR_MARTE)
JUPITER  = (1.5, 12.5, 0.8, COR_JUPITER)
SATURNO  = (1.2, 16.0, 0.5, COR_SATURNO, True, COR_ANEL_SATURNO)
URANO    = (0.9, 19.0, 0.3, COR_URANO)
NETUNO   = (0.8, 22.0, 0.2, COR_NETUNO)

# Satélites naturais
#Terra
LUA = (0.15, 1.0, 5.0, COR_LUA)
#Marte
FOBOS     = (0.05, 0.4, 8.0, COR_FOBOS)
DEIMOS    = (0.03, 0.8, 6.0, COR_DEIMOS)
#Jupiter
IO        = (0.18, 2.0, 12.0, COR_IO)
EUROPA    = (0.15, 3.2,  9.0, COR_EUROPA)
GANIMEDES = (0.25, 5.0,  6.0, COR_GANIMEDES)
CALISTO   = (0.23, 8.8,  4.0, COR_CALISTO)
#Saturno
TITA      = (0.24, 6.5,  4.5, COR_TITA)
ENCELADO  = (0.08, 2.5,  8.5, COR_ENCELADO)
REIA      = (0.10, 3.8,  6.5, COR_REIA)
#Urano
TITANIA   = (0.11, 3.5,  5.0, COR_TITANIA)
OBERON    = (0.10, 4.6,  4.0, COR_OBERON)
MIRANDA   = (0.06, 1.8,  7.5, COR_MIRANDA)
#Netuno
TRITAO    = (0.16, 3.0,  6.0, COR_TRITAO)


#Outro sistema
COR_ESTRELA_AZUL = (0.3, 0.5, 1.0)
COR_PLANETA_1 = (0.4, 0.9, 0.4)
COR_PLANETA_2 = (0.8, 0.2, 0.5) 
COR_SATELITE = (0.8, 0.8, 0.9)
COR_ANEL_1 = (0.9, 0.6, 0.8)

ESTRELA_AZUL = (3.0, 27.0, 0.15, COR_ESTRELA_AZUL) 

PLANETA_1 = (0.6, 4.5, 1.2, COR_PLANETA_1)
PLANETA_2 = (0.8, 8.5, 0.5, COR_PLANETA_2, True, COR_ANEL_1)

SATELITE = (0.2, 1.5, 3.0, COR_SATELITE)

#Outro sistema
COR_ANA_VERMELHA = (0.8, 0.1, 0.1) 
COR_PLANETA_LAVA = (1.0, 0.3, 0.0)    
COR_PLANETA_ROCO = (0.5, 0.4, 0.3)    
COR_PLANETA_GELO = (0.6, 0.8, 0.9)   
COR_ANEL_GELO    = (0.8, 0.9, 1.0)

ANA_VERMELHA = (2.5, 105.0, 0.02, COR_ANA_VERMELHA)

PLANETA_LAVA = (0.4, 3.5, 3.0, COR_PLANETA_LAVA)
PLANETA_ROCO = (0.6, 6.0, 1.8, COR_PLANETA_ROCO)
PLANETA_GELO = (0.8, 10.0, 0.7, COR_PLANETA_GELO, True, COR_ANEL_GELO)


# INTERFACE DE USUÁRIO
INSTRUCOES = [
            "PLANETARIO INTERATIVO",
            "",
            "Movimentação: W, A, S, D, Espaço, shift + Mouse",
            "Pausa: Botao Direito do Mouse",
            "Tela Cheia: F11",
            "Fechar: ESC",
            "",
            "CLIQUE PARA INICIAR"
        ]

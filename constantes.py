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

# Cores dedicadas para geometria adicional (discos de acreção e anéis planetários)
COR_ANEL_BURACO_NEGRO = (1.0, 0.4, 0.0)
COR_ANEL_SATURNO = (0.7, 0.6, 0.5)

# PARÂMETROS GERAIS
QUANT_ESTRELAS = 1000
FPS = 30

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
LUA = (0.15, 1.0, 5.0, COR_LUA)

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
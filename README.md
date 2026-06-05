# Planetário Interativo 3D 🪐

Simulação interativa do sistema solar em 3D desenvolvida em Python, focada em renderização gráfica e física orbital hierárquica.

## 🚀 Dependências

Certifique-se de ter o Python instalado e execute o comando abaixo para instalar as bibliotecas necessárias:

```bash
pip install pygame PyOpenGL
```

## 🎮 Como Executar
Execute o arquivo principal no terminal:
```bash
python main.py
```

## ⌨️ Controles

| Ação | Comando |
| :--- | :--- |
| **Movimentar (Frente, Trás, Esquerda, Direita)** | `W`, `A`, `S`, `D` |
| **Subir** | `Espaço` |
| **Descer** | `Shift Esquerdo` |
| **Olhar ao redor** | `Mouse` |
| **Pausar / Despausar Simulação** | `Botão Direito do Mouse` |
| **Alternar Tela Cheia** | `F11` |
| **Fechar o Programa** | `ESC` |

## 📂 Estrutura do Projeto
> A arquitetura do código foi dividida de forma modular para separar a lógica de física, a configuração gráfica e o loop principal:
> 
> main.py: O coração da aplicação. Gerencia o game loop, inicializa o contexto OpenGL, controla os estados do jogo (Menu vs. Simulação) e > escuta os eventos do teclado e mouse.
> 
> classes.py: Contém a classe CorpoCeleste. É aqui que a mágica da renderização hierárquica acontece. Utilizando glPushMatrix() e        > glPopMatrix(), garantimos que a translação e rotação de um planeta afetem seus satélites, mas não afetem os outros planetas do sistema > solar.
> 
> funcoes.py: Agrupa as funções utilitárias do projeto. Inclui cálculos trigonométricos (seno e cosseno) para traduzir a rotação da      > câmera (Yaw/Pitch) em vetores de movimento 3D direcional. Também lida com a geração da textura que permite escrever texto 2D na tela do > OpenGL.

> constantes.py: Centraliza todos os dados do sistema solar (tamanho, velocidade de translação, distância e cor dos corpos celestes),    > além de configurações da engine (FPS, cores base, sensibilidade do mouse).

## 🧠 Conceitos Técnicos Aplicados
> Matrizes de Transformação: O projeto evita calcular coordenadas cartesianas exatas (x, y, z) manualmente para a órbita de cada planeta. > Em vez disso, o OpenGL manipula o próprio "universo" através de rotações de eixo (glRotatef) e translações (glTranslatef), delegando a > matemática pesada para a API gráfica.
> 
> Textura a partir de Superfícies: Como o OpenGL puro não desenha textos com facilidade, foi implementada uma técnica de Texturização    > Dinâmica, onde o Pygame desenha o texto em uma superfície transparente, a converte para uma string de pixels e a envia como textura    > para um quadrilátero 2D (GL_QUADS) renderizado de forma ortográfica (glOrtho) sobre a tela.
> 
> Z-Buffer (Depth Test): Utilização do GL_DEPTH_TEST para garantir que os corpos celestes mais próximos à câmera ocultem os que estão    > mais distantes, criando o efeito de oclusão e profundidade realista.

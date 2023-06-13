import pygame
import random
import datetime
import mysql.connector
import os

#especifica a pasta WizardCode como a pasta atual
os.chdir(r".\jogo\WizardCode")

# conecta ao banco de dados 
dbperguntas = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mamacosma2!",
    database="jogo")

# define o cursor
cursor = dbperguntas.cursor()

# função que pega um valor aleatorio de cada linha e coloca em uma variavel

def perguntaAleatoriaSQL():
    cursor.execute("SELECT * FROM perguntas WHERE materia = 'Banco de Dados (SQL)' ORDER BY RAND() LIMIT 1")
    linhas = cursor.fetchall()
    linha = random.choice(linhas)
    txt = linha[0]
    alt1 = linha[1]
    alt2 = linha[2]
    alt3 = linha[3]
    alt4 = linha[4]
    resp = linha[5]
    materia = linha[6]
    return txt, alt1, alt2, alt3, alt4, resp, materia

def perguntaAleatoriaPython():
    cursor.execute("SELECT * FROM perguntas WHERE materia = 'Python' ORDER BY RAND() LIMIT 1")
    linhas = cursor.fetchall()
    linha = random.choice(linhas)
    txt = linha[0]
    alt1 = linha[1]
    alt2 = linha[2]
    alt3 = linha[3]
    alt4 = linha[4]
    resp = linha[5]
    materia = linha[6]
    return txt, alt1, alt2, alt3, alt4, resp, materia

def perguntaAleatoriaJava():
    cursor.execute("SELECT * FROM perguntas WHERE materia = 'Java' ORDER BY RAND() LIMIT 1")
    linhas = cursor.fetchall()
    linha = random.choice(linhas)
    txt = linha[0]
    alt1 = linha[1]
    alt2 = linha[2]
    alt3 = linha[3]
    alt4 = linha[4]
    resp = linha[5]
    materia = linha[6]
    return txt, alt1, alt2, alt3, alt4, resp, materia


alternativa = 0
# CORES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# RECT = RETANGULO = HITBOX RETANGULAR
class Livros(pygame.sprite.Sprite):
    def __init__(self, imagem): # ATRIBUTOS
        super().__init__()
        self.image = imagem
        self.rect = self.image.get_rect()

    def reset_pos(self): # MÉTODO
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, LARGURA)

    def update(self): # MÉTODO
        self.rect.y += 3
        if self.rect.y > 650:
            self.reset_pos()


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self): # ATRIBUTOS
        super().__init__()
        self.image = obst_image
        self.rect = self.image.get_rect()

    def reset_pos(self): # MÉTODO
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, LARGURA)

    def update(self): # MÉTODO
        self.rect.y += 3
        if self.rect.y > 650:
            self.reset_pos()

class Player(pygame.sprite.Sprite):
    def __init__(self): # ATRIBUTOS
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()

    def update(self): # MÉTODO
        pos = [x_coord, y_coord]
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def mudar_imagem(self, nova_imagem):
        self.image.fill((0, 0, 0))  # REMOVE A PRIMEIRA SKIN
        player_image.set_colorkey(BLACK)
        self.image = pygame.image.load(nova_imagem).convert_alpha()
    
    def converterTempo(segundos):
        tempo = str(datetime.timdelta(seconds=segundos))
        return tempo
    
    def atualizar_informacoes(self):
        # Renderiza o texto para cada informação
        texto_vidas = fonte.render("Vidas: " + str(vidas), True, (255, 255, 255))  # Preto
        texto_acertos = fonte.render("Acertos: " + str(acertos), True, (255, 255, 255))
        texto_cronometro = fonte.render(f"Tempo: {datetime.timedelta(seconds=cronometro *-1)}", True, (255, 255, 255))
        # Posiciona os textos na tela
        TELA.blit(texto_acertos, (10, 10))
        TELA.blit(texto_vidas, (10, 50))
        TELA.blit(texto_cronometro, (10, 90))
        
# INICIO DO JOGO--------------------------------------------------------------------------------------------
pygame.init()
LARGURA = 1200
ALTURA = 900
TAMANHO = [LARGURA, ALTURA]
TELA = pygame.display.set_mode(TAMANHO)
question_surface = pygame.Surface((1050, 300))  # cria uma nova surface para a tela de pergunta
question_image = pygame.image.load("FundoPergunta.png").convert()
cont_vida = 0
acertos = 0
resposta = 0
erros = acertos -1
vidas = 3

#CRONOMETRO
tempo_jogo = 0 # a partir de que numero o "timer" começa a contar
cronometro = tempo_jogo
pygame.time.set_timer(pygame.USEREVENT, 1000) # em milissegundos 

# TRANSFORMA AMBAS LISTAS EM SPRITES
# SPRITES(LIVROS)
sql_list = pygame.sprite.Group()
py_list = pygame.sprite.Group()
java_list = pygame.sprite.Group()


# SPRITES(OBSTÁCULOS)
obst_list = pygame.sprite.Group()

# LISTA COM TODAS AS SPRITES
all_sprites_list = pygame.sprite.Group()

# NOME DA TELA
pygame.display.set_caption('CODE WIZARD')

clock = pygame.time.Clock()

# IMAGENS
background_position = [0, 0]
background_image = pygame.image.load("fundo.png").convert()
player_image = pygame.image.load("spriteFazendeiro.png").convert_alpha()
book_imageSQL = pygame.image.load("LivroSql.png").convert()
book_imageJava = pygame.image.load("LivroJava.png").convert()
book_imagePy = pygame.image.load("LivroPython.png").convert()
obst_image = pygame.image.load("Bigorna.png").convert()
book_imageSQL.set_colorkey(BLACK)
book_imagePy.set_colorkey(BLACK)
book_imageJava.set_colorkey(BLACK)
obst_image.set_colorkey(BLACK)

# VELOCIDADE POR FRAME (ANDAR)
x_speed = 0
y_speed = 0

# POSIÇÃO ATUAL (JUNÇÃO COM ANDAR)
x_coord = 275
y_coord = 615

player = Player()
all_sprites_list.add(player)

# OBJETO LIVRO------------------------------------------------------------------------------------------------
for i in range(1):
    livro = Livros(book_imageSQL)

    # LOCALIZAÇÃO RANDOMICA P OBJETO
    livro.rect.x = random.randrange(LARGURA)
    livro.rect.y = random.randrange(-300, -20)
   

    # ADICIONA O OBJETO NA LISTA DE SPRITES
    sql_list.add(livro)

    all_sprites_list.add(livro)

for i in range(1):
    livro = Livros(book_imagePy)

    # LOCALIZAÇÃO RANDOMICA P OBJETO
    livro.rect.x = random.randrange(LARGURA)
    livro.rect.y = random.randrange(-300, -20)
   

    # ADICIONA O OBJETO NA LISTA DE SPRITES
    py_list.add(livro)

    all_sprites_list.add(livro)

for i in range(1):
    livro = Livros(book_imageJava)

    # LOCALIZAÇÃO RANDOMICA P OBJETO
    livro.rect.x = random.randrange(LARGURA)
    livro.rect.y = random.randrange(-300, -20)
   

    # ADICIONA O OBJETO NA LISTA DE SPRITES
    java_list.add(livro)

    all_sprites_list.add(livro)

for i in range(5):
    obstaculo = Obstaculo()

    # LOCALIZAÇÃO RANDOMICA P OBJETO
    obstaculo.rect.x = random.randrange(LARGURA)
    obstaculo.rect.y = random.randrange(-300, -20)

    # ADICIONA O OBJETO NA LISTA DE SPRITES
    obst_list.add(obstaculo)

    all_sprites_list.add(obstaculo)

tela_pergunta = False
# LOOP PRINCIPAL DO JOGO---------------------------------------------------------------------------------------
pause = False
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            # VERIFICA SE É UMA SETA
            # AJUSTA A VELOCIDADE
            if event.key == pygame.K_LEFT and x_coord > -1 and not pause:
                x_speed = -40
            elif event.key == pygame.K_RIGHT and x_coord < 1100 and not pause:
                x_speed = 40
            elif event.key == pygame.K_ESCAPE:  # Verificação da tecla ESC pressionada
                tela_pergunta = False
                pause = False
            elif event.key == pygame.K_1 and tela_pergunta:  # Verificação da tecla 1 pressionada
                tela_pergunta = False
                print("player apertou 1")
                resposta = 1
                pause = False
            elif event.key == pygame.K_2 and tela_pergunta:  # Verificação da tecla 2 pressionada
                tela_pergunta = False
                print("player apertou 2")
                resposta = 2
                pause = False
            elif event.key == pygame.K_3 and tela_pergunta:  # Verificação da tecla 3 pressionada
                tela_pergunta = False
                print("player apertou 3")
                resposta = 3
                pause = False
            elif event.key == pygame.K_4 and tela_pergunta:  # Verificação da tecla 4 pressionada
                tela_pergunta = False
                print("player apertou 4")
                resposta = 4
                pause = False

        elif event.type == pygame.KEYUP:
            # PARA DE ANDAR AO SOLTAR
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

        # ANDAR
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed

        #loop cronometro 
        if event.type == pygame.USEREVENT:
            cronometro -= 1

    # COPIA A IMAGEM NA TELA--------------------------------------------------------------------------------
    TELA.fill(WHITE)
    TELA.blit(background_image, background_position)
    TELA.blit(player_image, [x_coord, y_coord])

    # CHAMA O MÉTODO QUE MOVIMENTA OS LIVROS------------------------------------------------------------
    if not pause:
        all_sprites_list.update()

    # VERIFICA SE O JOGADOR COLIDIU COM ALGO-------------------------------------------------------
    sql_hit_list = pygame.sprite.spritecollide(player, sql_list, False)
    py_hit_list = pygame.sprite.spritecollide(player, py_list, False)
    java_hit_list = pygame.sprite.spritecollide(player, java_list, False)
    obst_hit_list = pygame.sprite.spritecollide(player, obst_list, False)

     # PERGUNTAS ----------------------------------------------------------------------------------
    pygame.font.init()
    txt, alt1, alt2, alt3, alt4, resp, materia = perguntaAleatoriaSQL()
    fonte = pygame.font.Font("Quicksand-Bold.ttf", 18)  
    fontemat = pygame.font.Font("Quicksand-Bold.ttf", 25)                   
    player.atualizar_informacoes()

    # acertou pergunta
    if resposta == alternativa and resposta != 0:
        acertos += 1
        resposta = 0
        cont_vida += 1
        print(acertos)
        print("Player acertou.")
        
    # errou pergunta
    if resposta is not None and resposta != alternativa and resposta != 0:
        resposta = 0
        vidas -= 1
        print(acertos)
        print("Player errou")

    # muda skin
    if 6 > acertos >= 3:
        player.mudar_imagem('SpritePescador.png')
    elif 9 > acertos >= 6:
        player.mudar_imagem('SpriteFerreiro.png')
    elif 12 > acertos >= 9:
        player.mudar_imagem('SpriteCavaleiro.png')
    elif acertos >= 12:
        player.mudar_imagem('SpriteMago.png')
    if vidas == -1:
        pygame.quit()

    # regenera vida a cada 3 perguntas
    if cont_vida % 3 == 0 and cont_vida != 0 and vidas != 3:
        vidas += 1
        cont_vida = 0
        

    # CHECA COLISÕES----------------------------------------------------------------------
    for livro in sql_hit_list:
        # ABRE PERGUNTA NA TELA
        txt, alt1, alt2, alt3, alt4, resp, materia = perguntaAleatoriaSQL()
        alternativa = resp
        materiatela = fontemat.render(materia, 1, WHITE)
        txttela = fonte.render(txt, 1, WHITE)
        alt1tela = fonte.render(alt1, 1, WHITE)
        alt2tela = fonte.render(alt2, 1, WHITE)
        alt3tela = fonte.render(alt3, 1, WHITE)
        alt4tela = fonte.render(alt4, 1, WHITE)
        print(txt, alt1, alt2, alt3, alt4, resp, materia)
        print("A resposta correta é: ", alternativa)
        tela_pergunta = True
        # RESETA PARA O INICIO DA TELA
        livro.reset_pos()
    all_sprites_list.draw(TELA)

    for livro in py_hit_list:
        # ABRE PERGUNTA NA TELA
        txt, alt1, alt2, alt3, alt4, resp, materia = perguntaAleatoriaPython()
        alternativa = resp
        materiatela = fontemat.render(materia, 1, WHITE)
        txttela = fonte.render(txt, 1, WHITE)
        alt1tela = fonte.render(alt1, 1, WHITE)
        alt2tela = fonte.render(alt2, 1, WHITE)
        alt3tela = fonte.render(alt3, 1, WHITE)
        alt4tela = fonte.render(alt4, 1, WHITE)
        print(txt, alt1, alt2, alt3, alt4, resp, materia)
        print("A resposta correta é: ", alternativa)
        tela_pergunta = True
        # RESETA PARA O INICIO DA TELA
        livro.reset_pos()

    all_sprites_list.draw(TELA)

    for livro in java_hit_list:
        # ABRE PERGUNTA NA TELA
        txt, alt1, alt2, alt3, alt4, resp, materia = perguntaAleatoriaJava()
        alternativa = resp
        materiatela = fontemat.render(materia, 1, WHITE)
        txttela = fonte.render(txt, 1, WHITE)
        alt1tela = fonte.render(alt1, 1, WHITE)
        alt2tela = fonte.render(alt2, 1, WHITE)
        alt3tela = fonte.render(alt3, 1, WHITE)
        alt4tela = fonte.render(alt4, 1, WHITE)
        print(txt, alt1, alt2, alt3, alt4, resp, materia)
        print("A resposta correta é: ", alternativa)
        tela_pergunta = True
        # RESETA PARA O INICIO DA TELA
        livro.reset_pos()
    all_sprites_list.draw(TELA)

    for obstaculo in obst_hit_list:
        vidas -= 1
        # RESETA PARA O INICIO DA TELA
        obstaculo.reset_pos()
    all_sprites_list.draw(TELA)

    # pergunta na tela
    if tela_pergunta:
        TELA.blit(question_surface, (80, 250))
        question_surface.blit(question_image, (0, 0))
        TELA.blit(materiatela, (130, 270))
        TELA.blit(txttela, (130, 330))
        TELA.blit(alt1tela, (140, 370))
        TELA.blit(alt2tela, (140, 410))
        TELA.blit(alt3tela, (140, 450))
        TELA.blit(alt4tela, (140, 490))
        pause = True

    # ATUALIZA A TELA
    pygame.display.flip()

    # FPS
    clock.tick(60)

# FECHA
pygame.quit()

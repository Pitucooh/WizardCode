import pygame
import random


# CORES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# RECT = RETANGULO = HITBOX RETANGULAR
class Livros(pygame.sprite.Sprite):
    def __init__(self): # ATRIBUTOS
        super().__init__()
        self.image = book_image
        self.rect = self.image.get_rect()

    def reset_pos(self): # MÉTODO
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, largura)

    def update(self): # MÉTODO
        self.rect.y += 1
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


# INICIO DO JOGO
pygame.init()
largura = 700
altura = 900
SIZE = [largura, altura]
screen = pygame.display.set_mode(SIZE)

# SPRITES(LIVROS)
block_list = pygame.sprite.Group()
# LISTA COM TODAS AS SPRITES
all_sprites_list = pygame.sprite.Group()

# NOME DA TELA
pygame.display.set_caption('Tentativa do jogo!')

clock = pygame.time.Clock()

# IMAGENS
background_position = [0, 0]
background_image = pygame.image.load("fundo.jpg").convert()
player_image = pygame.image.load("wizard.png").convert()
book_image = pygame.image.load("livro.png").convert()
player_image.set_colorkey(WHITE)
book_image.set_colorkey(BLACK)

# VELOCIDADE POR FRAME (ANDAR)
x_speed = 0
y_speed = 0

# POSIÇÃO ATUAL (JUNÇÃO COM ANDAR)
x_coord = 10
y_coord = 600

player = Player()
all_sprites_list.add(player)

for i in range(3):
    # This represents a block
    livro = Livros()

    # Set a random location for the block
    livro.rect.x = random.randrange(largura)
    livro.rect.y = random.randrange(altura)

    # Add the block to the list of objects
    block_list.add(livro)
    all_sprites_list.add(livro)


# LOOP PRINCIPAL DO JOGO
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            # VERIFICA SE É UMA SETA
            # AJUSTA A VELOCIDADE
            if event.key == pygame.K_LEFT:
                x_speed = -40
            elif event.key == pygame.K_RIGHT:
                x_speed = 40

        elif event.type == pygame.KEYUP:
            # PARA DE ANDAR AO SOLTAR
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

        # ANDAR
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed

    # COPIA A IMAGEM NA TELA
    screen.fill(WHITE)
    screen.blit(background_image, background_position)
    screen.blit(player_image, [x_coord, y_coord])

    # CHAMA O MÉTODO QUE MOVIMENTA OS LIVROS
    all_sprites_list.update()

    # VERIFICA SE O JOGADOR COLIDIU COM ALGO
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)

    # CHECA COLISÕES
    for block in blocks_hit_list:
        # RESETA PARA O INICIO DA TELA
        block.reset_pos()
    all_sprites_list.draw(screen)

    # ATUALIZA A TELA
    pygame.display.flip()

    # FPS
    clock.tick(60)

# FECHA
pygame.quit()
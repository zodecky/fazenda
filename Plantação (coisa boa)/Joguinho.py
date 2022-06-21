import pygame
pygame.init()

global plataforma
global player
global player_rect
global speed
pode_pular = False
big_pulo = False

size = width, height = 1080, 720
speed = [0, 0]
max_speed = [9.5, 10]
ACELERACAO = 0.06
DESACELERACAO = 0.04
black = 0, 0, 0
clock = pygame.time.Clock()
tempo_pulo = 0
tempo_chao = 0

TEMPO_PULO = 7
TEMPO_BIG_PULO = 10
PULO = 0.2
AGUA = 5

screen = pygame.display.set_mode(size)

player = pygame.image.load(
    "/Users/Gabriel/Documents/GitHub/fazenda/Plantação (coisa boa)/Personagem.png")
player = pygame.transform.scale(player, (60, 60))
player_rect = player.get_rect()


def gravidade():
    speed[1] += 1


def pulo_minimo():
    speed[1] -= PULO * dt


def pulando():
    speed[1] -= PULO * dt


def draw():
    global plataforma
    plataforma = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(500, 500, 60, 60))


def colisao():
    global plataforma
    global player
    global player_rect
    if player_rect.colliderect(plataforma):
        global speed
        speed[1] -= AGUA


while True:

    clock.tick(60)
    dt = clock.get_time()
    gravidade()

    if player_rect.bottom > height:
        speed[1] = 0
        player_rect.bottom = height
        tempo_pulo = 0
        tempo_chao += 1
        if tempo_chao > 10:
            big_pulo = False
        pode_pular = True

    # Eventos pulo e exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pode_pular = False
                big_pulo = False
                if tempo_pulo < 5:
                    big_pulo = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pode_pular:
                    pulo_minimo()
                    tempo_chao = 0

    # Movimento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        speed[0] -= ACELERACAO * dt
    elif speed[0] < 0:
        speed[0] += DESACELERACAO * dt

    if keys[pygame.K_d]:
        speed[0] += ACELERACAO * dt
    elif speed[0] > 0:
        speed[0] -= DESACELERACAO * dt

    if keys[pygame.K_w]:
        pass
    if keys[pygame.K_s]:
        speed[1] += ACELERACAO * dt
    if keys[pygame.K_SPACE]:
        if big_pulo:
            tempo_pulo_variavel = TEMPO_BIG_PULO
        else:
            tempo_pulo_variavel = TEMPO_PULO
        if tempo_pulo < tempo_pulo_variavel and pode_pular:
            tempo_pulo += 1
            pulando()

            # Velocidade máxima
    if speed[0] > max_speed[0]:
        speed[0] = max_speed[0]
    elif speed[0] < -max_speed[0]:
        speed[0] = -max_speed[0]
    # print(tempo_pulo, big_pulo)

    player_rect = player_rect.move(speed)
    screen.fill(black)
    screen.blit(player, player_rect)
    draw()
    colisao()
    pygame.display.flip()

pygame.quit()
exit()

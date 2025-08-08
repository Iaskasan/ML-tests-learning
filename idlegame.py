import pygame
import sys

pygame.init()

# Configuration de la fenêtre
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Idle Game Simple")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 200)

# Font pour afficher le texte
font = pygame.font.SysFont(None, 40)

# Variables du jeu
score = 0
score_increment = 1
clock = pygame.time.Clock()

# Rect pour le bouton "Clique moi"
button_rect = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 2, 120, 50)

# Temps pour incrément automatique
AUTO_INCREMENT_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(AUTO_INCREMENT_EVENT, 1000)  # toutes les 1000 ms = 1 sec

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                score += score_increment
        
        elif event.type == AUTO_INCREMENT_EVENT:
            score += score_increment

    # On remplit l'écran en blanc
    screen.fill(WHITE)

    # Dessiner le bouton
    pygame.draw.rect(screen, BLUE, button_rect)
    button_text = font.render("Clique moi", True, WHITE)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

    # Afficher le score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

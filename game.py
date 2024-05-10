import pygames

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
largeur = 800
hauteur = 600
fenetre = pygame.display.set_mode((largeur, hauteur))

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

# Variables
dessiner = False
couleur = NOIR
epaisseur = 5

# Boucle principale
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      dessiner = True
    elif event.type == pygame.MOUSEBUTTONUP:
      dessiner = False
    elif event.type == pygame.MOUSEMOTION:
      if dessiner:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(fenetre, couleur, pos, epaisseur)

  # Affichage de la fenêtre
  pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
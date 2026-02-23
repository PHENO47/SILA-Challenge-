import pygame
import random
import json
import os

# =================================================================
# ⚙️ CONFIGURATION & CONSTANTES (Clean Code)
# =================================================================
WIDTH, HEIGHT = 800, 450
FPS = 60
GRAVITY = 0.8
FRICTION = -0.12
BOUNCE = 0.3
COLOR_PLAYER = (52, 152, 219)  # Bleu Flat Design
COLOR_ENEMY  = (231, 76, 60)   # Rouge Flat Design
COLOR_COIN   = (241, 196, 15)  # Or

# =================================================================
# 🧱 CLASSES TECHNIQUES
# =================================================================

class Projectile(pygame.sprite.Sprite):
    """ Gère les projectiles tirés par le joueur. """
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((12, 6))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 12 * direction

    def update(self):
        self.rect.x += self.speed
        if not (0 < self.rect.x < WIDTH):
            self.kill()

class Entity(pygame.sprite.Sprite):
    """ Classe mère gérant la physique AABB, la gravité et les rebonds. """
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)

    def apply_physics(self, platforms):
        """ Applique les forces de gravité, friction et gère les collisions. """
        # 1. Calcul des forces
        acc = pygame.math.Vector2(0, GRAVITY)
        acc.x += self.vel.x * FRICTION
        
        # 2. Intégration du mouvement
        self.vel += acc
        self.pos += self.vel + 0.5 * acc

        # 3. Résolution des collisions Horizontales (AABB)
        self.rect.x = self.pos.x
        for plat in platforms:
            if self.rect.colliderect(plat):
                if self.vel.x > 0: self.pos.x = plat.left - self.rect.width
                elif self.vel.x < 0: self.pos.x = plat.right
                self.vel.x *= -BOUNCE # Effet de rebond pro
                self.rect.x = self.pos.x

        # 4. Résolution des collisions Verticales (AABB)
        self.rect.y = self.pos.y
        for plat in platforms:
            if self.rect.colliderect(plat):
                if self.vel.y > 0: # Chute
                    self.pos.y = plat.top - self.rect.height
                    self.vel.y = 0
                elif self.vel.y < 0: # Saut (plafond)
                    self.pos.y = plat.bottom
                    self.vel.y *= -BOUNCE
                self.rect.y = self.pos.y

class Enemy(Entity):
    """ Ennemi avec IA de patrouille et poursuite. """
    def __init__(self, x, y):
        super().__init__(x, y, COLOR_ENEMY)
        self.speed = 2
        self.detection_range = 250

    def update(self, player, platforms):
        dist_x = player.pos.x - self.pos.x
        # IA : Si le joueur est proche, on le poursuit, sinon on patrouille
        if abs(dist_x) < self.detection_range:
            self.vel.x = self.speed * (1.5 if dist_x > 0 else -1.5)
        else:
            self.vel.x = self.speed
        
        self.apply_physics(platforms)
        # Changement de direction si mur touché
        if abs(self.vel.x) < 0.2: self.speed *= -1

# =================================================================
# 🚀 MOTEUR DE JEU PRINCIPAL
# =================================================================

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Platformer Pro Jour 6")
        self.clock = pygame.time.Clock()
        self.load_data()
        self.reset_game()

    def load_data(self):
        """ Charge le niveau JSON et le High Score persistant. """
        # High Score
        if os.path.exists("highscore.txt"):
            with open("highscore.txt", "r") as f: self.high_score = int(f.read())
        else: self.high_score = 0

        # Tilemap JSON
        with open("map.json", "r") as f:
            self.map_data = json.load(f)

    def reset_game(self):
        """ Réinitialise les groupes de sprites et le joueur. """
        self.platforms = [pygame.Rect(p['x'], p['y'], p['w'], p['h']) for p in self.map_data['platforms']]
        self.coins = pygame.sprite.Group()
        for c in self.map_data['coins']:
            coin = pygame.sprite.Sprite()
            coin.image = pygame.Surface((15, 15), pygame.SRCALPHA)
            pygame.draw.circle(coin.image, COLOR_COIN, (7, 7), 7)
            coin.rect = coin.image.get_rect(topleft=(c['x'], c['y']))
            self.coins.add(coin)

        self.enemies = pygame.sprite.Group()
        for e in self.map_data['enemies']: self.enemies.add(Enemy(e['x'], e['y']))
        
        self.projectiles = pygame.sprite.Group()
        self.player = Entity(100, 100, COLOR_PLAYER)
        self.score = 0
        self.facing = 1

    def handle_input(self):
        """ Gestion hybride PC (Clavier) + Mobile (Tactile). """
        # --- Contrôles PC ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  self.player.vel.x = -6; self.facing = -1
        if keys[pygame.K_RIGHT]: self.player.vel.x = 6;  self.facing = 1
        
        # --- Contrôles Mobile (Touch Zones) ---
        m_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            mx, my = m_pos
            if mx < WIDTH // 3: # Gauche
                self.player.vel.x = -6; self.facing = -1
            elif mx > 2 * WIDTH // 3: # Droite
                self.player.vel.x = 6; self.facing = 1
            
            # Zone Centrale = Saut
            if (WIDTH // 3 < mx < 2 * WIDTH // 3) and self.player.vel.y == 0:
                self.player.vel.y = -16

    def update(self):
        """ Mise à jour de la logique et détection des collisions. """
        self.player.apply_physics(self.platforms)
        self.enemies.update(self.player, self.platforms)
        self.projectiles.update()

        # Collisions : Collecte de pièces
        if pygame.sprite.spritecollide(self.player, self.coins, True):
            self.score += 10

        # Collisions : Tir sur ennemis
        pygame.sprite.groupcollide(self.projectiles, self.enemies, True, True)

        # Collisions : Joueur / Ennemi (Game Over)
        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            self.save_high_score()
            self.reset_game()

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as f: f.write(str(self.high_score))

    def draw(self):
        """ Rendu graphique. """
        self.screen.fill((44, 62, 80)) # Fond gris-bleu foncé
        
        # Dessin des plateformes
        for plat in self.platforms:
            pygame.draw.rect(self.screen, (39, 174, 96), plat)
        
        self.coins.draw(self.screen)
        self.enemies.draw(self.screen)
        self.projectiles.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)

        # Affichage Score
        font = pygame.font.SysFont("Arial", 24, bold=True)
        txt = font.render(f"Score: {self.score}  |  High: {self.high_score}", True, (255, 255, 255))
        self.screen.blit(txt, (20, 20))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.player.vel.y == 0:
                        self.player.vel.y = -16
                    if event.key == pygame.K_LCTRL:
                        self.projectiles.add(Projectile(self.player.rect.centerx, self.player.rect.centery, self.facing))
            
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    Game().run()
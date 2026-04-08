import pygame
import random
from src.config import WHITE, FONT_PATH

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.vx = random.uniform(-6, 6)
        self.vy = random.uniform(-6, 6)
        self.lifetime = 255 

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.15 
        self.lifetime -= 5 

    def draw(self, screen):
        if self.lifetime > 0:
            s = pygame.Surface((6, 6), pygame.SRCALPHA)
            pygame.draw.circle(s, (*self.color, self.lifetime), (3, 3), 3)
            screen.blit(s, (int(self.x), int(self.y)))

class Firework:
    def __init__(self, x, y):
        self.particles = []
        colors = [(255, 50, 50), (50, 255, 50), (80, 80, 255), (255, 255, 50), (255, 50, 255)]
        color = random.choice(colors)
        for _ in range(60):
            self.particles.append(Particle(x, y, color))

    def update(self):
        for p in self.particles: p.update()
        self.particles = [p for p in self.particles if p.lifetime > 0]

    def draw(self, screen):
        for p in self.particles: p.draw(screen)

class GUIManager:
    def __init__(self, screen):
        self.screen = screen
        try:
            self.font_main = pygame.font.Font(FONT_PATH, 45)
            self.font_small = pygame.font.Font(FONT_PATH, 25)
        except:
            self.font_main = pygame.font.SysFont("Arial", 45, bold=True)
            self.font_small = pygame.font.SysFont("Arial", 25)

    def draw_text(self, text, x, y, color=WHITE, center=False):
        text_surface = self.font_main.render(text, True, color)
        text_rect = text_surface.get_rect()
        if center: text_rect.center = (x, y)
        else: text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_balance(self, balance):
        text = f"Số dư: {balance:,} VNĐ"
        text_surface = self.font_small.render(text, True, (0, 255, 0))
        self.screen.blit(text_surface, (30, 30))
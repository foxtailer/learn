from config import FONT, pygame


class MyCounter:
    def __init__(self, pos, size, start):
        self.value = start
        self.position = pos
        self.size = size
        self.rect = pygame.Rect(pos, size)
        self._render_surface()

    def _render_surface(self):
        self.surface = pygame.Surface(self.size)
        self.surface.fill((200, 200, 200))
        text_surf = FONT.render(str(self.value), True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        self.surface.blit(text_surf, text_rect)


    def update(self):
        self.value += 1
        self._render_surface()

    def back(self):
        self.value -= 2
        self._render_surface()

    def draw(self, screen):
        screen.blit(self.surface, self.rect.topleft)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
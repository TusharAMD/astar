import pygame


class Font:
    def __init__(self, normal, italic):
        self.normal = normal
        self.italic = italic

    def get(self, size: int, is_italic=False):
        return pygame.font.Font(self.italic if is_italic else self.normal, size)


class Roboto:
    BLACK = Font('assets/fonts/Roboto-Black.ttf', 'assets/fonts/Roboto-BlackItalic.ttf')
    BOLD = Font('assets/fonts/Roboto-Bold.ttf', 'assets/fonts/Roboto-BoldItalic.ttf')
    MEDIUM = Font('assets/fonts/Roboto-Medium.ttf', 'assets/fonts/Roboto-MediumItalic.ttf')
    LIGHT = Font('assets/fonts/Roboto-Light.ttf', 'assets/fonts/Roboto-LightItalic.ttf')
    THIN = Font('assets/fonts/Roboto-Thin.ttf', 'assets/fonts/Roboto-ThinItalic.ttf')

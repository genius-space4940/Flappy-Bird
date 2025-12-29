from pygame import *

class Button():
    def __init__(self, width, height, x, y, color, font, text, border_radius=16):
        self.rect = Rect(width, height, x, y)
        self.color = color
        self.font = font
        self.text = text
        self.text_color = tuple(min(255, i - 60) for i in self.color)
        self.border_radius = border_radius
        self.hover_color = tuple(min(255, i + 40) for i in self.color)
        self.hover_text_color = tuple(min(255, i + 40) for i in self.text_color)

    def show(self, window):
        if self.rect.collidepoint(mouse.get_pos()):
            draw.rect(window, self.hover_color, self.rect, border_radius=self.border_radius)
            text_btn = self.font.render(self.text, True, self.hover_text_color)
            mouse.set_cursor(SYSTEM_CURSOR_HAND)

        else:
            draw.rect(window, self.color, self.rect, border_radius=self.border_radius)
            text_btn = self.font.render(self.text, True, self.text_color)
            mouse.set_cursor(SYSTEM_CURSOR_ARROW)

        text_cords = text_btn.get_rect(center=self.rect.center)

        window.blit(text_btn, text_cords)

    def is_hovered(self):
        return self.rect.collidepoint(mouse.get_pos())
    
    def is_clicked(self, events):
        for event in events:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return True
                
        return False

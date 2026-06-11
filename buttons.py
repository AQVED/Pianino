from settings import WHITE, GREY,BLACK
from pygame import Rect, mouse, draw, MOUSEBUTTONDOWN

class Button:
    def __init__(self,x, y, w, h, text, action=None, img_idle=None,img_hover=None,center=False):
        #self.rect = Rect(x,y,w,h)
        self.text = text
        self.action = action

        self.img_idle = img_idle
        self.img_hover = img_hover
        self.use_image = img_idle is not None


        self.idle = GREY
        self.hover = (180,180,180)
        self.border = BLACK
        self.text_color = BLACK

        if self.use_image and (w is None or h is None):
            iw, ih = self.img_idle.get_size()
            w = w or iw
            h = h or ih

        if center:
            self.rect = Rect(0,0,w,h)
            self.rect.center = (x,y)
        else:
            self.rect = Rect(x,y,w,h)

    def draw(self, screen, font):
        mouse_pos = mouse.get_pos()
        hovered = self.rect.collidepoint(mouse_pos)

        if self.use_image:
            surf = (self.img_hover if (hovered and self.img_hover)else self.img_idle)
            if surf.get_size() != (self.rect.w, self.rect.h):
                surf = transform.scale(surf, (self.rect.w, self.rect.h))#type:ignore
            screen.blit(surf,self.rect.topleft)

            if self.text:
                text_surf = font.render(self.text, 1, self.text_color)
                text_rect = text_surf.get_rect(center=self.rect.center)
                screen.blit(text_surf, text_rect)
        else:
            color = self.hover if self.rect.collidepoint(mouse_pos) else self.idle
            draw.rect(screen,color,self.rect)
            draw.rect(screen, self.border, self.rect, 2)

            if self.text:
                text_surf = font.render(self.text, 1, self.text_color)
                text_rect = text_surf.get_rect(center=self.rect.center)
                screen.blit(text_surf, text_rect)


    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.action:
                self.action()
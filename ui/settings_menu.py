from pygame import *
from buttons import Button
from ui.slider import Slider

class SettingsMenu:
    def __init__(self,screen_rect, initial_volume, initial_keys, min_keys, max_keys, on_change, on_back):
        self.screen_rect = screen_rect
        self.on_change = on_change
        self.on_back = on_back

        cx = screen_rect.centerx
        top = 140
        back_idle = transform.scale(image.load('assets/images/buttons/exit_unhover.png'),(48,48))
        back_hover = transform.scale(image.load('assets/images/buttons/exit_hover.png'),(48,48))
        
        self.back_btn = Button(40,30,48,48,'',self._back,back_idle,back_hover)


        def volume_to_text(v):
            return f"{int(v*100)}%"
        
        self.volume_slider = Slider(cx-200,top,400,0.0,1.0,step=0.01,initial=initial_volume,label='гучність',value_to_text=volume_to_text)
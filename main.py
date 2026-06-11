from random import choice
from pygame import *
from settings import *
from sounds import load_sounds
from keys import draw_keys, create_key_rects
from buttons import Button
#from ui.settings_menu import SettingsMenu
#
#

init()
sounds = load_sounds(KEYS)
all_sounds_list = list(sounds.values())
GEN_DIR = "assets/data/sounds"
generated_sounds = {}

key_rects = create_key_rects(len(KEYS))
key_list = list(KEYS.keys())
my_font = font.SysFont("Arial",24)
pressed_keys = set()


screen_mode = 'main'
settings_menu = None
random_toggle = None
use_random_sounds = False

current_volume = 1.0 #1.0 - 100% 1.5 - 150% 0.5 - 50%
for s in sounds.values():
    try:
        s.set_volume(current_volume)
    except Exception:
        pass


#
#
#
#
#

buttons = [Button(
    60,20,50,50,'',
    open_settins, # type: ignore
    img_idle = SETTINGS_IDLE, # type: ignore
    img_hover = SETTINGS_HOVER # type: ignore
)]

running = True
while running:
    screen.fill('white')
    if screen_mode == 'settings' and settings_menu:
        settings_menu.draw(screen, my_font)
        if random_toggle:
            random_toggle.draw(screen,my_font)
    else:
        for button in buttons:
            button.draw(screen, my_font)
        draw_keys(screen,key_rects, pressed_keys)

    display.flip()
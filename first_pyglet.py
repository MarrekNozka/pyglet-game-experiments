#!/usr/bin/env python3
# Soubor:  asteroids.py
# Datum:   01.04.2018 19:00
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
############################################################################
import random
import pyglet
import math


window = pyglet.window.Window()


hand_image = pyglet.image.load('ship.png')
hand_sprite = pyglet.sprite.Sprite(hand_image)


class SpaceShip:
    def __init__(self):
        self.speed = 10


def tik(t):
    hand_sprite.x = hand_sprite.x + t * 20
    hand_sprite.y = hand_sprite.y + 20 * math.sin(hand_sprite.x / 5)


def on_text_handler(text):
    # hand_sprite.x = random.randint(1, 500)
    # hand_sprite.y = random.randint(1, 500)
    hand_sprite.rotation += 30


def mouse_press_handler(x, y, button, mod):
    print(button, mod)
    hand_sprite.x = x
    hand_sprite.y = y


def on_draw_handler():
    window.clear()
    hand_sprite.draw()


window.push_handlers(
        on_text=on_text_handler,
        on_draw=on_draw_handler,
        on_mouse_press=mouse_press_handler,
)
pyglet.clock.schedule_interval(tik, 1/30)


pyglet.app.run()

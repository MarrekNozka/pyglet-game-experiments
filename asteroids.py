#!/usr/bin/env python3
# Soubor:  asteroids.py
# Datum:   01.04.2018 19:00
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
############################################################################
from math import sin, cos, radians, pi

import pyglet
from pyglet.window.key import LEFT, RIGHT, UP, DOWN

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

ACCELERATION = 78
ROTATION_SPEED = 88


def sprite_proxy(attr: str):
    def set_(self: "SpaceShip", new):
        setattr(self.sprite, attr, new)

    def get_(self: "SpaceShip"):
        return getattr(self.sprite, attr)

    return property(fget=get_, fset=set_)


class SpaceShip(object):
    x = sprite_proxy('x')
    y = sprite_proxy('y')
    rotation = sprite_proxy('rotation')

    def __init__(self, window=window, batch=batch):
        self.keys = set()

        self.image = pyglet.image.load('ship.png')
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)

        self.speed = 100

        self.x = self.y = 0
        self.rotation = 45

        # self.x = randint(0, window.width)
        # self.y = randint(0, window.height)
        # self.rotation = randint(0, 360)

    def tick(self, dt):
        self.x += dt * self.speed * cos(pi / 2 - radians(self.rotation))
        self.y += dt * self.speed * sin(pi / 2 - radians(self.rotation))
        for sym in self.keys:
            if sym == LEFT:
                self.rotation -= ROTATION_SPEED * dt
            elif sym == RIGHT:
                self.rotation += ROTATION_SPEED * dt
            elif sym == UP:
                self.speed += ACCELERATION * dt
            elif sym == DOWN:
                self.speed -= ACCELERATION * dt
                if self.speed < 0:
                    self.speed = 0


ship = SpaceShip()


def tik(dt):
    ship.tick(dt)


@window.event
def on_text(text):
    # hand_sprite.x = random.randint(1, 500)
    # hand_sprite.y = random.randint(1, 500)
    ship.rotation += 30


@window.event
def on_key_press(sym, mod):
    ship.keys.add(sym)


@window.event
def on_key_release(sym, mod):
    ship.keys.remove(sym)


@window.event
def on_mouse_press(x, y, button, mod):
    print(button, mod)
    ship.x = x
    ship.y = y


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.clock.schedule_interval(tik, 1 / 30)

pyglet.app.run()

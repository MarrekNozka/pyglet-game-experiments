#!/usr/bin/env python3
# Soubor:  asteroids.py
# Datum:   01.04.2018 19:00
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
############################################################################
from math import sin, cos, radians, pi
from random import randint

import pyglet
from pyglet.window.key import LEFT, RIGHT, UP, DOWN

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

ACCELERATION = 78
ROTATION_SPEED = 88


class SpaceShip(object):
    def __init__(self, window=window, batch=batch):
        self._x = self._y = 0
        self._rotation = 45

        self.keys = set()

        self.image = pyglet.image.load('ship.png')
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)
        self.sprite.rotation = self._rotation

        self.speed = 100
        # self.x = randint(0, window.width)
        # self.y = randint(0, window.height)
        # self.rotation = randint(0, 360)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new):
        self._x = self.sprite.x = new

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new):
        self._y = self.sprite.y = new

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, new):
        self._rotation = self.sprite.rotation = new

    def tick(self, dt):
        self.x += dt * self.speed * cos(pi / 2 - radians(self._rotation))
        self.y += dt * self.speed * sin(pi / 2 - radians(self._rotation))
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

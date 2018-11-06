#!/usr/bin/env python3
# Soubor:  asteroids.py
# Datum:   6.11.2018 00:00
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
############################################################################
from math import sin, cos, radians, pi
from random import randint, choice

import pyglet

window = pyglet.window.Window(1000, 800)
batch = pyglet.graphics.Batch()


class Stone(object):
    def __init__(self, window=window, batch=batch):
        self._x = randint(0, window.width)
        self._y = randint(0, window.height)
        self._rotation = randint(0, 360)
        self.speed = randint(30, 150)
        self.rspeed = randint(-50, 50)

        num = choice(range(0, 20))
        self.image = pyglet.image.load('meteors/{}.png'.format(num))
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)
        self.sprite.rotation = self._rotation

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
        self.sprite.rotation += dt * self.rspeed
        self.x += dt * self.speed * cos(pi / 2 - radians(self.rotation))
        self.y += dt * self.speed * sin(pi / 2 - radians(self.rotation))


stones = []
for i in range(50):
    stone = Stone()
    stones.append(stone)
    pyglet.clock.schedule_interval(stone.tick, 1 / 30)


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.app.run()

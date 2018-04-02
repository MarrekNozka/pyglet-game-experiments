#!/usr/bin/env python3
# Soubor:  asteroids.py
# Datum:   01.04.2018 19:00
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
############################################################################
from random import randint
from math import sin, cos, radians, pi
import pyglet
from pyglet.window.key import LEFT, RIGHT, UP, DOWN


window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

ACCELERATION = 78
ROTATTION_SPEED = 123


class SpaceShip:
    def __init__(self, window=window, batch=batch):
        self.image = pyglet.image.load('ship.png')
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)

        self.x = randint(0, window.width)
        self.x = 0
        self.y = randint(0, window.height)
        self.y = 0
        self.speed = 100
        self.rotation = randint(0, 360)
        self.rotation = 45

        self.keys = set()

    def __setattr__(self, name, value):

        self.__dict__[name] = value

        if name == 'x':
            self.sprite.x = value
        elif name == 'y':
            self.sprite.y = value
        elif name == 'rotation':
            self.sprite.rotation = value

    def tick(self, dt):
        self.x += dt * self.speed * cos(pi/2 - radians(self.rotation))
        self.y += dt * self.speed * sin(pi/2 - radians(self.rotation))
        for sym in self.keys:
            if sym == LEFT:
                ship.rotation -= ROTATTION_SPEED * dt
            elif sym == RIGHT:
                ship.rotation += ROTATTION_SPEED * dt
            elif sym == UP:
                ship.speed += ACCELERATION * dt
            elif sym == DOWN:
                ship.speed -= ACCELERATION * dt
                if ship.speed < 0:
                    ship.speed = 0


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
    ship.sprite.x = x
    ship.sprite.y = y


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.clock.schedule_interval(tik, 1/30)

pyglet.app.run()

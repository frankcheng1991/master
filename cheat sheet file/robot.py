from vpython import *
#from robot import *
import random
import math
import ipywidgets as widgets

class GenericBot:
def __init__(self, position = vector(0, 0, 0),
             heading = vector(0, 0, 1), speed = 1):
    self.position = position
    self.heading = heading.norm()
    self.speed = speed
    self.parts = []

def update(self):
    self.turn(0)
    self.forward()

def turn(self, angle):
    # convert angle from degrees to radians (VPython
    # assumes all angles are in radians)
    theta = math.radians(angle)
    self.heading = rotate(self.heading, angle = theta, axis = vector(0, 1, 0))
    for part in self.parts:
        part.rotate(angle = theta, axis = vector(0, 1, 0),
                    origin = self.position)

def forward(self):
    self.position += self.heading * self.speed
    for part in self.parts:
        part.pos += self.heading * self.speed

class ZombieBot(GenericBot):
def __init__(self, position = vector(0, 0, 0),
             heading = vector(0, 0, 1)):
    GenericBot.__init__(self, position, heading)
    self.body = cylinder(pos = self.position,
                         axis = vector(0, 4, 0),
                         radius = 1,
                         color = vector(0, 1, 0))
    self.arm1 = cylinder(pos = self.position + vector(0.6, 3, 0),
                         axis = vector(0, 0, 2),
                         radius = .3,
                         color = vector(1, 1, 0))
    self.arm2 = cylinder(pos = self.position + vector(-0.6, 3, 0),
                         axis = vector(0, 0, 2),
                         radius = .3,
                         color = vector(1, 1, 0))
    self.halo = ring(pos = self.position + vector(0, 5, 0),
                         axis = vector(0, 1, 0),
                         radius = 1,
                         color = vector(1, 1, 0))
    self.head = sphere(pos = self.position + vector(0, 4.5, 0),
                         radius = 0.5,
                         color = vector(1, 1, 1))
    self.parts = [self.body, self.arm1, self.arm2,
                  self.halo, self.head]

def update(self):
    # call turn with a random angle between -5 and 5
    # degrees
    self.turn(random.uniform(-5, 5))
    self.forward()

class PlayerBot(GenericBot):
def __init__(self, position = vector(0, 0, 0),
             heading = vector(0, 0, 1)):
    GenericBot.__init__(self, position, heading)
    self.body = cylinder(pos = self.position + vector(0, 0.5, 0),
                           axis = vector(0, 6, 0),
                           radius = 1,
                           color = vector(1, 0, 0))
    self.head = box(pos = vector(0, 7, 0) + self.position,
                           length = 2,
                           width = 2,
                           height = 2,
                           color = vector(0, 1, 0))
    self.nose = cone(pos = vector(0, 7, 1) + self.position,
                           radius = 0.5,
                           axis = vector(0, 0, 1),
                           color = vector(1, 1, 0))
    self.wheel1 = cylinder(pos = self.position + vector(1, 1, 0),
                           axis = vector(0.5, 0, 0),
                           radius = 1,
                           color = vector(0, 0, 1))
    self.wheel2 = cylinder(pos = self.position + vector(-1, 1, 0),
                           axis = vector(-0.5, 0, 0),
                           radius = 1,
                           color = vector(0, 0, 1))
    self.parts = [self.body, self.head, self.nose,
                  self.wheel1, self.wheel2]

def update(self):
    self.turn(0) # we'll leave the turn handling up to our buttons...
    self.forward()
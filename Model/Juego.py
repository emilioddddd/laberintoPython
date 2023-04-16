#!/usr/bin/python
#-*- coding: utf-8 -*-

from Laberinto import Laberinto
from Habitacion import Habitacion
from Puerta import Puerta
from Pared import Pared

class Juego:
    def __init__(self):
        self.laberinto=None

    def fabriacarHabitacion(unNum):
        hab = Habitacion(unNum)
        return hab

    def fabricarPared():
        return Pared()

    def fabricarPuertaLado1Lado2(hab1, hab2):
        puerta = Puerta()
        puerta.lado1=hab1
        puerta.lado2=hab2
        return puerta

    def fabricarLaberinto():
        return Laberinto()

    def laberinto2Habitaciones(self):
        self.laberinto=Laberinto()

        hab1 = Habitacion(1)
        hab2 = Habitacion(2)

        puerta=Puerta()
        puerta.lado1=hab1
        puerta.lado2=hab2

        hab1.norte=Pared()
        hab1.este = Pared()
        hab1.oeste=Pared()

        hab2.sur=Pared()
        hab2.este = Pared()
        hab2.oeste=Pared()

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def laberinto2HabitacionesFM(self):
        self.laberinto= self.fabricarLaberinto()

        hab1 = self.fabriacarHabitacion(1)
        hab2 = self.fabriacarHabitacion(2)

        puerta=self.fabricarPuertaLado1Lado2(hab1, hab2)

        hab1.norte = self.fabricarPared()
        hab1.este = self.fabricarPared()
        hab1.oeste = self.fabricarPared()

        hab2.sur = self.fabricarPared()
        hab2.este = self.fabricarPared()
        hab2.oeste = self.fabricarPared()

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

juego = Juego()
juego.laberinto2Habitaciones()


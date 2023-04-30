#!/usr/bin/python
#-*- coding: utf-8 -*-

from Contenedor import Contenedor

class Habitacion(Contenedor):
    """Este es concreateComplement"""
    def __init__(self):
        pass

    def entrar(self):
        print("Estas en la habitacion",self.num)



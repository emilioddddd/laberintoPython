#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):
    """Este es concreateComplement"""
    def __init__(self, num):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.num = num


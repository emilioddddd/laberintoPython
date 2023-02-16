#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self):
        self.Abierta = None
        self.Lado1 = None
        self.Lado2 = None

